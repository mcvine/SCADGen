from __future__ import absolute_import

import sys
import os
sys.path.append(os.path.abspath("../../python"))

import glob
from Parser import Parser

filelist = glob.glob(os.path.abspath(".")+"/*.xml")
for fname in filelist:
    parser = Parser(fname)
    parser.createSCAD()
