from __future__ import absolute_import

import xml.etree.ElementTree as ET
from .Component import Component

class Torus(Component):

    def __init__(self, xml_elem):
        """
        Gets the major and minor axes dimensions
        for the Torus from its line in the XML file.
        The contents of this line are acessed through
        the xml.etree.ElementTree.Element object, xml_elem.
        """
        from . import unit_parser, length_unit
        _convert = lambda x: float(unit_parser.parse(xml_elem.get(x))/length_unit)
        self.major, self.minor = map(_convert, "major minor".split())
        return

    def __str__(self):
        """
        Returns a string containing the SCAD code
        for instantiating this Torus object.
        """
        return "Torus({0!s}, {1!s});".format(self.major, self.minor)

    def __eq__(self, rhs):
        """
        Returns true if the two Torus components are equal. Returns false otherwise.
        """
        if type(self) != type(rhs):
            return False
        elif self.major != rhs.major or self.minor != rhs.minor:
            return False
        else:
            return True
