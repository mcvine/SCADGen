from __future__ import absolute_import

from .CompVisitor import CompVisitor as CV

class SCADCompVisitor(CV):

    def visitBlock(self, elem):
        return "cube([{0!s}, {1!s}, {2!s}], center=true);".format(elem.x, elem.y, elem.z)

    def visitCone(self, elem):
        return "cylinder(h = {0!s}, r1 = {1!s}, r2 = {2!s}, $fn=100, center=true);".format(elem.height, elem.bottom_radius, elem.top_radius)

    def visitCylinder(self, elem):
        return "cylinder(h = {0!s}, r = {1!s}, $fn=100, center=true);".format(elem.height, elem.radius)

    def visitPyramid(self, elem):
        return """polyhedron(
    points=[ [{0!s},{1!s},-{2!s}], [{0!s},-{1!s},-{2!s}],
             [-{0!s},-{1!s},-{2!s}], [-{0!s},{1!s},-{2!s}], [0,0,0] ],
    faces=[ [0,1,4], [1,2,4], [2,3,4], [3,0,4], [1,0,3], [2,1,3] ]
);""".format((elem.x/2), (elem.y/2), elem.z)

    def visitSphere(self, elem):
        return "sphere(r = {0!s}, $fn=100);".format(elem.radius)

    def visitTorus(self, elem):
        return "Torus({0!s}, {1!s});".format(elem.major, elem.minor)
