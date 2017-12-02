class Torus:

    def __init__(self, xml_line):
        """
        Gets the major and minor axes dimensions
        for the Torus from its line in the XML file
        (xml_line) and stores them in member variables
        self.major and self.minor.
        """
        self.major = self.getMajor(xml_line) 
        self.minor = self.getMinor(xml_line)

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

    def getMajor(self, line):
        """
        Locates the "major" tag in "line" and uses
        its posistion to determin the major axis value. Then,
        converts the value to a float, and returns it.
        """
        maj_start_index = line.index("major");
        maj_start_index = maj_start_index + 7
        maj_substr = line[maj_start_index:]
        maj_ind2 = 0
        for c in maj_substr:
            if c == "\"":
                break
            maj_ind2 += 1
        maj_substr = maj_substr[:rad_ind2]
        return float(maj_substr)


    def getMinor(self, line):
        """
        Locates the "minor" tag in "line" and uses
        its posistion to determin the minor axis value. Then,
        converts the value to a float, and returns it.
        """
        min_start_index = line.index("minor");
        min_start_index = min_start_index + 7
        min_substr = line[min_start_index:]
        min_ind2 = 0
        for c in min_substr:
            if c == "\"":
                break
            min_ind2 += 1
        min_substr = min_substr[:rad_ind2]
        return float(min_substr)

    def __str__(self):
        """
        Returns a string containing the SCAD code
        for instantiating this Torus object.
        """
        return "Torus({0!s}, {1!s});".format(self.major, self.minor)
