from __future__ import absolute_import

import sys
import os

from SCADGen.Parser import Parser
from SCADGen import components, operations

import xml.etree.ElementTree as et

def test_difference_Comp1Height():
    elem1 = et.Element("cylinder", { "height" : "5.*mm", "radius" : "2.5*mm" })
    elem2 = et.Element("cone", { "height" : "5.*mm", "radius" : "2.5*mm" })
    op = operations.Difference()
    op.addComp(components.Cylinder(elem1))
    op.addComp(components.Cone(elem2))
    assert(op[0].height == 5)

def test_difference_Comp1Radius():
    elem1 = et.Element("cylinder", { "height" : "5.*mm", "radius" : "2.5*mm" })
    elem2 = et.Element("cone", { "height" : "5.*mm", "radius" : "2.5*mm" })
    op = operations.Difference()
    op.addComp(components.Cylinder(elem1))
    op.addComp(components.Cone(elem2))
    assert(op[0].radius == 2.5)

def test_difference_Comp2Height():
    elem1 = et.Element("cylinder", { "height" : "5.*mm", "radius" : "2.5*mm" })
    elem2 = et.Element("cone", { "height" : "5.*mm", "radius" : "2.5*mm" })
    op = operations.Difference()
    op.addComp(components.Cylinder(elem1))
    op.addComp(components.Cone(elem2))
    assert(op[1].height == 5)

def test_difference_Comp2Top():
    elem1 = et.Element("cylinder", { "height" : "5.*mm", "radius" : "2.5*mm" })
    elem2 = et.Element("cone", { "height" : "5.*mm", "radius" : "2.5*mm" })
    op = operations.Difference()
    op.addComp(components.Cylinder(elem1))
    op.addComp(components.Cone(elem2))
    assert(op[1].radius == 2.5)

def test_intersection_Comp1Radius():
    elem1 = et.Element("sphere", { "radius" : "5.*mm" })
    elem2 = et.Element("block", { "width" : "5.*mm", "height" : "7.*mm", "thickness": "1.*mm" })
    op = operations.Intersection()
    op.addComp(components.Sphere(elem1))
    op.addComp(components.Block(elem2))
    assert(op[0].radius == 5)

def test_intersection_Comp2Diag():
    elem1 = et.Element("sphere", { "radius" : "5.*mm" })
    elem2 = et.Element("block", { "width" : "5.*mm", "height" : "1.*mm", "thickness": "5.*mm" })
    op = operations.Intersection()
    op.addComp(components.Sphere(elem1))
    op.addComp(components.Block(elem2))
    assert(op[1].x == 5 and op[1].y == 5 and op[1].z == 1)

def test_union_Comp1Radius():
    elem1 = et.Element("sphere", { "radius" : "2.5*mm" })
    elem2 = et.Element("cylinder", { "height" : "5.*mm", "radius" : "1.*mm" })
    op = operations.Union()
    op.addComp(components.Sphere(elem1))
    op.addComp(components.Cylinder(elem2))
    assert(op[0].radius == 2.5)

def test_union_Comp2Height():
    elem1 = et.Element("sphere", { "radius" : "2.5*mm" })
    elem2 = et.Element("cylinder", { "height" : "5.*mm", "radius" : "1.*mm" })
    op = operations.Union()
    op.addComp(components.Sphere(elem1))
    op.addComp(components.Cylinder(elem2))
    assert(op[1].height == 5)

def test_union_Comp2Radius():
    elem1 = et.Element("sphere", { "radius" : "2.5*mm" })
    elem2 = et.Element("cylinder", { "height" : "5.*mm", "radius" : "1.*mm" })
    op = operations.Union()
    op.addComp(components.Sphere(elem1))
    op.addComp(components.Cylinder(elem2))
    assert(op[1].radius == 1)
