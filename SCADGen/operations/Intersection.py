from __future__ import absolute_import

from .Nary import Nary

class Intersection(Nary):

    def __init__(self):
        """
        Stores the components for the Intersection
        in member variables self.comp1 self.comp2.
        """
        Nary.__init__(self)
        return

    def accept(self, visit):
        from . import SCADOpVisitor, JSOpVisitor
        assert(isinstance(visit, SCADOpVisitor) or isinstance(visit, JSOpVisitor))
        return visit.visitIntersection(self)
