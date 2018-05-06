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
        _convert = lambda x: self._convertToLength(xml_elem.get(x))
        self.major, self.minor = map(_convert, "major minor".split())
        return

    def accept(self, visit):
        from . import SCADCompVisitor, JSCompVisitor
        assert(isinstance(visit, SCADCompVisitor) or isinstance(visit, JSCompVisitor))
        return visit.visitTorus(self)

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

    def __ne__(self, rhs):
        return not (self == rhs)
