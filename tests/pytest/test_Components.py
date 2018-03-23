from __future__ import absolute_import

import sys
import os

sys.path.append(os.path.abspath("../../SCADGen/python"))
from Parser import Parser
import components
import operations

import xml.etree.ElementTree as et

def test_block():
    fname = os.path.abspath("../unittests/components/Block.xml")
    p = Parser(fname)
    test = p.rootelems[0]
    sol = [1., 50., 70.]
    assert(test.x == sol[0] and test.y == sol[1] and test.z == sol[2])

def test_cone():
    fname = os.path.abspath("../unittests/components/Cone_diff_radii.xml")
    p = Parser(fname)
    test = p.rootelems[0]
    sol = [5, 2, 4]
    assert(test.bottom_radius == sol[2] and test.top_radius == sol[1] and test.height == sol[0])

def test_cylinder():
    fname = os.path.abspath("../unittests/components/Cylinder.xml")
    p = Parser(fname)
    test = p.rootelems[0]
    sol = [5, 2.5]
    assert(test.radius == sol[1] and test.height == sol[0])

def test_pyramid():
    fname = os.path.abspath("../unittests/components/Pyramid.xml")
    p = Parser(fname)
    test = p.rootelems[0]
    sol = [5, 5, 10]
    assert(test.edgeX == sol[0] and test.edgeY == sol[1] and test.height == sol[2])

def test_sphere():
    fname = os.path.abspath("../unittests/components/Sphere.xml")
    p = Parser(fname)
    test = p.rootelems[0]
    assert(test.radius == 2.5)

def test_torus():
    fname = os.path.abspath("../unittests/components/Torus.xml")
    p = Parser(fname)
    test = p.rootelems[0]
    sol = [10, 5]
    assert(test.major == sol[0] and test.minor == sol[1])
