from __future__ import absolute_import

import sys
import os
sys.path.append(os.path.abspath("../../SCADGen/python"))

import xml.etree.ElementTree as et
from Parser import Parser
import components
import operations

def test_dilation():
    fname = os.path.abspath("../unittests/operations/Dilation.xml")
    p = Parser(fname)
    test = p.rootelems[0]
    elem1 = et.Element("block", { "diagonal" : "(1, 1, 1)" })
    sol = operations.Dilation(5)
    sol.body = components.Block(elem1)
    assert(test == sol)

def test_reflection():
    fname = os.path.abspath("../unittests/operations/Reflection.xml")
    p = Parser(fname)
    test = p.rootelems[0]
    elem1 = et.Element("cylinder", { "height" : "5", "radius" : "2.5" })
    sol = operations.Reflection("(1, 1, 1)")
    sol.body = components.Cylinder(elem1)
    assert(test == sol)

def test_rotation():
    fname = os.path.abspath("../unittests/operations/Rotation.xml")
    p = Parser(fname)
    test = p.rootelems[0]
    elem1 = et.Element("block", { "diagonal" : "(5, 5, 5)" })
    sol = operations.Rotation(45, "(0, 0, 1)")
    sol.body = components.Block(elem1)
    assert(test == sol)

def test_translation():
    fname = os.path.abspath("../unittests/operations/Translation.xml")
    p = Parser(fname)
    test = p.rootelems[0]
    elem1 = et.Element("sphere", { "radius" : "5" })
    sol = operations.Translation("(10, 0, 0)")
    sol.body = components.Sphere(elem1)
    assert(test == sol)
