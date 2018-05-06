from __future__ import absolute_import

from .Nary import Nary

class Union(Nary):

    def __init__(self):
        """
        Stores the n components for the Union
        operation in a member list self.comps and
        self.comp2.
        """
        Nary.__init__(self)
        return

    def accept(self, visit):
        from . import SCADOpVisitor, JSOpVisitor
        assert(isinstance(visit, SCADOpVisitor) or isinstance(visit, JSOpVisitor))
        return visit.visitUnion(self)
