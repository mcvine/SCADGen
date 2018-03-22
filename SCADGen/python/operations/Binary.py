from __future__ import absolute_import

from .Nary import Nary

class Binary(Nary):

    def __init__(self):
        Nary.__init__()
        return

    def isComp(self):
        return False

    def __eq__(self, rhs):
        """
        Returns true if two Binary operations are equal. Returns false otherwise.
        """
        if type(self) != type(rhs):
            return False
        elif self.comp1 != rhs.comp1 or self.comp2 != rhs.comp2:
            return False
        else:
            return True

    def addComp(self, component):
        if self.num_comps < 2:
            super(Binary, self).addComp(component)
        else:
            raise AttributeError("A binary operation cannot have more than 2 components.")
