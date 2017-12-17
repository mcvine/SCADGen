from components import Block, Cone, Cylinder, Sphere, Torus
from operations import Binary, Difference, Dilation, Intersection
from operations import Reflection, Rotation, Transformation, Translation, Union
import xml.etree.ElementTree as ET

class Parser:

    def __init__(self, xml_file):
        self.xmltree = ET.parse(xml_file)
        self.rootelems = []
        self.parse()
        return

    def parse(self):
        root = self.xmltree.getroot()
        for child in root:

    def getRootElem(self, elem):
        assert(elem is ET.Element, "Error: {0!s} is not an XML Element".format(elem))
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

    def isUnary(self, elem):
        tag = elem.tag
        if tag == "dilation" or tag == "reflection" or tag == "rotation" or tag == "translation":
            return True
        else if tag == "reversal":
            raise NotImplementedError("Reversal is not yet implemented")
        else:
            return False

