from __future__ import absolute_import

import sys
import os

from SCADGen.Parser import Parser
from SCADGen import components, operations
from SCADGen.components import SCADCompVisitor, JSCompVisitor
from SCADGen.operations import SCADOpVisitor, JSOpVisitor

import xml.etree.ElementTree as et

def test_block_str():
    elem1 = et.Element("block", { "width" : "5.*mm", "height" : "7.*mm", "thickness": "1.*mm" })
    test = components.Block(elem1)
    sol = "cube([1.0, 5.0, 7.0], center=true);"
    assert(test.accept(SCADCompVisitor()) == sol)

def test_cone_str():
    elem1 = et.Element("cone", { "height" : "5.*mm", "topRadius" : "2.*mm", "bottomRadius" : "4.*mm" })
    test = components.Cone(elem1)
    sol = "cylinder(h = 5.0, r1 = 4.0, r2 = 2.0, $fn=100, center=true);"
    assert(test.accept(SCADCompVisitor()) == sol)

def test_cylinder_str():
    elem1 = et.Element("cylinder", { "height" : "5.*mm", "radius" : "2.5*mm" })
    test = components.Cylinder(elem1)
    sol = "cylinder(h = 5.0, r = 2.5, $fn=100, center=true);"
    assert(test.accept(SCADCompVisitor()) == sol)

def test_pyramid_str():
    elem1 = et.Element("pyramid", { "thickness" : "5.*mm", "width" : "5.*mm", "height" : "10.*mm" })
    test = components.Pyramid(elem1)
    sol = """polyhedron(
    points=[ [2.5,2.5,-10.0], [2.5,-2.5,-10.0],
             [-2.5,-2.5,-10.0], [-2.5,2.5,-10.0], [0,0,0] ],
    faces=[ [0,1,4], [1,2,4], [2,3,4], [3,0,4], [1,0,3], [2,1,3] ]
);"""
    assert(test.accept(SCADCompVisitor()) == sol)

def test_sphere_str():
    elem1 = et.Element("sphere", { "radius" : "2.5*mm" })
    test = components.Sphere(elem1)
    sol = "sphere(r = 2.5, $fn=100);"
    assert(test.accept(SCADCompVisitor()) == sol)

def test_torus_str():
    elem1 = et.Element("torus", { "major" : "10.*mm", "minor" : "5.*mm"})
    test = components.Torus(elem1)
    sol = "Torus(10.0, 5.0);"
    assert(test.accept(SCADCompVisitor()) == sol)

def test_difference_str():
    elem1 = et.Element("cylinder", { "radius" : "2.5*mm", "height" : "5.*mm" })
    elem2 = et.Element("cone", { "bottomRadius" : "2.5*mm", "topRadius" : "0.*mm", "height" : "5.*mm" })
    comp1 = components.Cylinder(elem1)
    comp2 = components.Cone(elem2)
    test = operations.Difference()
    test.addComp(comp1)
    test.addComp(comp2)
    sol = """difference() {
    cylinder(h = 5.0, r = 2.5, $fn=100, center=true);
    cylinder(h = 5.0, r1 = 2.5, r2 = 0.0, $fn=100, center=true);
}"""
    assert(test.accept(SCADOpVisitor()) == sol)

def test_dilation_str():
    elem = et.Element("block", { "width" : "1.*mm", "height" : "1.*mm", "thickness": "1.*mm" })
    test = operations.Dilation(5)
    test.body = components.Block(elem)
    sol = """scale([5, 5, 5]) {
    cube([1.0, 1.0, 1.0], center=true);
}"""
    assert(test.accept(SCADOpVisitor()) == sol)

def test_intersection_str():
    elem1 = et.Element("sphere", { "radius" : "5.*mm" })
    elem2 = et.Element("block", { "width" : "5.*mm", "height" : "1.*mm", "thickness": "5.*mm" })
    test = operations.Intersection()
    test.addComp(components.Sphere(elem1))
    test.addComp(components.Block(elem2))
    sol = """intersection() {
    sphere(r = 5.0, $fn=100);
    cube([5.0, 5.0, 1.0], center=true);
}"""
    assert(test.accept(SCADOpVisitor()) == sol)

def test_reflection_str():
    elem = et.Element("cylinder", { "height" : "5.*mm", "radius" : "2.5*mm" })
    test = operations.Reflection("(1, 1, 1)")
    test.body = components.Cylinder(elem)
    sol = """mirror([1.0, 1.0, 1.0]) {
    cylinder(h = 5.0, r = 2.5, $fn=100, center=true);
}"""
    assert(test.accept(SCADOpVisitor()) == sol)

def test_rotation_str():
    elem = et.Element("block", { "width" : "5.*mm", "height" : "5.*mm", "thickness": "5.*mm" })
    vector = et.Element("axis", { "beam" : "0.0", "transversal" : "0.0", "vertical" : "1.0" })
    test = operations.Rotation("45.*deg", vector)
    test.body = components.Block(elem)
    sol = """rotate(45.0, [0.0, 0.0, 1.0]) {
    cube([5.0, 5.0, 5.0], center=true);
}"""
    assert(test.accept(SCADOpVisitor()) == sol)

def test_translation_str():
    elem = et.Element("sphere", { "radius" : "5.*mm" })
    vector = et.Element("vector", { "beam" : "10.*mm", "transversal" : "0.*mm", "vertical" : "0.*mm" })
    test = operations.Translation(vector)
    test.body = components.Sphere(elem)
    sol = """translate([10.0, 0.0, 0.0]) {
    sphere(r = 5.0, $fn=100);
}"""
    assert(test.accept(SCADOpVisitor()) == sol)

def test_union_str():
    elem1 = et.Element("sphere", { "radius" : "2.5*mm" })
    elem2 = et.Element("cylinder", { "height" : "5.*mm", "radius" : "1.*mm" })
    test = operations.Union()
    test.addComp(components.Sphere(elem1))
    test.addComp(components.Cylinder(elem2))
    sol = """union() {
    sphere(r = 2.5, $fn=100);
    cylinder(h = 5.0, r = 1.0, $fn=100, center=true);
}"""
    assert(test.accept(SCADOpVisitor()) == sol)
