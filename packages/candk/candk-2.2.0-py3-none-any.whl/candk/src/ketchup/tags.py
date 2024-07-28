
from src.ketchup.spread import Spread, InlineSpread, RenderTypes


#########  TAG SPREADS  #########
#################################

def get_spread(tag = None):
	if tag == '@byline':
		return BylineTag(tag)
	elif tag == '@imports':
		return ImportsTag(tag)
	elif tag == '@class':
		return ClassTag(tag)
	elif tag == '@method':
		return MethodTag(tag)
	elif tag in ['@return', '@returns']:
		return ReturnTag(tag)
	elif tag in ['@deflist', '@params', '@constants', '@attributes']:
		return DeflistTag(tag)
	elif tag in ['@h1','@h2','@h3','@h4','@m1','@m2','@m3','@m4']:
		return HeaderTag(tag)
	elif tag == '@table':
		return TableTag(tag)
	elif tag == '@hr':
		return HrTag(tag)
	elif tag == '@br':
		return BrTag(tag)
	elif tag == '@codeblock':
		return CodeblockTag(tag)
	elif tag == '@literal':
		return LiteralTag(tag)
	elif tag == '@note':
		return NoteTag(tag)
	elif tag in ['@bulleted', '@non-bulleted', '@numbered']:
		return ListTag(tag)
	else:
		return ParagraphTag()


class ParagraphTag(InlineSpread):
	pass


class BylineTag(InlineSpread):

	def add_text(self, text, render_type = RenderTypes.HTML, preserve_linebreaks = False):
		text = super().render_text(text, render_type)
		self.text += text + '\n'

	def render(self, index, render_type = RenderTypes.HTML):
		result = ''
		if render_type == RenderTypes.HTML:
			result += '<div id="' + index + '" class="k-byline">'
			for line in self.text.splitlines():
				result += '<div class="k-byline-line">' + self.render_text(line) + '</div>'
			result += '</div>'
		elif render_type == RenderTypes.MARKDOWN:
			for line in self.text.splitlines():
				result += '> * ' + self.render_text(line, render_type) + '\n'
			result += '\n'
		return result


class ImportsTag(Spread):

	def add_text(self, text, render_type = RenderTypes.HTML, preserve_linebreaks = False):
		text = super().render_text(text, render_type)
		self.text += text + '\n'

	def render(self, index, render_type = RenderTypes.HTML):
		result = ''
		if render_type == RenderTypes.HTML:
			result += '<div id="' + index + '" class="k-imports">\n'
			result += 'Imports:'
			for line in self.text.splitlines():
				result += '<div class="k-imports-line">' + line + '</div>'
			result += '</div>'
		elif render_type == RenderTypes.MARKDOWN:
			result += '**Imports:**\n\n'
			for line in self.text.splitlines():
				result += '* ```' + line + '```\n'
			result += '\n'
		return result


class ClassTag(Spread):

	def render(self, index, render_type = RenderTypes.HTML):
		result = ''
		if render_type == RenderTypes.HTML:
			result += '<div id="' + index + '" class="k-class">' + self.text + '</div>'
		elif render_type == RenderTypes.MARKDOWN:
			result += '## ```' + self.text + '```\n\n'
		return result


class MethodTag(Spread):

	def render(self, index, render_type = RenderTypes.HTML):
		result = ''
		if render_type == RenderTypes.HTML:
			result += '<div id="' + index + '" class="k-method">' + self.text + '</div>'
		elif render_type == RenderTypes.MARKDOWN:
			result += '#### ```' + self.text + '```\n'
		return result


class HeaderTag(Spread):

	def __init__(self, tag = None):
		self.text = ''
		self.type = tag
		self.tag = tag

	def render(self, index, render_type = RenderTypes.HTML):
		result = ''
		tag_type = self.tag[1:]
		if render_type == RenderTypes.HTML:
			result += '<div id="' + index + '" class="k-' + tag_type + '">' + self.text + '</div>'
		elif render_type == RenderTypes.MARKDOWN:
			result += '#'*int(tag_type[1:]) + ' ' + self.text + '\n'
		return result


