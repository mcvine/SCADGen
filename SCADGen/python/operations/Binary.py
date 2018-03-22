from __future__ import absolute_import

from .Nary import Nary

class Binary(Nary):

    def __init__(self):
        Nary.__init__(self)
        return

    def isComp(self):
        return False

    def __eq__(self, rhs):
        """
        Returns true if two Binary operations are equal. Returns false otherwise.
        """
        if type(self) != type(rhs):
            return False
        elif self.comps[0] != rhs.comps[0] or self.comps[1] != rhs.comps[1]:
            return False
        else:
            return True

    def addComp(self, component):
        if self.num_comps < 2:
            Nary.addComp(self, component)
        else:
            raise AttributeError("A binary operation cannot have more than 2 components.")
