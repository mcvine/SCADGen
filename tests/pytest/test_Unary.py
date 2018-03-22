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
    assert(op.body.x == 1 and op.body.y == 1 and op.body.z == 1)

def test_reflection_vector():
    elem1 = et.Element("cylinder", { "height" : "5", "radius" : "2.5" })
    op = operations.Reflection("(1, 1, 1)")
    op.body = components.Cylinder(elem1)
    assert(op.vector == [1, 1, 1])

def test_reflection_body():
    elem1 = et.Element("cylinder", { "height" : "5", "radius" : "2.5" })
    op = operations.Reflection("(1, 1, 1)")
    op.body = components.Cylinder(elem1)
    assert(op.body.height == 5 and op.body.radius == 2.5)

def test_rotation_angle():
    elem1 = et.Element("block", { "width" : "5.*mm", "height" : "5.*mm", "thickness": "5.*mm" })
    op = operations.Rotation(45, "(0, 0, 1)")
    op.body = components.Block(elem1)
    assert(op.angle == 45)

def test_rotation_vector():
    elem1 = et.Element("block", { "width" : "1.*mm", "height" : "1.*mm", "thickness": "1.*mm" })
    op = operations.Rotation(45, "(0, 0, 1)")
    op.body = components.Block(elem1)
    assert(op.vector == [0, 0, 1])

def test_rotation_body():
    elem1 = et.Element("block", { "width" : "5.*mm", "height" : "5.*mm", "thickness": "5.*mm" })
    op = operations.Rotation(45, "(0, 0, 1)")
    op.body = components.Block(elem1)
    assert(op.body.x == 5 and op.body.y == 5 and op.body.z == 5)

def test_translation_vector():
    elem1 = et.Element("sphere", { "radius" : "5" })
    op = operations.Translation("(10, 0, 0)")
    op.body = components.Sphere(elem1)
    assert(op.vector == [10, 0, 0])

def test_translation_body():
    elem1 = et.Element("sphere", { "radius" : "5" })
    op = operations.Translation("(10, 0, 0)")
    op.body = components.Sphere(elem1)
    assert(op.body.radius == 5)
