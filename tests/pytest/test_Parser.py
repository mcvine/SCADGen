from __future__ import absolute_import

import filecmp
import sys
import os
sys.path.append(os.path.abspath("../../SCADGen/python"))

import xml.etree.ElementTree as et
from Parser import Parser
import components
import operations

def test_parsercore():
    fname = os.path.abspath("./test_xmls/parser_test.xml")
    elem1 = et.Element("cylinder", { "radius" : "1.5", "height" : "10" })
    elem2 = et.Element("cylinder", { "radius" : "2.5", "height" : "5" })
    comp1 = components.Cylinder(elem1)
    comp2 = components.Cylinder(elem2)
    op = operations.Translation("(0, 0, -2.5)")
    op.body = comp1
    sol = operations.Union()
    sol.comp1 = comp2
    sol.comp2 = op
    p = Parser(fname)
    test = p.rootelems[0]
    assert(test == sol)

def test_generateSCAD():    
    fname = os.path.abspath("./test_xmls/parser_test.xml")
    p = Parser(fname)
    p.createSCAD()
    test = os.path.abspath("./test_xmls/parser_test.scad")
    sol = os.path.abspath("./test_xmls/parser_sol.scad")
    assert(filecmp.cmp(test, sol, shallow=False) == True)
