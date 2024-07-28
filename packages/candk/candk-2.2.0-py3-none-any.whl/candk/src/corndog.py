import sys, os, re, getopt

HELP = """python corndog.py -frmh -s <path or file> -o <path> -n <name> -x <ext>

-f	Export results to a single file. By default the name of the file is
	'Corndog_out.txt' unless a different name and extension are provided via the
	-n and/or -x options.

-r	Parse files in subdirectories as well as the starting directory.

-m	Export results to multiple files, with each file corresponding to a source
	file. The files are named the same as the source file with the subfolders
	prepended by hyphens (-) and the extension '.txt'. The names cannot be set
	with the -n option, but the xtension can be changed with the -x option.

-h	Display the help. This will also display if any invalid options are given.

-s	The starting point for the parsing. By default the starting point is the
	current working directory. If a filename is given as the starting point,
	only that file will be parsed instead of the entire directory.

-o	The path for the output file. By default the output directory is the current
	working directory.

-n	Give the output file a specific name.

-x	Give the output file(s) a specific file extension.
"""

STREAM = 'stream'
SINGLE_FILE = 'single file'
ONE_TO_ONE = 'one to one'

# these are what mark the beginning of a comment
COMMENTS = {
	'.py': ['#','"""', "'''"],
	'.java': ['//', '/*', '/**'],
	'.sql': ['--', '/*', '/**'],
	'.xml': ['<!--'],
	'.html': ['<!--'],
	'.php': ['<!--', '//', '#'],
	'.ftl': ['<!--'],
	'.js': ['/*', '//'],
	'.css': ['/*', '/**'],
	'.c': ['/*'],
	'.cpp': ['/*', '/**'],
	'.sh': ['#'],
	'.bat': ['::', 'REM ', 'rem '],
	'.txt': [''],
	'.properties': ['#', '!'],
	'.kp': [''],
	'.tas': [':CD ', ':CM '],
	}
# these are characters to ignore at the beginning of a comment
IGNORES = {
	'.py': ['#'],
	'.java': [],
	'.sql': [],
	'.xml': [],
	'.html': [],
	'.php': [],
	'.ftl': [],
	'.js': [],
	'.css': [],
	'.c': [],
	'.cpp': [],
	'.sh': ['#'],
	'.bat': [],
	'.txt': [],
	'.properties': ['#', '!'],
	'.kp': [],
	'.tas': [],
	}
# these are marks that should be removed if they are in a comment
REPLACES = {
	'.py': ['//','"""', "'''"],
	'.java': ['//', '/*', '/**', '*/'],
	'.sql': ['//','--', '/*', '/**', '*/'],
	'.xml': ['//','-->'],
	'.html': ['//','-->'],
	'.php': ['//','-->'],
	'.ftl': ['//','-->'],
	'.js': ['//', '/*', '/**', '*/'],
	'.css': ['//', '/*', '/**', '*/'],
	'.c': ['//', '/*', '/**', '*/'],
	'.cpp': ['//', '/*', '/**', '*/'],
	'.sh': ['//'],
	'.bat': ['::', 'REM ', 'rem '],
	'.txt': ['//'],
	'.properties': ['//'],
	'.kp': ['//'],
	'.tas': ['//',':CD ', ':CM '],
}

