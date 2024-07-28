import os, sys, getopt
from src.corndog import Corndog, STREAM, SINGLE_FILE, ONE_TO_ONE
from src.ketchup.base import Ketchup

HELP = """python corndog.py -frmh -s <path or file> -o <path> -n <name> -x <ext>

-f	Export results to a single file. By default the name of the file is
	'Corndog_out.txt' unless a different name and extension are provided via the
	-n and/or -x options.

-r	Parse files in subdirectories as well as the starting directory.

-m	Export results to multiple files, with each file corresponding to a source
	file. The files are named the same as the source file with the subfolders
	prepended by hyphens (-) and the extension '.txt'. The names cannot be set
	with the -n option, but the extension can be changed with the -x option.

-h	Display the help. This will also display if any invalid options are given.

-s	The starting point for the parsing. By default the starting point is the
	current working directory. If a filename is given as the starting point,
	only that file will be parsed instead of the entire directory.

-o	The path for the output file. By default the output directory is the current
	working directory.

-n	Give the output file a specific name.

-x	Give the output file(s) a specific file extension.
"""

class CorndogWithKetchup(Corndog):

	# def __init__(self, start_point = None, search_subs = False, output = STREAM, output_name = 'Conrdog_out', output_ext = '.txt', output_dir = None):
	# 	super().__init__(start_point = start_point, search_subs = search_subs, output = output, output_name = output_name, output_ext = output_ext, output_dir = output_dir)

	def send_to_output(self, text, output, output_name = 'Corndog_out', output_ext = '.txt', output_dir = None):
		output_name = output_name.replace('-', '.')
		super().send_to_output(text, output, output_name = output_name, output_ext = '.kp', output_dir = output_dir)
		filename = output_name + output_ext
		file = os.path.join(output_dir, filename)
		prev_dir = os.getcwd()
		os.chdir(output_dir)
		kp = Ketchup(filename, output_dir = output_dir)
		kp.begin()
		os.remove(filename)
		os.chdir(prev_dir)


def main():

	showhelp = False
	optlist = []
	try:
		optlist, args = getopt.getopt(sys.argv[1:], 'fmrhn:o:s:')
	except getopt.GetoptError:
		showhelp = True

	cd = CorndogWithKetchup(output_ext = '.kp', output = ONE_TO_ONE)

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