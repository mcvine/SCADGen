from __future__ import absolute_import

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

    def accept(self, visit):
        from . import SCADOpVisitor, JSOpVisitor
        assert(isinstance(visit, SCADOpVisitor) or isinstance(visit, JSOpVisitor))
        return visit.visitDifference(self)
