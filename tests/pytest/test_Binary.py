from __future__ import absolute_import

import sys
import os
sys.path.append(os.path.abspath("../../SCADGen/python"))

import xml.etree.ElementTree as et
from Parser import Parser
import components
import operations

def test_difference_Comp1Height():
    elem1 = et.Element("cylinder", { "height" : "5", "radius" : "2.5" })
    elem2 = et.Element("cone", { "height" : "5", "topRadius" : "0", "bottomRadius" : "2.5" })
    op = operations.Difference()
    op.comp1 = components.Cylinder(elem1)
    op.comp2 = components.Cone(elem2)
    assert(op.comp1.height == 5)

def test_difference_Comp1Radius():
    elem1 = et.Element("cylinder", { "height" : "5", "radius" : "2.5" })
    elem2 = et.Element("cone", { "height" : "5", "topRadius" : "0", "bottomRadius" : "2.5" })
    op = operations.Difference()
    op.comp1 = components.Cylinder(elem1)
    op.comp2 = components.Cone(elem2)
    assert(op.comp1.radius == 2.5)

def test_difference_Comp2Height():
    elem1 = et.Element("cylinder", { "height" : "5", "radius" : "2.5" })
    elem2 = et.Element("cone", { "height" : "5", "topRadius" : "0", "bottomRadius" : "2.5" })
    op = operations.Difference()
    op.comp1 = components.Cylinder(elem1)
    op.comp2 = components.Cone(elem2)
    assert(op.comp2.height == 5)

def test_difference_Comp2Top():
    elem1 = et.Element("cylinder", { "height" : "5", "radius" : "2.5" })
    elem2 = et.Element("cone", { "height" : "5", "topRadius" : "0", "bottomRadius" : "2.5" })
    op = operations.Difference()
    op.comp1 = components.Cylinder(elem1)
    op.comp2 = components.Cone(elem2)
    assert(op.comp2.top_radius == 0)

def test_difference_Comp2Bottom():
    elem1 = et.Element("cylinder", { "height" : "5", "radius" : "2.5" })
    elem2 = et.Element("cone", { "height" : "5", "topRadius" : "0", "bottomRadius" : "2.5" })
    op = operations.Difference()
    op.comp1 = components.Cylinder(elem1)
    op.comp2 = components.Cone(elem2)
    assert(op.comp2.bottom_radius == 2.5)

def test_intersection_Comp1Radius():
    elem1 = et.Element("sphere", { "radius" : "5" })
    elem2 = et.Element("block", { "diagonal" : "(5, 5, 1)" })
    op = operations.Intersection()
    op.comp1 = components.Sphere(elem1)
    op.comp2 = components.Block(elem2)
    assert(op.comp1.radius == 5)

def test_intersection_Comp2Diag():
    elem1 = et.Element("sphere", { "radius" : "5" })
    elem2 = et.Element("block", { "diagonal" : "(5, 5, 1)" })
    op = operations.Intersection()
    op.comp1 = components.Sphere(elem1)
    op.comp2 = components.Block(elem2)
    assert(op.comp2.x == 5 and op.comp2.y == 5 and op.comp2.z == 1)

def test_union_Comp1Radius():
    elem1 = et.Element("sphere", { "radius" : "2.5" })
    elem2 = et.Element("cylinder", { "height" : "5", "radius" : "1" })
    op = operations.Union()
    op.comp1 = components.Sphere(elem1)
    op.comp2 = components.Cylinder(elem2)
    assert(op.comp1.radius == 2.5)

def test_union_Comp2Height():
    elem1 = et.Element("sphere", { "radius" : "2.5" })
    elem2 = et.Element("cylinder", { "height" : "5", "radius" : "1" })
    op = operations.Union()
    op.comp1 = components.Sphere(elem1)
    op.comp2 = components.Cylinder(elem2)
    assert(op.comp2.height == 5)

def test_union_Comp2Radius():
    elem1 = et.Element("sphere", { "radius" : "2.5" })
    elem2 = et.Element("cylinder", { "height" : "5", "radius" : "1" })
    op = operations.Union()
    op.comp1 = components.Sphere(elem1)
    op.comp2 = components.Cylinder(elem2)
    assert(op.comp2.radius == 1)
