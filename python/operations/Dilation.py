from Tranformation import Transformation

class Dilation(Transformation):

    def __init__(self, body, scale):
        """
        Stores the component for the Dilation and
        the scaling factor in member variables
        self.body and self.scale.
        """
        Transformation.__init__(self, body)
        self.scale = scale
        return

    def __str__(self):
        """
        Returns a string containing the SCAD
        code for the dilation.
        """
        return """scale([{0!s}, {0!s}, {0!s}]) {
                      {1!s};
                  }""".format(self.scale, self.body)
