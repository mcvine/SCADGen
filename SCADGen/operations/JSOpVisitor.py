from __future__ import absolute_import

from .OpVisitor import OpVisitor as OP

import sys
import os

sys.path.append(os.path.abspath("../.."))
from SCADGen.components import JSCompVisitor

class JSOpVisitor(OP):

    def visitDifference(self, elem):
        raise NotImplementedError("JS code generation is not yet implemented.")

    def visitDilation(self, elem):
        raise NotImplementedError("JS code generation is not yet implemented.")

    def visitIntersection(self, elem):
        raise NotImplementedError("JS code generation is not yet implemented.")

    def visitReflection(self, elem):
        raise NotImplementedError("JS code generation is not yet implemented.")

    def visitRotation(self, elem):
        raise NotImplementedError("JS code generation is not yet implemented.")

    def visitTranslation(self, elem):
        raise NotImplementedError("JS code generation is not yet implemented.")

    def visitUnion(self, elem):
        raise NotImplementedError("JS code generation is not yet implemented.")
