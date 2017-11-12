class Cone:

    def __init__(self, xml_line):
        """
        Gets bottom/top radius and height for the cone
        from its line in the XML file (xml_line) and stores
        them in member variables self.bottom_radius,
        self.top_radius, and self.height.
        """
        self.bottom_radius = self.get_bottom_radius(xml_line)
        self.top_radius = self.get_top_radius(xml_line)
        self.height = self.get_height(xml_line) 
        return

    def get_top_radius(self, line):
        """
        Locates the "top" tag in "line" and uses its position
        to determine the top radius value. Then, converts
        the value to a float, and returns it.
        """
        tr_start_index = line.index("top")
        tr_start_index = tr_start_index + 5
        tr_substr = line[tr_start_index:]
        tr_ind2 = 0
        for c in tr_substr:
            if c == "\"":
                break
            tr_ind2 += 1
        tr_substr = tr_substr[:tr_ind2]
        return float(tr_substr)

    def get_bottom_radius(self, line):
        """
        Locates the "bottom" tag in "line" and uses its position
        to determine the bottom radius value. Then, converts
        the value to a float, and returns it.
        """
        br_start_index = line.index("bottom")
        br_start_index = br_start_index + 8
        br_substr = line[br_start_index:]
        br_ind2 = 0
        for c in br_substr:
            if c == "\"":
                break
            br_ind2 += 1
        br_substr = br_substr[:br_ind2]
        return float(br_substr)

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
        code for this Cone object.
        """
        return "cylinder(h = {0!s}, r1 = {1!s}, r2 = {2!s});".format(
            self.height, self.bottom_radius, self.top_radius)
