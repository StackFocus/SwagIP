#!/usr/bin/python
import sys, os
sys.path.insert (0,'/opt/swagip/git')
os.chdir('/opt/swagip/git')

activate_this = '/opt/swagip/env/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

from swagip import app as application
