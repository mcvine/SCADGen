from __future__ import absolute_import

from . import Block, Cone, Cylinder, Pyramid, Sphere, Torus

from abc import ABCMeta, abstractmethod

class CompVisitor:
    __metaclass__ = ABCMeta

    @abstractmethod
    def visitBlock(self, elem):
        raise NotImplementedError("CompVisitor is abstract! Use JSCompVisitor or SCADCompVisitor instead!")

    @abstractmethod
    def visitCone(self, elem): 
        raise NotImplementedError("CompVisitor is abstract! Use JSCompVisitor or SCADCompVisitor instead!")

    @abstractmethod
    def visitCylinder(self, elem):
        raise NotImplementedError("CompVisitor is abstract! Use JSCompVisitor or SCADCompVisitor instead!")

    @abstractmethod
    def visitPyramid(self, elem):
        raise NotImplementedError("CompVisitor is abstract! Use JSCompVisitor or SCADCompVisitor instead!")

    @abstractmethod
    def visitSphere(self, elem):
        raise NotImplementedError("CompVisitor is abstract! Use JSCompVisitor or SCADCompVisitor instead!")

    @abstractmethod
    def visitTorus(self, elem):
        raise NotImplementedError("CompVisitor is abstract! Use JSCompVisitor or SCADCompVisitor instead!")
