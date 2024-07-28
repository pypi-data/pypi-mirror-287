
import os, sys
from pathlib import Path
from datetime import datetime

from src.ketchup.tags import get_spread
from src.ketchup.spread import KETCHUP_TAGS, FRONTLINE_TAGS, Spread, InlineSpread, RenderTypes


VERSION = '2.2.0'

source_path = Path(__file__).resolve()
source_dir = source_path.parent

STYLESHEET = os.path.join(source_dir, 'style.css')


########  BASE CLASSES  ########
################################

class Document():

	def __init__(self, filepath, page_name = None,
					output_name = None, output_dir = None,
					css_file = STYLESHEET,
					render_type = RenderTypes.HTML,
					preserves_linebreaks = False):
		self.page_name = page_name
		self.filepath = filepath
		self.output_name = output_name
		self.output_dir = output_dir
		self.css_file = css_file
		self.render_type = render_type
		self.preserves_linebreaks = preserves_linebreaks
		self.document = []


	def add_text(self, text):
		myfile = text.split('\n')
		parse_text(myfile)


	def parse_text(self, myfile):
		prev_line = None
		prev_spread = None
		spread = None
		empty_lines = 0
		for line in myfile:
			unstripped_line = line
			line = line.strip()

			if prev_line == '@page' and not spread:
				self.page_name = line
				pass
			elif prev_line == '@file' and not spread:
				self.output_name = line
				pass
			elif prev_line == '@outdir' and not spread:
				self.output_dir = line
				pass

			if line in KETCHUP_TAGS and (not spread or ( spread and spread.type not in ['@codeblock', '@literal', '@class', '@method'])):
				empty_lines = 0
				if spread and not spread.is_empty():
					self.document.append(spread)
					prev_spread = spread
					spread = None
				if line not in ['@page', '@file', '@outdir']:
					spread = get_spread(line)
				if spread and spread.type in ['@hr','@br']:
					self.document.append(spread)
					spread = None

			elif line == '' and (not spread or ( spread and spread.type not in ['@codeblock', '@literal'])):
				if spread and not spread.is_empty():
					self.document.append(spread)
					prev_spread = spread
				empty_lines += 1
				spread = None

			elif line in ['@endcodeblock', '@endliteral', '@codeblockend']:
				empty_lines = 0
				if spread and not spread.is_empty():
					self.document.append(spread)
					prev_spread = spread
				spread = None

			elif spread and spread.type in ['@codeblock', '@literal']:
				empty_lines = 0
				spread.add_text(unstripped_line, self.render_type, self.preserves_linebreaks)

			elif len(line) > 1 and line[0] in ['-', '*', '#'] and line[1] in ['-', '*', '#', ' '] and (not spread or spread.type not in ['@non-bulleted', '@bulleted', '@numbered', '@table', '@class', '@method']):
				empty_lines = 0
				if spread and not spread.is_empty():
					self.document.append(spread)
					prev_spread = spread
				tag = FRONTLINE_TAGS[line[0]]
				spread = get_spread(tag)
				spread.add_text(line, self.render_type, self.preserves_linebreaks)

			elif len(line) > 3 and line[:2] in ['@h', '@m'] and (not spread or spread.type not in ['@non-bulleted', '@bulleted', '@numbered', '@table', '@class', '@method']):
				empty_lines = 0
				if spread and not spread.is_empty():
					self.document.append(spread)
					prev_spread = spread
				tag = line[:3]
				spread = get_spread(tag)
				text = line[3:].strip()
				spread.add_text(text, self.render_type, self.preserves_linebreaks)

			elif len(line) > 2 and line[:3] == '___':
				empty_lines = 0
				if spread and not spread.is_empty():
					self.document.append(spread)
					prev_spread = spread
				spread = get_spread('@hr')
				self.document.append(spread)
				prev_spread = spread
				spread = None

			elif spread:
				empty_lines = 0
				spread.add_text(line, self.render_type, self.preserves_linebreaks)
			else:
				if prev_line not in ['@page', '@file', '@outdir']:
					if empty_lines == 3:
						spread = get_spread('@h1')
					elif empty_lines == 2:
						spread = get_spread('@h2')
					else:
						spread = get_spread()
					spread.add_text(line, self.render_type, self.preserves_linebreaks)
					empty_lines = 0
			prev_line = line

		if spread and not spread.is_empty():
			self.document.append(spread)
			prev_spread = spread
			spread = None


	def render(self, index):
		result = ''
		for i in range(len(self.document)):
			spread = self.document[i]
			result += spread.render(str(i), render_type = self.render_type) + '\n'
		return result




