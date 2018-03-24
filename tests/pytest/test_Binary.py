from __future__ import absolute_import

import sys
import os

sys.path.append(os.path.abspath("../../SCADGen/python"))
from Parser import Parser
import components
import operations

import xml.etree.ElementTree as et

def test_difference_Comp1Height():
    elem1 = et.Element("cylinder", { "height" : "5.*mm", "radius" : "2.5*mm" })
    elem2 = et.Element("cone", { "height" : "5.*mm", "topRadius" : "0.*mm", "bottomRadius" : "2.5*mm" })
    op = operations.Difference()
    op.comp1 = components.Cylinder(elem1)
    op.comp2 = components.Cone(elem2)
    assert(op.comp1.height == 5)

def test_difference_Comp1Radius():
    elem1 = et.Element("cylinder", { "height" : "5.*mm", "radius" : "2.5*mm" })
    elem2 = et.Element("cone", { "height" : "5.*mm", "topRadius" : "0.*mm", "bottomRadius" : "2.5*mm" })
    op = operations.Difference()
    op.comp1 = components.Cylinder(elem1)
    op.comp2 = components.Cone(elem2)
    assert(op.comp1.radius == 2.5)

def test_difference_Comp2Height():
    elem1 = et.Element("cylinder", { "height" : "5.*mm", "radius" : "2.5*mm" })
    elem2 = et.Element("cone", { "height" : "5.*mm", "topRadius" : "0.*mm", "bottomRadius" : "2.5*mm" })
    op = operations.Difference()
    op.comp1 = components.Cylinder(elem1)
    op.comp2 = components.Cone(elem2)
    assert(op.comp2.height == 5)

def test_difference_Comp2Top():
    elem1 = et.Element("cylinder", { "height" : "5.*mm", "radius" : "2.5*mm" })
    elem2 = et.Element("cone", { "height" : "5.*mm", "topRadius" : "0.*mm", "bottomRadius" : "2.5*mm" })
    op = operations.Difference()
    op.comp1 = components.Cylinder(elem1)
    op.comp2 = components.Cone(elem2)
    assert(op.comp2.top_radius == 0)

def test_difference_Comp2Bottom():
    elem1 = et.Element("cylinder", { "height" : "5.*mm", "radius" : "2.5*mm" })
    elem2 = et.Element("cone", { "height" : "5.*mm", "topRadius" : "0.*mm", "bottomRadius" : "2.5*mm" })
    op = operations.Difference()
    op.comp1 = components.Cylinder(elem1)
    op.comp2 = components.Cone(elem2)
    assert(op.comp2.bottom_radius == 2.5)

def test_intersection_Comp1Radius():
    elem1 = et.Element("sphere", { "radius" : "5.*mm" })
    elem2 = et.Element("block", { "width" : "5.*mm", "height" : "7.*mm", "thickness": "1.*mm" })
    op = operations.Intersection()
    op.comp1 = components.Sphere(elem1)
    op.comp2 = components.Block(elem2)
    assert(op.comp1.radius == 5)

def test_intersection_Comp2Diag():
    elem1 = et.Element("sphere", { "radius" : "5.*mm" })
    elem2 = et.Element("block", { "width" : "5.*mm", "height" : "1.*mm", "thickness": "5.*mm" })
    op = operations.Intersection()
    op.comp1 = components.Sphere(elem1)
    op.comp2 = components.Block(elem2)
    assert(op.comp2.x == 5 and op.comp2.y == 5 and op.comp2.z == 1)

def test_union_Comp1Radius():
    elem1 = et.Element("sphere", { "radius" : "2.5*mm" })
    elem2 = et.Element("cylinder", { "height" : "5.*mm", "radius" : "1.*mm" })
    op = operations.Union()
    op.comp1 = components.Sphere(elem1)
    op.comp2 = components.Cylinder(elem2)
    assert(op.comp1.radius == 2.5)

def test_union_Comp2Height():
    elem1 = et.Element("sphere", { "radius" : "2.5*mm" })
    elem2 = et.Element("cylinder", { "height" : "5.*mm", "radius" : "1.*mm" })
    op = operations.Union()
    op.comp1 = components.Sphere(elem1)
    op.comp2 = components.Cylinder(elem2)
    assert(op.comp2.height == 5)

def test_union_Comp2Radius():
    elem1 = et.Element("sphere", { "radius" : "2.5*mm" })
    elem2 = et.Element("cylinder", { "height" : "5.*mm", "radius" : "1.*mm" })
    op = operations.Union()
    op.comp1 = components.Sphere(elem1)
    op.comp2 = components.Cylinder(elem2)
    assert(op.comp2.radius == 1)
