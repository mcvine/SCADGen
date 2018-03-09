from __future__ import absolute_import

import xml.etree.ElementTree as ET
from Component import Component

class Pyramid(Component):

    def __init__(self, xml_elem):
        self.edgeX = float(xml_elem.get("edgeX"))
        self.edgeY = float(xml_elem.get("edgeY"))
        self.height = float(xml_elem.get("height"))
        return;

    def __str__(self):
        return """polyhedron(
    points=[ [{0!s},{1!s},-{2!s}], [{0!s},-{1!s},{-2!s}],
             [-{0!s},-{1!s},-{2!s}], [-{0!s},{1!s},-{2!s}], [0,0,0] ],
    faces=[ [0,1,4], [1,2,4], [2,3,4], [3,0,4], [1,0,3], [2,1,3] ]
);""".format((self.edgeX/2), (self.edgeY/2), self.height)
