from .Binary import Binary

class Difference(Binary):

    def __init__(self):
        """
        Stores the components for the difference
        operation in member variables self.comp1 and
        self.comp2.
        """
        Binary.__init__(self)
        return

    def __str__(self):
        """
        Returns a string containing the SCAD code
        for implementing a difference.
        """ 
        return """difference() {{
    {0!s}
    {1!s}
}}""".format(self.comp1, self.comp2)