class Ketchup(Document):

	def begin(self):
		self.initialize_data()
		fullpath = os.path.abspath(self.filepath)
		self.parse_file(fullpath)
		filename, file_ext = os.path.splitext(self.filepath)
		filename = filename.replace('/', '.')
		filename = filename.replace('\\', '.')
		result = self.render(self.page_name)
		self.send_to_output(result, self.output_name, self.output_dir)


	def initialize_data(self):
		self.document = []
		filename, file_ext = os.path.splitext(self.filepath)
		filename = filename.replace('/', '.')
		filename = filename.replace('\\', '.')
		if self.page_name is None:
			self.page_name = filename
		if self.output_name is None:
			self.output_name = filename
		if self.output_dir is None:
			self.output_dir = os.getcwd()

		# if output_dir is not an absolute path, we need to make it one
		if not os.path.isabs(self.output_dir):
			self.output_dir = os.path.abspath(self.output_dir)


	def parse_file(self, filepath):
		with open(filepath, 'r') as myfile:
			self.parse_text(myfile)


	def minify_css(self, css_file):
		with open(css_file, 'r') as mycss:
			css = mycss.read()
			css = css.strip()
			css = css.replace('\t', '')
		return css


	def render_nav(self):
		result = '<div class="k-navbar">'
		for i in range(len(self.document)):
			spread = self.document[i]
			if spread.type in ['@h1','@h2']:
				num = spread.type[-1]
				result += '<a class="k-a" href="#' + str(i) + '"><div class="k-nav k-nav-header k-nh' + num + '">' + spread.text + '</div></a>\n'
			if spread.type == '@class':
				result += '<a class="k-a" href="#' + str(i) + '"><div class="k-nav k-nav-class">' + spread.text + '</div></a>\n'
			if spread.type == '@method':
				result += '<a class="k-a" href="#' + str(i) + '"><div class="k-nav k-nav-method">' + spread.text + '</div></a>\n'
		result += '</div>\n'
		return result


	def render(self, filename):
		result = ''
		if self.render_type == RenderTypes.HTML:
			result += '<html><head>\n'
			title = filename.split('.')[-1]
			result += '<title>' + title + '</title>\n'
			result += '<style>' + self.minify_css(self.css_file) + '</style>\n'
			result += '</head><body>\n'
			result += '<a class="k-a" href=""><div class="k-page-title">' + filename + '</div></a>\n'
			result += '<div class="k-page">\n'
			result += self.render_nav()
			result += '<div class="k-content">\n'

		for i in range(len(self.document)):
			spread = self.document[i]
			result += spread.render(str(i), render_type = self.render_type) + '\n'

		if self.render_type == RenderTypes.HTML:
			right_now = datetime.now()
			result += '<div class="k-spacer">Generated ' + right_now.strftime('%I:%M%p  %d %b %Y') + '</br>'
			result += 'Documentation generated by Ketchup v'+ VERSION +'</br>'
			result += 'Developed by Charles Koch - 2020</div>'
			result += '</div></div></body></html>'
		return result


	def send_to_output(self, text, output_name, output_dir):
		file_path = os.path.join(output_dir, output_name + '.' + self.render_type)
		with open(file_path, 'w') as outfile:
			outfile.write(text)

