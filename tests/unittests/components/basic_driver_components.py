"""
$ python basic_driver_components.py             # run all tests
$ python basic_driver_components.py block       # run block tests
"""

from __future__ import absolute_import

import sys
feature = sys.argv[1].capitalize() if len(sys.argv)>1 else ''

import os
sys.path.append(os.path.abspath("../../.."))

import glob
from SCADGen.Parser import Parser

filelist = glob.glob(os.path.abspath(".")+"/%s*.xml" % feature)
for fname in filelist:
    parser = Parser(fname)
    parser.createSCAD()
