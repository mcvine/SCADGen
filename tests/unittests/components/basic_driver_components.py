"""
$ python basic_driver_operations.py             # run all tests
$ python basic_driver_operations.py block       # run block tests
"""

from __future__ import absolute_import

import sys
feature = sys.argv[1].capitalize() if len(sys.argv)>1 else ''

import os
sys.path.append(os.path.abspath("../../../SCADGen/python"))

import glob
from Parser import Parser

filelist = glob.glob(os.path.abspath(".")+"/%s*.xml" % feature)
for fname in filelist:
    parser = Parser(fname)
    parser.createSCAD()
