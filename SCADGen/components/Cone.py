from __future__ import absolute_import

import xml.etree.ElementTree as ET
from .Component import Component

class Cone(Component):

    def __init__(self, xml_elem):
        """
        Gets bottom/top radius and height for the cone
        from the attributes from its XML line. These attributes
        are accessed with the xml.etree.ElementTree.Element
        object, xml_elem.
        """
        def _convert(x):
            value = xml_elem.get(x)
            if value is None:
                raise RuntimeError("was not able to get %s from %s" % (x, xml_elem))
            return self._convertToLength(value)
        self.radius, self.height = map(_convert, "radius height".split())
        # return

    def __str__(self):
        """
        Returns a string containing the SCAD
        code for this Cone object.
        """
        return "translate([0.0, 0.0, -{0!s}]) {{cylinder(h = {1!s},  r1 = {2!s}, r2=0,  $fn=100, center=true);}}".format(
            self.height/2, self.height,  self.radius)

    def __eq__(self, rhs):
        """
        Returns true if the two Cone components are equal. Returns false otherwise.
        """
        if type(self) != type(rhs):
            return False
        elif self.radius != rhs.radius or self.height != rhs.height:
            return False
        else:
            return True

    def __ne__(self, rhs):
        return not (self == rhs)
