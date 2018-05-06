from __future__ import absolute_import

import xml.etree.ElementTree as ET
from .Component import Component

class Pyramid(Component):

    def __init__(self, xml_elem):
        """
        Gets the base dimensions and height for the cone
        from the attributes from its XML line. These attributes
        are accessed with the xml.etree.ElementTree object,
        xml_elem. This will likely need to be changed later
        once the "formal" xml format is added to pyre.
        """
        _convert = lambda x: self._convertToLength(xml_elem.get(x))
        self.x, self.y, self.z = map(_convert, "thickness width height".split())
        return;

    def accept(self, visit):
        from . import SCADCompVisitor, JSCompVisitor
        assert(isinstance(visit, SCADCompVisitor) or isinstance(visit, JSCompVisitor))
        return visit.visitPyramid(self)

    def __eq__(self, rhs):
        """
        Returns true if the two Pyramids are equal. Returns false otherwise.
        """
        if type(self) != type(rhs):
            return False
        elif self.x != rhs.x or self.y != rhs.y or self.z != rhs.z:
            return False
        else:
            return True

    def __ne__(self, rhs):
        return not (self == rhs)
