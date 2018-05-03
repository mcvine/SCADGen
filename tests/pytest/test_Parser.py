from __future__ import absolute_import

import filecmp
import sys
import os

from SCADGen.Parser import Parser
from SCADGen import components, operations

import xml.etree.ElementTree as et

def test_parsercore():
    fname = os.path.abspath("./tests/pytest/test_xmls/parser_test.xml")
    elem1 = et.Element("cylinder", { "radius" : "1.5*mm", "height" : "10.*mm" })
    elem2 = et.Element("cylinder", { "radius" : "2.5*mm", "height" : "5.*mm" })
    comp1 = components.Cylinder(elem1)
    comp2 = components.Cylinder(elem2)
    vector = et.Element("vector", { "beam" : "0.*m", "transversal" : "0.*m", "vertical" : "-2.5*mm" })
    op = operations.Translation(vector)
    op.body = comp1
    sol = operations.Union()
    sol.addComp(comp2)
    sol.addComp(op)
    p = Parser(fname)
    test = p.rootelems[0]
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
