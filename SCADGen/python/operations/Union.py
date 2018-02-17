from __future__ import absolute_import

from Binary import Binary

class Union(Binary):

    def __init__(self):
        """
        Stores the two components for the Union
        operation in member variables self.comp1 and
        self.comp2.
        """
        Binary.__init__(self)
        return

    def __str__(self):
        """
        Returns a string containing the SCAD
        code for implementing the Union.
        """
        return """union() {{
    {0!s}
    {1!s}
}}""".format(self.comp1, self.comp2)
