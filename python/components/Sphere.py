class Sphere:

    def __init__(self, xml_line):
        """
        Gets the radius for the sphere from
        its line in the XML file (xml line) and
        stores them in member variable self.radius.
        """
        self.radius = self.get_radius(xml_line)
        return 

    def get_radius(self, line):
        """
        Locates the "radius" tag in "line" and uses its
        position to determine the radius value. Then, converts
        the value to a float, and returns it.
        """
        rad_start_index = line.index("radius")
        rad_start_index = rad_start_index + 8
        rad_substr = line[rad_start_index:]
        rad_ind2 = 0
        for c in rad_substr:
            if c == "\"":
                break
            rad_ind2 += 1
        rad_substr = rad_substr[:rad_ind2]
        return float(rad_substr)

    def __str__(self):
        """
        Returns a string containing the SCAD
        code for this sphere objec.
        """
        return "sphere(r = {0!s}, $fn=100);".format(self.radius)
