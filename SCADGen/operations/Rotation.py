from __future__ import absolute_import

from .Transformation import Transformation

class Rotation(Transformation):

    def __init__(self, angle, vector):
        """
        Stores the component for the rotation, the
        vector about which the rotation occurs, and the
        angle of rotation in self.body, self.vector, and
        self.angle.
        """
        Transformation.__init__(self)
        from . import unit_parser, angle_unit
        beam = float(vector.get("beam"))
        transversal = float(vector.get("transversal"))
        vertical = float(vector.get("vertical"))
        self.vector = []
        self.vector.append(beam)
        self.vector.append(transversal)
        self.vector.append(vertical)
        self.angle = unit_parser.parse(angle)/angle_unit
        """v = vector[1:-1]
        comma1 = v.find(",")
        comma2 = v[comma1+1:].find(",") + comma1 + 1
        self.vector.append(float(v[:comma1].replace(" ", "")))
        self.vector.append(float(v[comma1+1:comma2].replace(" ", "")))
        self.vector.append(float(v[comma2+1:].replace(" ", "")))"""
        return

    def accept(self, visit):
        from . import SCADOpVisitor, JSOpVisitor
        assert(isinstance(visit, SCADOpVisitor) or isinstance(visit, JSOpVisitor))
        return visit.visitRotation(self)

    def __eq__(self, rhs):
        """
        Returns true if the two Rotation operations are equal. Returns false otherwise.
        """
        if type(self) != type(rhs):
            return False
        elif self.body != rhs.body or self.angle != rhs.angle or self.vector != rhs.vector:
            return False
        else:
            return True

    def __ne__(self, rhs):
        return not (self == rhs)
