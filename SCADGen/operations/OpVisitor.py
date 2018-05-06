from __future__ import absolute_import

from . import Difference, Dilation, Intersection, Reflection, Rotation, Translation, Union
 
from abc import ABCMeta, abstractmethod

class OpVisitor:
    __metaclass__ = ABCMeta

    @abstractmethod
    def visitDifference(self, elem):
        raise NotImplementedError("OpVisitor is an abstract class! Use JSOpVisitor or SCADOpVisitor instead!")

    @abstractmethod
    def visitDilation(self, elem):
        raise NotImplementedError("OpVisitor is an abstract class! Use JSOpVisitor or SCADOpVisitor instead!")

    @abstractmethod
    def visitIntersection(self, elem):
        raise NotImplementedError("OpVisitor is an abstract class! Use JSOpVisitor or SCADOpVisitor instead!")

    @abstractmethod
    def visitReflection(self, elem):
        raise NotImplementedError("OpVisitor is an abstract class! Use JSOpVisitor or SCADOpVisitor instead!")

    @abstractmethod
    def visitRotation(self, elem):
        raise NotImplementedError("OpVisitor is an abstract class! Use JSOpVisitor or SCADOpVisitor instead!")

    @abstractmethod
    def visitTranslation(self, elem):
        raise NotImplementedError("OpVisitor is an abstract class! Use JSOpVisitor or SCADOpVisitor instead!")

    @abstractmethod
    def visitUnion(self, elem):
        raise NotImplementedError("OpVisitor is an abstract class! Use JSOpVisitor or SCADOpVisitor instead!")
