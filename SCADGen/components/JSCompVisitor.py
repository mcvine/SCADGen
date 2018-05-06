from __future__ import absolute_import

from .CompVisitor import CompVisitor as CV

class JSCompVisitor(CV):

    def visitBlock(self, elem):
        raise NotImplementedError("JS code generation is not yet implemented.")

    def visitCone(self, elem):
        raise NotImplementedError("JS code generation is not yet implemented.")

    def visitCylinder(self, elem):
        raise NotImplementedError("JS code generation is not yet implemented.")

    def visitPyramid(self, elem):
        raise NotImplementedError("JS code generation is not yet implemented.")

    def visitSphere(self, elem):
        raise NotImplementedError("JS code generation is not yet implemented.")

    def visitTorus(self, elem):
        raise NotImplementedError("JS code generation is not yet implemented.")