class Corndog():

	def __init__(self, start_point = None, search_subs = False, output = STREAM, output_name = 'Conrdog_out', output_ext = '.txt', output_dir = None):
		self._configure(start_point, search_subs, output, output_name, output_ext, output_dir)


	def _configure(self, start_point, search_subs, output, output_name, output_ext, output_dir):
		self.start_point = start_point
		self.search_subs = search_subs
		self.output = output
		self.output_name = output_name
		self.output_ext = output_ext
		self.output_dir = output_dir
		self.final_text = ''
		self.original_start = self.start_point

		self.initialize_data()


	def initialize_data(self):
		if self.start_point is None:
			self.start_point = os.getcwd()

		# if start_point is not an absolute path, we need to make it one
		if not os.path.isabs(self.start_point):
			self.start_point = os.path.abspath(self.start_point)

		self.original_start = self.start_point

		#print(self.original_start)

		# if start_point is a file, we need to set the start point to the directory itself
		if os.path.isfile(self.start_point):
			self.start_point = os.path.dirname(os.path.abspath(self.start_point))

		if self.output_dir is None:
			self.output_dir = self.start_point

		# if output_dir is not an absolute path, we need to make it one
		if not os.path.isabs(self.output_dir):
			self.output_dir = os.path.abspath(self.output_dir)


	def begin(self):
		self.initialize_data()
		search_type = 'file'

		# determine if start_point is a file or a directory
		if os.path.isfile(self.original_start):
			search_type = 'file'
		if os.path.isdir(self.original_start):
			search_type = 'dir'

		if search_type == 'file':
			# if it's a file, just parse it and output it
			os.chdir(self.start_point)
			text = self.parse_file(self.original_start)
			self.send_to_output(text, self.output, self.output_name, self.output_ext, self.output_dir)
		elif search_type == 'dir':
			self.final_text = ''
			self._search_dir(self.start_point, first_dir = True)
			if self.output == SINGLE_FILE:
				self.send_to_output(self.final_text, self.output, self.output_name, self.output_ext, self.output_dir)

	def _search_dir(self, root, first_dir = False, prev_name = ''):
		os.chdir(root)
		if not first_dir:
			dirname = prev_name + os.path.basename(root) + '-'
		else:
			dirname = ''
		for entry in os.listdir(root):
			full_path = os.path.abspath(entry)
			if os.path.isfile(entry):
				text = self.parse_file(full_path)
				filename, file_ext = os.path.splitext(entry)
				file_ext = file_ext.lower()
				filename = dirname + filename
				if text != '' and text is not None:
					if self.output == ONE_TO_ONE or self.output == STREAM:
						self.send_to_output(text, self.output, filename, self.output_ext, self.output_dir)
					else:
						self.final_text += text + '\n'
			elif os.path.isdir(entry) and self.search_subs:
				self._search_dir(full_path, prev_name = dirname)
				os.chdir(root)


	def send_to_output(self, text, output, output_name = 'Corndog_out', output_ext = '.txt', output_dir = None):
		if output_dir is None:
			output_dir = os.getcwd()
		file_path = os.path.join(output_dir, output_name + output_ext)
		#print 'SEND TO: ' + file_path
		if output == STREAM:
			print(text)
		elif output == SINGLE_FILE or output == ONE_TO_ONE:
			with open(file_path, 'w') as outfile:
				outfile.write(text)


	def parse_file(self, filepath):
		#print 'READING: ' + filepath
		start_fetch = False
		result = ''
		# determine file type (via the extension)
		myname, file_ext = os.path.splitext(filepath)
		file_ext = file_ext.lower()
		if file_ext not in COMMENTS.keys():
			# uh oh! we got a file that is not supported!
			#print('File Type Not Supported')
			return result
		# set correct comment markers
		lookers = []
		# for mark in COMMENTS[file_ext]:
		# 	lookers.append(mark + '-==')
		lookers = ['-==']
		ignores = ' \t'
		for mark in IGNORES[file_ext]:
			ignores += mark
		# read the file
		with open(filepath, 'r') as myfile:
			for line in myfile:
				if start_fetch:
					# if we've started a fetch, lets capture this!
					if line.strip() == '':
						start_fetch = False
						result += '\n'
					else:
						# remove all of the marks identified as ignores or replaces
						line = line.lstrip(ignores)
						if file_ext == '.tas' and len(line) > 3 and line[:4] not in COMMENTS['.tas']:
							# must be in a TaskBuilder file
							# can only read comment sections
							start_fetch = False
							result += '\n'
						else:
							for mark in REPLACES[file_ext]:
								line = line.replace(mark, '')
							line = line.replace('-==', '\n')
							if line.strip() != '':
								result += line
							else:
								start_fetch = False
								result += '\n'
				else:
					# if we haven't started a fetch, lets check
					for looker in lookers:
						if looker in line:
							start_fetch = True
							line = line.lstrip(ignores)
							if file_ext == '.tas' and len(line) > 3 and line[:4] not in COMMENTS['.tas']:
								# must be in a TaskBuilder file
								# can only read comment sections
								start_fetch = False
								result += '\n'
							else:
								for mark in REPLACES[file_ext]:
									line = line.replace(mark, '')
								line = line.replace('-==', '')
								result += line
		if result.strip() != '':
			result += '\n'

		return result



def main():

	showhelp = False
	optlist = []
	try:
		optlist, args = getopt.gnu_getopt(sys.argv[1:], 'fmrhn:x:o:s:')
	except getopt.GetoptError:
		showhelp = True

	cd = Corndog()

	for o, arg in optlist:
		if o == '-r':
			cd.search_subs = True
		if o == '-m':
			cd.output = ONE_TO_ONE
		if o == '-f':
			cd.output = SINGLE_FILE
		if o == '-h':
			showhelp = True
		if o == '-n':
			cd.output_name = arg
		if o == '-x':
			cd.output_ext = arg
		if o == '-o':
			cd.output_dir = arg
		if o == '-s':
			cd.start_point = arg


	if showhelp:
		print(HELP)
		return

	cd.begin()

if __name__ == '__main__':
	main()








