import xml.etree.ElementTree as ET
from .Component import Component

class Sphere(Component):

    def __init__(self, xml_elem):
        """
        Gets the radius for the sphere from
        its line in the XML file (xml line).
        The contents of this line are acessed with
        the xml.etree.ElementTree.Element object, xml_elem.
        """
        self.radius = xml_elem.get("radius")
        return 

    def __str__(self):
        """
        Returns a string containing the SCAD
        code for this sphere objec.
        """
        return "sphere(r = {0!s}, $fn=100);".format(self.radius)
