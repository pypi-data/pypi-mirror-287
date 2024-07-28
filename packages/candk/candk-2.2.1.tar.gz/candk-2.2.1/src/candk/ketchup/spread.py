
KETCHUP_TAGS = ['@byline',		# multiline
				'@imports',		# multiline
				'@class',		# single line
				'@method',		# single line
				'@attributes',	# multiline list
				'@constants',	# multiline list
				'@params',		# multiline list
				'@return',		# single line
				'@returns',		# single line
				'@exceptions',	# multiline list
				'@deflist',		# multiline list
				'@h1','@h2',	# single line
				'@h3','@h4',	# single line
				'@m1','@m2',	# single line
				'@m3','@m4',	# single line
				'@table',		# multiline
				'@hr',			# horizontal rule
				'@br',			# break line
				'@codeblock',	# multiline
				'@endcodeblock',# end tag
				'@codeblockend',# alternate end tag
				'@literal',		# multiline
				'@endliteral',	# end tag
				'@literalend',	# alternate end tag
				'@note',		# single line
				'@page',		# single line
				'@file',		# single line
				'@outdir',		# single line
				]

FRONTLINE_TAGS = {
				'-': '@non-bulleted',
				'*': '@bulleted',
				'#': '@numbered',
				}

# render types
class RenderTypes:
	HTML = 'html'
	MARKDOWN = 'md'
				

########  BASE SPREAD  ########
###############################

class Spread():

	def __init__(self, tag = None):
		self.type = tag
		self.text = ''

	def __str__(self):
		return str(self.type)

	def is_empty(self):
		return self.text == ''

	def add_text(self, text, render_type = RenderTypes.HTML, preserve_linebreaks = False):
		if render_type == RenderTypes.HTML:
			text = text.replace('<', '&lt;')
			text = text.replace('>', '&gt;')
		elif render_type == RenderTypes.MARKDOWN:
			text = text.replace('[', '\[')
			text = text.replace('+', '\+')
		self.text += ' ' + text

	def render_text(self, text, render_type = RenderTypes.HTML):
		if render_type == RenderTypes.HTML:
			text = text.replace('<', '&lt;')
			text = text.replace('>', '&gt;')
		elif render_type == RenderTypes.MARKDOWN:
			text = text.replace('[', '\[')
			text = text.replace('+', '\+')
		return text

	def render(self, index, render_type = RenderTypes.HTML):
		result = ''
		if render_type == RenderTypes.HTML:
			result += '<div id="' + index + '" class="k-paragraph">' + self.render_text(self.text, ) + '</div>'
		elif render_type == RenderTypes.MARKDOWN:
			result += '\n' + self.render_text(self.text, render_type) + '\n'
		return result


########  INLINE SPREAD  ########
#################################

class InlineSpread(Spread):

	def add_text(self, text, render_type = RenderTypes.HTML, preserve_linebreaks = False):
		if render_type == RenderTypes.HTML:
			text = text.replace('<', '&lt;')
			text = text.replace('>', '&gt;')
		elif render_type == RenderTypes.MARKDOWN:
			text = text.replace('[', '\[')
			text = text.replace('+', '\+')
		if preserve_linebreaks:
			self.text += '@' + text
		else:
			self.text += ' ' + text

	def render_text(self, text, render_type = RenderTypes.HTML):
		text = super().render_text(text, render_type)
		return self.render_inline(text, render_type)


	def render_inline(self, text, render_type = RenderTypes.HTML):
		result = ''
		disregard_next = False
		codeline_start = False
		codeline_end = False
		link_text = ''
		tag = None
		bold = False
		italic = False
		for i in range(len(text)):
			char = text[i]
			if char == '\\':
				disregard_next = True
			elif disregard_next:
				disregard_next = False
				result += char
			else:
				if tag == 'codeline':
					if (char == '-' and (i < (len(text)-1) and text[i+1] == '/')) or (codeline_end and char == '/'):
						codeline_end = True
					else:
						codeline_end = False
					if char == '/' and codeline_end:
						if render_type == RenderTypes.HTML:
							result += '</span>'
						elif render_type == RenderTypes.MARKDOWN:
							result += '```'
						codeline_start = False
						codeline_end = False
						tag = None
					elif char == '-' and (codeline_end or codeline_start):
						pass
					else:
						codeline_start = False
						result += char
						codeline_end = False
				elif char == '/' and (i == 0 or text[i-1] == ' ') and tag not in ['code', 'codeline']:
					if i < (len(text)-1) and text[i+1] == '-':
						tag = 'codeline'
						codeline_start = True
					else:
						tag = 'code'
					if render_type == RenderTypes.HTML:
						result += '<span class="k-code">'
					elif render_type == RenderTypes.MARKDOWN:
						result += '```'
				elif char == ' ' and tag == 'code':
					if render_type == RenderTypes.HTML:
						result += '</span> '
					elif render_type == RenderTypes.MARKDOWN:
						result += '```'
					tag = None
				elif char == '!' and (i == 0 or text[i-1] == ' ') and tag not in ['link']:
					tag = 'link'
					link_text = ''
					if render_type == RenderTypes.HTML:
						result += '<a class="k-link" target="_blank" href="'
					elif render_type == RenderTypes.MARKDOWN:
						result += '['
				elif char == ' ' and tag == 'link':
					if render_type == RenderTypes.HTML:
						result += '">' + link_text + '</a> '
					elif render_type == RenderTypes.MARKDOWN:
						result = link_text + '](' + link_text + ')'
					tag = None
				elif char == '*' and tag is None:
					if (i < (len(text)-1) and text[i+1] != ' ') and not bold:
						bold = True
						if render_type == RenderTypes.HTML:
							result += '<strong>'
						elif render_type == RenderTypes.MARKDOWN:
							result += '**'
					elif bold:
						bold = False
						if render_type == RenderTypes.HTML:
							result += '</strong>'
						elif render_type == RenderTypes.MARKDOWN:
							result += '**'
				elif char == '_' and tag is None:
					if (i < (len(text)-1) and text[i+1] != ' ') and not italic:
						italic = True
						if render_type == RenderTypes.HTML:
							result += '<em>'
						elif render_type == RenderTypes.MARKDOWN:
							result += '_'
					elif italic:
						italic = False
						if render_type == RenderTypes.HTML:
							result += '</em>'
						elif render_type == RenderTypes.MARKDOWN:
							result += '_'
				elif char =='@' and tag is None:
					if render_type == RenderTypes.HTML:
						result += '<br />'
					if render_type == RenderTypes.MARKDOWN:
						result += '<br />'
				else:
					if tag == 'link':
						link_text += char
					result += char
		if tag in ['code','codeline']:
			if render_type == RenderTypes.HTML:
				result += '</span> '
			elif render_type == RenderTypes.MARKDOWN:
				result += '```'
		elif tag in ['link']:
			if render_type == RenderTypes.HTML:
				result += '">' + link_text + '</a> '
			elif render_type == RenderTypes.MARKDOWN:
				result += '](' + link_text + ')'
		if bold:
			if render_type == RenderTypes.HTML:
				result += '</strong>'
			elif render_type == RenderTypes.MARKDOWN:
				result += '**'
		if italic:
			if render_type == RenderTypes.HTML:
				result += '</em>'
			elif render_type == RenderTypes.MARKDOWN:
				result += '_'

		return result





