from components import Block, Cone, Cylinder, Sphere, Torus
from operations import Binary, Difference, Dilation, Intersection
from operations import Reflection, Rotation, Transformation, Translation, Union
import xml.etree.ElementTree as ET

class Parser:

    def __init__(self, xml_file):
        self.xmltree = ET.parse(xml_file)
        self.rootelems = []
        self.containsTorus = False
        self.filename = xml_file
        self.parse()
        return

    def parse(self):
        root = self.xmltree.getroot()
        for child in root:
            self.rootelems.append(self.getRootElem(child))

    def getRootElem(self, elem):
        ## assert(elem is ET.Element, "Error: {0!s} is not an XML Element".format(elem))
        if self.isComp(elem):
            return self.makeComp(elem)
        else if self.isBinary(elem):
            children = list(elem)
            bin_op = self.makeBinary(elem)
            bin_op.comp1 = self.getRootElem(children[0])
            bin_op.comp2 = self.getRootElem(children[1])
            return bin_op
        else:
            comp1 = None
            attrs = []
            for child in elem:
                if self.isBinary(child) or self.isComp(child) or self.isUnary(child):
                    comp1 = child
                else:
                    attrs.append(child)
            un_op = self.makeUnary(elem, attrs)
            un_op.body = self.getRootElem(comp1)
            return un_op
        
    def isComp(self, elem):
        tag = elem.tag
        if tag == "block" or tag == "cone" or tag == "cylinder" or tag == "sphere" or tag == "torus":
            return True
        else if tag == "generalized-cone":
            raise NotImplementedError("Generalized Cone is not yet implemented")
        else:
            return False

    def makeComp(self, elem):
        tag = elem.tag
        if tag == "block":
            return Block(elem)
        else if tag == "cone":
            return Cone(elem)
        else if tag == "cylinder":
            return Cylinder(elem)
        else if tag == "sphere":
            return Sphere(elem)
        else if tag == "torus":
            self.containsTorus = True
            return Torus(elem)
        else if tag == "generalized-cone":            
            raise NotImplementedError("Generalized Cone is not yet implemented")
        else:
            raise NotImplementedError("{0!s} is not implemented".format(tag))

    def isBinary(self, elem):
        tag = elem.tag
        if tag == "difference" or tag == "intersection" or tag == "union":
            return True
        else:
            return False

    def makeBinary(self, elem):
        tag = elem.tag
        if tag == "difference":
            return Difference()
        else if tag == "intersection"
            return Intersection()
        else if tag == "union":
            return Union()
        else: 
            raise NotImplementedError("{0!s} is not implemented".format(tag))

    def isUnary(self, elem):
        tag = elem.tag
        if tag == "dilation" or tag == "reflection" or tag == "rotation" or tag == "translation":
            return True
        else if tag == "reversal":
            raise NotImplementedError("Reversal is not yet implemented")
        else:
            return False

    def makeUnary(self, elem, attrs):
        tag = elem.tag
        assert(len(attrs) > 0)
        if tag == "dilation":
            assert(attrs[0].tag == "scale")
            return Dilation(attrs[0])
        else if tag == "reflection":
            assert(attrs[0].tag == "vector")
            return Reflection(attrs[0])
        else if tag == "reversal":
            raise NotImplementedError("Reversal is not yet implemented")
        else if tag == "rotation":
            assert(len(attrs) >= 2)
            assert((attrs[0].tag == "angle" and attrs[1].tag == "vector")
                or (attrs[0].tag == "vector" and attrs[1].tag == "angle"))
            angle = None
            vector = None
            if attrs[0] == "angle":
                angle = attrs[0]
                vector = attrs[1]
            else:
                angle = attrs[1]
                vector = attrs[0]
            return Rotation(angle, vector)
        else if tag == "translation":
            assert(attrs[0].tag == "vector")
            return Translation(attrs[0])
        else:
            raise NotImplementedError("{0!s} is not implemented".format(tag))

    def printTorusModule(self):
        """
        Returns a string containing the OpenSCAD code
        for the Torus module. When a torus is used,
        the string will be added to the beginning of
        the OpenSCAD file.
        """
        return """module Torus(rx, ry) {
                      resize([rx, ry, 10])
                      rotate_extrude(convexity = 10)
                      translate([2, 0, 0])
                      circle(r = 1, $fn = 100)
                  }"""

    def createSCAD(self):
        fname = self.filename[:-3] + "scad"
        scadfile = open(fname, "w+")
        if self.containsTorus:
            scadefile.write(self.printTorusModule())
        for elem in self.rootelems: 
            if self.isComp(elem):
                continue
            scadfile.write("{0!s}".format(elem))
        scadfile.close()
        return
