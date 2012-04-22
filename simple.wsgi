import sys
from os.path import realpath, dirname
from os.path import join as path_join

activate_this = path_join(dirname(realpath(__file__)), 'bin','activate_this.py')
execfile(activate_this, dict(__file__=activate_this))

sys.path.insert(0, '/home/ivan/workspace/simple')
from simple import app as application
