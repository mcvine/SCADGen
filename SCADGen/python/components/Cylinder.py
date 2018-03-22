from __future__ import absolute_import

import xml.etree.ElementTree as ET
from .Component import Component

class Cylinder(Component):

    def __init__(self, xml_elem):
        """
        Gets radius and height for the cylinder from
        the atrributes from its XML line. These attributes are
        accessed using the xml.etree.ElementTree.Element object, xml_elem.
        """
        from . import unit_parser, length_unit
        _convert = lambda x: unit_parser.parse(xml_elem.get(x))/length_unit
        self.radius, self.height = map(_convert, "radius height".split())
        return

    def __str__(self):
        """
        Returns a string containing the SCAD
        code for this cylinder object.
        """
        return "cylinder(h = {0!s}, r = {1!s}, $fn=100);".format(self.height, self.radius)

    def __eq__(self, rhs):
        """
        Returns true if the two Cylinder components are equal. Returns false otherwise.
        """
        if type(self) != type(rhs):
            return False
        elif self.radius != rhs.radius or self.height != rhs.height:
            return False
        else:
            return True