class TableTag(InlineSpread):

	def add_text(self, text, render_type = RenderTypes.HTML, preserve_linebreaks = False):
		if render_type == RenderTypes.HTML:
			text = text.replace('<', '&lt;')
			text = text.replace('>', '&gt;')
		elif render_type == RenderTypes.MARKDOWN:
			text = text.replace('[', '\[')
			text = text.replace('+', '\+')
		self.text += text + '\n'

	def render(self, index, render_type = RenderTypes.HTML):
		result = ''
		if render_type == RenderTypes.HTML:
			result += '<table class="k-table">'
			header = True
			for line in self.text.splitlines():
				if len(line) > 2 and line[:3] == '---':
					header = False
				else:
					cells = line.split('|')
					result += '<tr>'
					for cell in cells:
						cell = cell.strip()
						if header:
							result += '<th>' + self.render_text(cell, render_type) + '</th>'
						else:
							result += '<td>' + self.render_text(cell, render_type) + '</td>'
					result += '</tr>'
			result += '</table>\n'
		elif render_type == RenderTypes.MARKDOWN:
			header = True
			num_cells = 0
			for line in self.text.splitlines():
				if len(line) > 2 and line[:3] == '---':
					header = False
					for i in range(num_cells):
						result += '|---'
					result += '|\n'
				else:
					cells = line.split('|')
					num_cells = len(cells)
					for cell in cells:
						cell = cell.strip()
						result += '| ' + self.render_text(cell, render_type) + ' '
					result += '|\n'
			result += '\n'
		return result


class HrTag(Spread):

	def render(self, index, render_type = RenderTypes.HTML):
		result = ''
		if render_type == RenderTypes.HTML:
			result += '<hr />\n'
		elif render_type == RenderTypes.MARKDOWN:
			result += '----------------------------------------\n'
		return result


class BrTag(Spread):

	def render(self, index, render_type = RenderTypes.HTML):
		result = ''
		if render_type == RenderTypes.HTML:
			result += '<div class="k-break"></div>\n'
		elif render_type == RenderTypes.MARKDOWN:
			result += '\n\n'
		return result


class CodeblockTag(Spread):

	def add_text(self, text, render_type = RenderTypes.HTML, preserve_linebreaks = False):
		if render_type == RenderTypes.HTML:
			text = text.replace('<', '&lt;')
			text = text.replace('>', '&gt;')
		self.text += text

	def render(self, index, render_type = RenderTypes.HTML):
		result = ''
		if render_type == RenderTypes.HTML:
			result += '<div id="' + index + '" class="k-codeblock">'
			result += self.text
			result += '</div>'
		elif render_type == RenderTypes.MARKDOWN:
			result += '```\n'
			result += self.text
			result += '\n```\n\n'
		return result


class LiteralTag(Spread):

	def add_text(self, text, render_type = RenderTypes.HTML, preserve_linebreaks = False):
		self.text += text

	def render(self, index, render_type = RenderTypes.HTML):
		result = ''
		if render_type == RenderTypes.HTML:
			text = self.text
			for line in text.splitlines():
				result += line + '<br/>'
		elif render_type == RenderTypes.MARKDOWN:
			result = self.text + '\n\n'
		return result


class NoteTag(InlineSpread):

	def render(self, index, render_type = RenderTypes.HTML):
		result = ''
		if render_type == RenderTypes.HTML:
			result += '<table id="' + index + '" class="k-note">'
			result += '<tr><td class="k-note-note">NOTE:</td>'
			result += '<td>'
			result += self.render_text(self.text, render_type)
			result += '</td></tr></table>'
		elif render_type == RenderTypes.MARKDOWN:
			result += '**NOTE:** ' + self.render_text(self.text, render_type) + '\n\n'
		return result


class ReturnTag(InlineSpread):

	def render(self, index, render_type = RenderTypes.HTML):
		result = ''
		if render_type == RenderTypes.HTML:
			result += '<div id="' + index + '" class="k-return">'
			result += 'Returns:'
			result += '<div class="k-return_desc">'
			result += self.render_text(self.text, render_type)
			result += '</div></div>'
		elif render_type == RenderTypes.MARKDOWN:
			result += '**Returns:** ' + self.render_text(self.text, render_type) + '\n\n'
		return result


