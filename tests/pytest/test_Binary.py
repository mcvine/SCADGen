from __future__ import absolute_import

import sys
import os
sys.path.append(os.path.abspath("../../SCADGen/python"))

import xml.etree.ElementTree as et
from Parser import Parser
import components
import operations

def test_difference():
    fname = os.path.abspath("../unittests/operations/Difference.xml")
    p = Parser(fname)
    test = p.rootelems[0]
    elem1 = et.Element("cylinder", { "height" : "5", "radius" : "2.5" })
    elem2 = et.Element("cone", { "height" : "5", "topRadius" : "0", "bottomRadius" : "2.5" })
    sol = operations.Difference()
    sol.comp1 = components.Cylinder(elem1)
    sol.comp2 = components.Cone(elem2)
    assert(test == sol)

def test_intersection():
    fname = os.path.abspath("../unittests/operations/Intersection.xml")
    p = Parser(fname)
    test = p.rootelems[0]
    elem1 = et.Element("sphere", { "radius" : "5" })
    elem2 = et.Element("block", { "diagonal" : "(5, 5, 1)" })
    sol = operations.Intersection()
    sol.comp1 = components.Sphere(elem1)
    sol.comp2 = components.Block(elem2)
    assert(test == sol)

def test_union():
    fname = os.path.abspath("../unittests/operations/Union.xml")
    p = Parser(fname)
    test = p.rootelems[0]
    elem1 = et.Element("sphere", { "radius" : "2.5" })
    elem2 = et.Element("cylinder", { "height" : "5", "radius" : "1" })
    sol = operations.Union()
    sol.comp1 = components.Sphere(elem1)
    sol.comp2 = components.Cylinder(elem2)
    assert(test == sol)
