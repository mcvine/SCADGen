from __future__ import absolute_import

import sys
import os
sys.path.append(os.path.abspath("../../SCADGen/python"))

import xml.etree.ElementTree as et
from Parser import Parser
import components
import operations

def test_block()
    fname = os.path.abspath("../unittests/components/Block.xml")
    p = Parser(fname)
    test = p.rootelems[0]
    elem1 = et.Element("block", { "diagonal" : "(5, 5, 5)" })
    sol = components.Block(elem1)
    assert(test == sol)

def test_cone()
    fname = os.path.abspath("../unittests/components/Cone_diff_radii.xml")
    p = Parser(fname)
    test = p.rootelems[0]
    elem1 = et.Element("cone", { "height" : "5", "topRadius" : "2", "bottomRadius" : "4" })
    sol = components.Block(elem1)
    assert(test == sol)

def test_cylinder()
    fname = os.path.abspath("../unittests/components/Cylinder.xml")
    p = Parser(fname)
    test = p.rootelems[0]
    elem1 = et.Element("cylinder", { "height" : "5", "radius" : "2.5" })
    sol = components.Block(elem1)
    assert(test == sol)

def test_sphere()
    fname = os.path.abspath("../unittests/components/Sphere.xml")
    p = Parser(fname)
    test = p.rootelems[0]
    elem1 = et.Element("sphere", { "radius" : "2.5" })
    sol = components.Block(elem1)
    assert(test == sol)

def test_torus()
    fname = os.path.abspath("../unittests/components/Torus.xml")
    p = Parser(fname)
    test = p.rootelems[0]
    elem1 = et.Element("torus", { "major" : "10", "minor" : "5" })
    sol = components.Block(elem1)
    assert(test == sol)
