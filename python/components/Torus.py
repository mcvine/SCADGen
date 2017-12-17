import xml.etree.ElementTree as ET

class Torus:

    def __init__(self, xml_elem):
        """
        Gets the major and minor axes dimensions
        for the Torus from its line in the XML file.
        The contents of this line are acessed through
        the xml.etree.ElementTree.Element object, xml_elem.
        """
        self.major = xml_elem.get("major") 
        self.minor = xml_elem.get("minor")

    def strTorusModule(self):
        """
        Returns a string containing the OpenSCAD
        code for the Torus module. This will be
        added to the beginning of the OpenSCAD file
        by the driver code.
        """
        return """module Torus(rx, ry) {
                      resize([rx, ry, 10])
                      rotate_extrude(convexity = 10)
                      translate([2, 0, 0])
                      circle(r = 1, $fn = 100);
                  }"""

    def __str__(self):
        """
        Returns a string containing the SCAD code
        for instantiating this Torus object.
        """
        return "Torus({0!s}, {1!s});".format(self.major, self.minor)
