from __future__ import absolute_import

import xml.etree.ElementTree as ET
from Component import Component

class Pyramid(Component):

    def __init__(self, xml_elem):
        """
        Gets the base dimensions and height for the cone
        from the attributes from its XML line. These attributes
        are accessed with the xml.etree.ElementTree object,
        xml_elem. This will likely need to be changed later
        once the "formal" xml format is added to pyre.
        """
        self.edgeX = float(xml_elem.get("edgeX"))
        self.edgeY = float(xml_elem.get("edgeY"))
        self.height = float(xml_elem.get("height"))
        return;

    def __str__(self):
        """
        Returns a string containing the SCAD code for this
        Cone object.
        """
        return """polyhedron(
    points=[ [{0!s},{1!s},-{2!s}], [{0!s},-{1!s},{-2!s}],
             [-{0!s},-{1!s},-{2!s}], [-{0!s},{1!s},-{2!s}], [0,0,0] ],
    faces=[ [0,1,4], [1,2,4], [2,3,4], [3,0,4], [1,0,3], [2,1,3] ]
);""".format((self.edgeX/2), (self.edgeY/2), self.height)
