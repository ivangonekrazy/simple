import sys
from os.path import realpath, dirname
from os.path import join as path_join

this_dir = dirname(realpath(__file__))
activate_this = path_join(this_dir, 'bin','activate_this.py')
execfile(activate_this, dict(__file__=activate_this))

sys.path.insert(0, this_dir)
from simple import app as application
