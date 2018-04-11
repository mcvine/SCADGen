from __future__ import absolute_import

import sys
import os

sys.path.append(os.path.abspath("../../SCADGen/python"))
from Parser import Parser
import components
import operations

import xml.etree.ElementTree as et

def test_dilation_scale():
    elem1 = et.Element("block", { "width" : "1.*mm", "height" : "1.*mm", "thickness": "1.*mm" })
    op = operations.Dilation(5)
    op.body = components.Block(elem1)
    assert(op.scale == 5)

def test_dilation_body():
    elem1 = et.Element("block", { "width" : "1.*mm", "height" : "1.*mm", "thickness": "1.*mm" })
    op = operations.Dilation(5)
    op.body = components.Block(elem1)
    assert(op.body.x == 1.0 and op.body.y == 1.0 and op.body.z == 1.0)

def test_reflection_vector():
    elem1 = et.Element("cylinder", { "height" : "5.*mm", "radius" : "2.5*mm" })
    op = operations.Reflection("(1, 1, 1)")
    op.body = components.Cylinder(elem1)
    assert(op.vector == [1, 1, 1])

def test_reflection_body():
    elem1 = et.Element("cylinder", { "height" : "5.*mm", "radius" : "2.5*mm" })
    op = operations.Reflection("(1, 1, 1)")
    op.body = components.Cylinder(elem1)
    assert(op.body.height == 5.0 and op.body.radius == 2.5)

def test_rotation_angle():
    elem1 = et.Element("block", { "width" : "5.*mm", "height" : "5.*mm", "thickness": "5.*mm" })
    vector = et.Element("axis", { "beam" : "0.0", "transversal" : "0.0", "vertical" : "1.0" })
    op = operations.Rotation("45.*deg", vector)
    op.body = components.Block(elem1)
    assert(op.angle == 45.0)

def test_rotation_vector():
    elem1 = et.Element("block", { "width" : "1.*mm", "height" : "1.*mm", "thickness": "1.*mm" })
    vector = et.Element("axis", { "beam" : "0.0", "transversal" : "0.0", "vertical" : "1.0" })
    op = operations.Rotation("45.*deg", vector)
    op.body = components.Block(elem1)
    assert(op.vector == [0.0, 0.0, 1.0])

def test_rotation_body():
    elem1 = et.Element("block", { "width" : "5.*mm", "height" : "5.*mm", "thickness": "5.*mm" })
    vector = et.Element("axis", { "beam" : "0.0", "transversal" : "0.0", "vertical" : "1.0" })
    op = operations.Rotation("45.*deg", vector)
    op.body = components.Block(elem1)
    assert(op.body.x == 5.0 and op.body.y == 5.0 and op.body.z == 5.0)

def test_translation_vector():
    elem1 = et.Element("sphere", { "radius" : "5.*mm" })
    vector = et.Element("vector", { "beam" : "10.*mm", "transversal" : "0.*mm", "vertical" : "0.*mm" })
    op = operations.Translation(vector)
    op.body = components.Sphere(elem1)
    assert(op.vector == [10.0, 0.0, 0.0])

def test_translation_body():
    elem1 = et.Element("sphere", { "radius" : "5.*mm" })
    vector = et.Element("vector", { "beam" : "10.*mm", "transversal" : "0.*mm", "vertical" : "0.*mm" })
    op = operations.Translation(vector)
    op.body = components.Sphere(elem1)
    assert(op.body.radius == 5.0)
