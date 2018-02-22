from __future__ import absolute_import

import sys
import os
sys.path.append(os.path.abspath("../../SCADGen/python"))

import xml.etree.ElementTree as et
import components
import operations

def test_blockstr():
    elem1 = et.Element("block", { "diagonal" : "(5, 5, 5)" })
    test = components.Block(elem1)
    sol = "cube([5, 5, 5]);"
    assert("{0!s}".format(test) == sol)

def test_conestr():
    elem1 = et.Element("cone", { "height" : "5", "topRadius" : "2", "bottomRadius" : "4" })
    test = components.Cone(elem1)
    sol = "cylinder(h = 5, r1 = 4, r1 = 2, $fn=100);"
    assert("{0!s}".format(test) == sol)

def test_cylinderstr():
    elem1 = et.Element("cylinder", { "height" : "5", "radius" : "2.5" })
    test = components.Cylinder(elem1)
    sol = "cylinder(h = 5, r = 2.5, $fn=100);"
    assert("{0!s}".format(test) == sol)

def test_spherestr():
    elem1 = et.Element("sphere", { "radius" : "2.5" })
    test = components.Sphere(elem1)
    sol = "sphere(r = 2.5, $fn=100);"
    assert("{0!s}".format(test) == sol)

def test_torusstr():
    elem1 = et.Element("torus", { "major" : "10", "minor" : "5"})
    test = components.Torus(elem1)
    sol = "Torus(10, 5);"
    assert("{0!s}".format(test) == sol)

def test_differencestr():
    elem1 = et.Element("cylinder", { "radius" : "2.5", "height" : "5" })
    elem2 = et.Element("cone", { "bottomRadius" : "2.5", "topRadius" : "0", "height" : "5" })
    comp1 = components.Cylinder(elem1)
    comp2 = components.Cone(elem2)
    test = operations.Difference()
    test.comp1 = comp1
    test.comp2 = comp2
    sol = """difference() {{
    cylinder(h = 5, r = 2.5, $fn=100);
    cylinder(h = 5, r1 = 2.5, r2 = 0, $fn=100);
}}"""
    assert("{0!s}".format(test) == sol)
