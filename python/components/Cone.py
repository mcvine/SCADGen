import xml.etree.ElementTree as ET

class Cone:

    def __init__(self, xml_elem):
        """
        Gets bottom/top radius and height for the cone
        from the attributes from its XML line. These attributes
        are accessed with the xml.etree.ElementTree.Element
        object, xml_elem."
        """
        self.bottom_radius = xml_elem.get("bottomRadius")
        self.top_radius = xml_elem.get("topRadius")
        self.height = xml_elem.get("height")
        return

    def __str__(self):
        """
        Returns a string containing the SCAD
        code for this Cone object.
        """
        return "cylinder(h = {0!s}, r1 = {1!s}, r2 = {2!s});".format(
            self.height, self.bottom_radius, self.top_radius)
