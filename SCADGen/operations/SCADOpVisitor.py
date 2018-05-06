from __future__ import absolute_import

from .OpVisitor import OpVisitor as OP

import sys
import os

sys.path.append(os.path.abspath("../.."))
from SCADGen.components import SCADCompVisitor

class SCADOpVisitor(OP):

    def visitDifference(self, elem):
        visit = []
        for comp in elem.comps:
            visit.append(SCADCompVisitor() if comp.isComp() else SCADOpVisitor())
        return """difference() {{
    {0:s}
    {1:s}
}}""".format(elem.comps[0].accept(visit[0]), elem.comps[1].accept(visit[1]))

    def visitDilation(self, elem):
        visit = SCADCompVisitor() if elem.body.isComp() else SCADOpVisitor()
        return """scale([{0!s}, {0!s}, {0!s}]) {{
    {1:s}
}}""".format(elem.scale, elem.body.accept(visit))

    def visitIntersection(self, elem):
        tmp_str = """intersection() {\n"""
        for comp in elem.comps:
            visit = SCADCompVisitor() if comp.isComp() else SCADOpVisitor()
            tmp_str = tmp_str + """    {0:s}\n""".format(comp.accept(visit))
        tmp_str = tmp_str + """}"""
        return tmp_str

    def visitReflection(self, elem):
        visit = SCADCompVisitor() if elem.body.isComp() else SCADOpVisitor()
        return """mirror([{0!s}, {1!s}, {2!s}]) {{
    {3:s}
}}""".format(elem.vector[0], elem.vector[1], elem.vector[2], elem.body.accept(visit))

    def visitRotation(self, elem):
        visit = SCADCompVisitor() if elem.body.isComp() else SCADOpVisitor()
        return """rotate({0!s}, [{1!s}, {2!s}, {3!s}]) {{
    {4:s}
}}""".format(elem.angle, elem.vector[0], elem.vector[1], elem.vector[2], elem.body.accept(visit))

    def visitTranslation(self, elem):
        visit = SCADCompVisitor() if elem.body.isComp() else SCADOpVisitor()
        return """translate([{0!s}, {1!s}, {2!s}]) {{
    {3:s}
}}""".format(elem.vector[0], elem.vector[1], elem.vector[2], elem.body.accept(visit))

    def visitUnion(self, elem):
        tmp_str = """union() {\n"""
        for comp in elem.comps:
            visit = SCADCompVisitor() if comp.isComp() else SCADOpVisitor()
            tmp_str = tmp_str + """    {0:s}\n""".format(comp.accept(visit))
        tmp_str = tmp_str + """}"""
        return tmp_str
