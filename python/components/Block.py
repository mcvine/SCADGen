import xml.etree.ElementTree as ET

class Block:

    def __init__(self, xml_elem):
        """
        Gets width, height, and thickness from the
        `diagonal` tag in the XML file. This tag is
        accessed with the xml.etree.ElementTree.Element
        object, xml_elem.
        """
        diagonal = xml_elem.get("diagonal")
        self.x = diagonal[0]
        self.y = diagonal[1]
        self.z = diagonal[2]
        return 

    def __str__(self):
        """
        Returns a string containing the SCAD
        code for this block/cube object.
        """
        return "cube([{0!s}, {1!s}, {2!s}]);".format(self.x, self.y, self.z)
