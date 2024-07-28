

'''
def add_paths_to_system (paths):
	import pathlib
	from os.path import dirname, join, normpath
	import sys
	
	this_folder = pathlib.Path (__file__).parent.resolve ()	
	for path in paths:
		sys.path.insert (0, normpath (join (this_folder, path)))

add_paths_to_system ([
	'../../../structures_pip'
])
'''


import pathlib
from os.path import dirname, join, normpath
import os
import sys

this_folder = pathlib.Path (__file__).parent.resolve ()
habitat = "/habitat"
monitors = str (normpath (join (this_folder, "monitors")))

os.chdir (this_folder)

if (len (sys.argv) >= 2):
	glob_string = monitors + '/' + sys.argv [1]
else:
	glob_string = monitors + '/**/monitor_*.py'

import biotech

scan = biotech.start (
	glob_string = glob_string,
	simultaneous = True,
	module_paths = [
		normpath (join (habitat, "parties"))
	],
	relative_path = monitors
)



#
#
#