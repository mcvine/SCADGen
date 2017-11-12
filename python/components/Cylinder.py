class Cylinder:

    def __init__(self, xml_line):
        """
        Gets radius and height for the cylinder from
        its line in the XML file (xml_line) and stores
        them in member variables self.radius and
        self.height.
        """
        self.radius = self.get_radius(xml_line)
        self.height = self.get_height(xml_line)
        return

    def get_radius(self, line):
        """
        Locates the "radius" tag in "line" and uses its position
        to determine the radius value. Then, converts
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

    def get_height(self, line):
        """
        Locates the "height" tag in "line" and uses its position
        to determine the height value. Then, converts
        the value to a float, and returns it.
        """
        hgt_start_index = line.index("height")
        hgt_start_index = hgt_start_index + 8
        hgt_substr = line[hgt_start_index:]
        hgt_ind2 = 0
        for c in hgt_substr:
            if c == "\"":
                break
            hgt_ind2 += 1
        hgt_substr = hgt_substr[:hgt_ind2]
        return float(hgt_substr)

    def __str__(self):
        """
        Returns a string containing the SCAD
        code for this cylinder object.
        """
        return "cylinder(h = {0!s}, r = {1!s});".format(self.height, self.radius)
