class Block:

    def __init__(self, xml_line):
        """
        Gets width, height, and thickness from its line
        in the XML file (xml_line) and stores them in
        member variables self.x, self.y, and self.z.
        """
        self.x = self.get_width(xml_line)
        self.y = self.get_thickness(xml_line)
        self.z = self.get_height(xml_line)
        return 

    def get_width(self, line):
        """
        Locates the "width" tag in "line" and uses its position
        to determine the width value. Then, converts
        the value to a float, and returns it.
        """
        wd_start_index = line.index("width")
        wd_start_index = wd_start_index + 7
        wd_substr = line[wd_start_index:]
        wd_ind2 = 0
        for c in wd_substr:
            if c == "\"":
                break
            wd_ind2 += 1
        wd_substr = wd_substr[:wd_ind2]
        return float(wd_substr)

    def get_thickness(self, line):
        """
        Locates the "thickness" tag in "line" and uses
        its position to determine the thickness value.
        Then, converts the value to a float, and returns it.
        """
        th_start_index = line.index("thickness")
        th_start_index = th_start_index + 11
        th_substr = line[th_start_index:]
        th_ind2 = 0
        for c in th_substr:
            if c == "\"":
                break
            th_ind2 += 1
        th_substr = th_substr[:th_ind2]
        return float(th_substr)

    def get_height(self, line):
        """
        Locates the "height" tag in "line" and uses its position
        to determine the height value. Then, converts
        the value to a float, and returns it.
        """
        ht_start_index = line.index("height")
        ht_start_index = ht_start_index + 8
        ht_substr = line[ht_start_index:]
        ht_ind2 = 0
        for c in ht_substr:
            if c == "\"":
                break
            ht_ind2 += 1
        ht_substr = ht_substr[:ht_ind2]
        return float(ht_substr)

    def __str__(self):
        """
        Returns a string containing the SCAD
        code for this block/cube object.
        """
        return "cube([{0!s}, {1!s}, {2!s}]);".format(self.x, self.y, self.z)
