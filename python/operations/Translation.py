from Transformation import Transformation

class Translation(Transformation):

    def __init__(self, vector):
        """
        Stores the component for the translation and
        the translation directions in member variables
        self.body and self.vector.
        """
        Transformation.__init__(self)
        self.vector = vector
        return

    def __str__(self):
        """
        Returns a string containing the SCAD code
        for the translation.
        """
        return """translate([{0!s}, {1!s}, {2!s}]) {
                      {3!s};
                  }""".format(self.vector[0], self.vector[1],
                              self.vector[2], self.body)