class DeflistTag(InlineSpread):

	def __init__(self, tag = None):
		self.text = ''
		self.type = tag
		self.tag = tag
		self.title = ''
		self.table_class = 'def'
		if tag == '@params':
			self.title = 'Parameters:'
			self.table_class = 'params'
		elif tag == '@attributes':
			self.title = 'Attributes:'
			self.table_class = 'attributes'
		elif tag == '@exceptions':
			self.title = 'Exceptions:'
			self.table_class = 'exceptions'
		elif tag == '@constants':
			self.title = 'Constants:'
			self.table_class = 'constants'

	def add_text(self, text, render_type = RenderTypes.HTML, preserve_linebreaks = False):
		if render_type == RenderTypes.HTML:
			text = text.replace('<', '&lt;')
			text = text.replace('>', '&gt;')
		elif render_type == RenderTypes.MARKDOWN:
			text = text.replace('[', '\[')
			text = text.replace('+', '\+')
		if ':' in text:
			self.text += '\n'
		else:
			self.text += ' '
		if preserve_linebreaks:
			self.text += '@'
		self.text += text

	def render(self, index, render_type = RenderTypes.HTML):
		result = ''
		if render_type == RenderTypes.HTML:
			result += '<div id="' + index + '" class="k-params">'
			result += self.title
			result += '<table class="k-'+ self.table_class +'">'
			for line in self.text.splitlines():
				splits = line.split(':', 1)
				if len(splits) == 2:
					result += '<tr><td class="k-var_name">' + splits[0].strip() + '</td><td class="k-var_desc">' + self.render_text(splits[1].strip()) + '</td></tr>'
			result += '</table></div>'
		elif render_type == RenderTypes.MARKDOWN:
			if self.title:
				result += '**' + self.title + '**\n\n'
			for line in self.text.splitlines():
				splits = line.split(':', 1)
				if len(splits) == 2:
					result += '* ```' + splits[0].strip() + '```: ' + self.render_text(splits[1].strip(), render_type) + '\n'
			result += '\n'
		return result


class ListTag(InlineSpread):

	def __init__(self, tag = None):
		self.text = ''
		self.type = tag
		self.tag = tag

	def add_text(self, text, render_type = RenderTypes.HTML, preserve_linebreaks = False):
		if render_type == RenderTypes.HTML:
			text = text.replace('<', '&lt;')
			text = text.replace('>', '&gt;')
		elif render_type == RenderTypes.MARKDOWN:
			text = text.replace('[', '\[')
			text = text.replace('+', '\+')
		if text[0] in ['-', '*', '#']:
			self.text += '\n'
		else:
			self.text += ' '
		if preserve_linebreaks:
			self.text += '@'
		self.text += text

	def render(self, index, render_type = RenderTypes.HTML):
		result = ''
		if self.tag == '@non-bulleted':
			tag = 'ul'
			mark = '-'
		elif self.tag == '@bulleted':
			tag = 'ul'
			mark = '*'
		elif self.tag == '@numbered':
			tag = 'ol'
			mark = '#'
		list_type = self.tag[1:]
		level = 1
		if render_type == RenderTypes.HTML:
			result += '<' + tag + ' id="' + index + '" class="k-' + list_type + '">\n'
			for line in self.text.splitlines():
				if len(line) > 1 and line[:2] == mark + ' ':
					if level > 1:
						# close the list
						for i in range(level, 1, -1):
							result += '</' + tag + '>\n'
					elif level < 1:
						result += '<' + tag + '>\n'
					level = 1
					result += '<li>' + self.render_text(line[2:], render_type) + '</li>\n'
				if len(line) > 2 and line[:3] == (mark*2) + ' ':
					if level > 2:
						# close the list
						for i in range(level, 2, -1):
							result += '</' + tag + '>\n'
					if level < 2:
						result += '<' + tag + '>\n'
					result += '<li>' + self.render_text(line[3:], render_type) + '</li>\n'
					level = 2
				if len(line) > 3 and line[:4] == (mark*3) + ' ':
					if level > 3:
						# close the list
						for i in range(level, 3, -1):
							result += '</' + tag + '>\n'
					if level < 3:
						result += '<' + tag + '>\n'
					result += '<li>' + self.render_text(line[4:], render_type) + '</li>\n'
					level = 3
				if len(line) > 4 and line[:5] == (mark*4) + ' ':
					if level > 4:
						# close the list
						for i in range(level, 4, -1):
							result += '</' + tag + '>\n'
					if level < 4:
						result += '<' + tag + '>\n'
					result += '<li>' + self.render_text(line[5:], render_type) + '</li>\n'
					level = 4

			for i in range(level, 0, -1):
				result += '</' + tag + '>\n'
		elif render_type == RenderTypes.MARKDOWN:
			if self.tag == '@non-bulleted':
				tag = '- '
				mark = '-'
			elif self.tag == '@bulleted':
				tag = '* '
				mark = '*'
			elif self.tag == '@numbered':
				tag = '1. '
				mark = '#'
			for line in self.text.splitlines():
				if len(line) > 1 and line[:2] == mark + ' ':
					result += tag + self.render_text(line[2:], render_type) + '\n'
				if len(line) > 2 and line[:3] == (mark*2) + ' ':
					result += '  ' + tag + self.render_text(line[3:], render_type) + '\n'
				if len(line) > 3 and line[:4] == (mark*3) + ' ':
					result += '    ' + tag + self.render_text(line[4:], render_type) + '\n'
				if len(line) > 4 and line[:5] == (mark*4) + ' ':
					result += '      ' + tag + self.render_text(line[5:], render_type) + '\n'
			result += '\n'
		return result















