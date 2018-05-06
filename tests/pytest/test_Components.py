from __future__ import absolute_import

import sys
import os

from SCADGen.Parser import Parser

import xml.etree.ElementTree as et

def test_block():
    fname = os.path.abspath("./tests/unittests/components/Block.xml")
    p = Parser(fname)
    test = p.rootelems[0]
    sol = [1., 50., 70.]
    assert(test.x == sol[0] and test.y == sol[1] and test.z == sol[2])

def test_cone():
    fname = os.path.abspath("./tests/unittests/components/Cone_diff_radii.xml")
    p = Parser(fname)
    test = p.rootelems[0]
    sol = [5, 2, 4]
    assert(test.bottom_radius == sol[2] and test.top_radius == sol[1] and test.height == sol[0])

def test_cylinder():
    fname = os.path.abspath("./tests/unittests/components/Cylinder.xml")
    p = Parser(fname)
    test = p.rootelems[0]
    sol = [50, 25]
    assert(test.radius == sol[1] and test.height == sol[0])

def test_pyramid():
    fname = os.path.abspath("./tests/unittests/components/Pyramid.xml")
    p = Parser(fname)
    test = p.rootelems[0]
    sol = [50, 50, 100]
    assert(test.x == sol[0] and test.y == sol[1] and test.z == sol[2])

def test_sphere():
    fname = os.path.abspath("./tests/unittests/components/Sphere.xml")
    p = Parser(fname)
    test = p.rootelems[0]
    assert(test.radius == 25)

def test_torus():
    fname = os.path.abspath("./tests/unittests/components/Torus.xml")
    p = Parser(fname)
    test = p.rootelems[0]
    sol = [100, 50]
    assert(test.major == sol[0] and test.minor == sol[1])
