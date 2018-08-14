from __future__ import absolute_import

import filecmp
import sys
import os

from SCADGen.Parser import Parser
from SCADGen import components, operations

import xml.etree.ElementTree as et

def test_parsercore():
    fname = os.path.abspath("./tests/pytest/test_xmls/parser_test.xml")
    p = Parser(fname)
    test = p.rootelems[0]
    sol = operations.Dilation(3.0)
    vector = et.Element("axis", { "beam" : "1.0", "transversal" : "0.0", "vertical" : "0.0" })
    op1 = operations.Rotation("90.*deg", vector)
    vector = et.Element("vector", { "beam" : "0.*mm", "transversal" : "0.*mm", "vertical" : "5.*cm" })
    op2 = operations.Translation(vector)
    op3 = operations.Reflection("(1, 1, 0)")
    op4 = operations.Difference()
    op5 = operations.Intersection()
    comp1 = et.Element("block", { "width" : "20.*mm", "height" : "20.*mm", "thickness" : "20.*mm" })
    comp2 = et.Element("sphere", { "radius" : "20.*mm" })
    comp3 = et.Element("pyramid", { "thickness" : "20.*mm", "width" : "20.*mm", "height" : "10.*mm" })
    op5.addComp(components.Block(comp1))
    op5.addComp(components.Sphere(comp2))
    op5.addComp(components.Pyramid(comp3))
    op6 = operations.Union()
    comp4 = et.Element("cone", { "height" : "20.*mm", "topRadius" : "10.*mm", "bottomRadius" : "20.*mm" })
    comp5 = et.Element("cylinder", { "height" : "10.*mm", "radius" : "20.*mm" })
    comp6 = et.Element("torus", {"major" : "30.*mm", "minor" : "20.*mm" })
    op6.addComp(components.Cone(comp4))
    op6.addComp(components.Cylinder(comp5))
    op6.addComp(components.Torus(comp6))
    op4.addComp(op5)
    op4.addComp(op6)
    op3.body = op4
    op2.body = op3
    op1.body = op2
    sol.body = op1
    assert(test == sol)

def test_isCompTrue():
    elem = et.Element("cylinder", {"radius" : "1.5*mm", "height" : "10.*mm" })
    fname = os.path.abspath("./tests/pytest/test_xmls/empty.xml")
    p = Parser(fname)
    assert(p.isComp(elem) == True)

def test_isCompFalse():
    elem = et.Element("difference")
    fname = os.path.abspath("./tests/pytest/test_xmls/empty.xml")
    p = Parser(fname)
    assert(p.isComp(elem) == False)

def test_isBinaryTrue():
    elem = et.Element("difference")
    fname = os.path.abspath("./tests/pytest/test_xmls/empty.xml")
    p = Parser(fname)
    assert(p.isBinary(elem) == True)

def test_isBinaryFalse():
    elem = et.Element("cylinder", {"radius" : "1.5*mm", "height" : "10.*mm" })
    fname = os.path.abspath("./tests/pytest/test_xmls/empty.xml")
    p = Parser(fname)
    assert(p.isBinary(elem) == False)

def test_isUnaryTrue():
    elem = et.Element("dilation")
    fname = os.path.abspath("./tests/pytest/test_xmls/empty.xml")
    p = Parser(fname)
    assert(p.isUnary(elem) == True)

def test_isUnaryFalse():
    elem = et.Element("cylinder", {"radius" : "1.5*mm", "height" : "10.*mm" })
    fname = os.path.abspath("./tests/pytest/test_xmls/empty.xml")
    p = Parser(fname)
    assert(p.isUnary(elem) == False)

def test_makeComp():
    elem = et.Element("cylinder", {"radius" : "1.5*mm", "height" : "10.*mm" })
    fname = os.path.abspath("./tests/pytest/test_xmls/empty.xml")
    p = Parser(fname)
    test = p.makeComp(elem)
    sol = components.Cylinder(elem)
    assert(test == sol)

def test_makeNary():
    elem = et.Element("difference")
    fname = os.path.abspath("./tests/pytest/test_xmls/empty.xml")
    p = Parser(fname)
    test = p.makeNary(elem)
    sol = operations.Difference()
    assert(test == sol)

def test_makeUnary():
    elem = et.Element("dilation")
    attrs = [et.Element("scale")]
    attrs[0].text = "5"
    fname = os.path.abspath("./tests/pytest/test_xmls/empty.xml")
    p = Parser(fname)
    test = p.makeUnary(elem, attrs)
    sol = operations.Dilation(float(5))
    assert(test == sol)

def test_generateSCAD():    
    fname = os.path.abspath("./tests/pytest/test_xmls/parser_test.xml")
    p = Parser(fname)
    p.createSCAD()
    test = os.path.abspath("./tests/pytest/test_xmls/parser_test.scad")
    sol = os.path.abspath("./tests/pytest/test_xmls/parser_sol.scad")
    assert(filecmp.cmp(test, sol) == True)

def test_unitlessParse():
    fname = os.path.abspath("./tests/pytest/test_xmls/unitless.xml")
    p = Parser(fname)
    p.createSCAD()
    test = os.path.abspath("./tests/pytest/test_xmls/unitless.scad")
    sol = os.path.abspath("./tests/pytest/test_xmls/unitless_sol.scad")
    assert(filecmp.cmp(test, sol) == True)
