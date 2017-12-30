import xml.etree.ElementTree as ET
from .Component import Component

class Block(Component):

    def __init__(self, xml_elem):
        """
        Gets width, height, and thickness from the
        `diagonal` tag in the XML file. This tag is
        accessed with the xml.etree.ElementTree.Element
        object, xml_elem.
        """
        """diagonal = xml_elem.get("diagonal")
        diagonal = diagonal[1:-1]
        comma1 = diagonal.find(",")
        comma2 = diagonal[comma1+1:].find(",")"""
        self.x = float(xml_elem.get("thickness")) #float(diagonal[:comma1])
        self.y = float(xml_elem.get("width")) #float(diagonal[comma1+1:comma2])
        self.z = float(xml_elem.get("height")) #float(diagonal[comma2+1:])
        return 

    def __str__(self):
        """
        Returns a string containing the SCAD
        code for this block/cube object.
        """
        return "cube([{0!s}, {1!s}, {2!s}]);".format(self.x, self.y, self.z)
