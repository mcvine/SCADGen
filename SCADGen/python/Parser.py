from __future__ import absolute_import

import components
import operations
import xml.etree.ElementTree as ET

class Parser:

    def __init__(self, xml_file):
        """
        This constructor creates an XML ElementTree object
        from the xml file passed as a parameter. Then, after
        setting the other members to default values, it calls
        the parse() function.
        """
        self.xmltree = ET.parse(xml_file)
        self.rootelems = []
        self.containsTorus = False
        self.containsop = False
        self.filename = xml_file
        self.parse()
        return

    def parse(self):
        """
        This function calls the getRootElem function
        on the top-level elements to generate the Python
        object structure that will be used to create the
        OpenSCAD code.
        """
        root = self.xmltree.getroot()
        for child in root:
            self.rootelems.append(self.getRootElem(child))

    def getRootElem(self, elem):
        """
        Using helper functions, this function recursively
        generates the Python object structure of a root element
        and its subelements.
        """
        # If the element is a component, it cannot have any children,
        # so the Python object for it is returned."""
        if self.isComp(elem):
            return self.makeComp(elem)
        # If the element is a binary operation, it is created, and its
        # children in the Python object are set by recursively calling
        # this function. The operation is then returned.
        elif self.isBinary(elem):
            children = list(elem)
            bin_op = self.makeNary(elem)
            bin_op.addComp(self.getRootElem(children[0]))
            bin_op.addComp(self.getRootElem(children[1]))
            return bin_op
        elif self.isNary(elem):
            children = list(elem)
            nary_op = self.makeNary(elem)
            for child in children:
                nary_op.addComp(self.getRootElem(child))
            return nary_op
        # If the element is an unary operation, the code determines
        # which of the element's children is a component or operation
        # and which are attributes. After determining this, the Python
        # object for the unary operation is created, and its body member
        # is set by recursively calling this function. Finally, the
        # Python object for the unary operation is returned.
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
        """
        This function returns True if the element's tag identifies
        it as such. If the element has the tag "generalized-cone",
        a NotImplementedError is currently returned because it is not
        yet implemented in this repository. This will be removed later.
        Otherwise, the element is not a component, and the function
        returns False.
        """
        tag = elem.tag
        if tag == "block" or tag == "cone" or tag == "cylinder" or tag == "pyramid" or tag == "sphere" or tag == "torus":
            return True
        elif tag == "generalized-cone":
            raise NotImplementedError("Generalized Cone is not yet implemented")
        else:
            return False

    def makeComp(self, elem):
        """
        This function uses the element's tag and its
        ElementTree object to create the correct Python
        object, which is then returned. If the element trying
        to be created is not (yet) implemented in this repository,
        a NotImplementedError is raised.
        """
        tag = elem.tag.title()
        if tag == "Generalized-Cone":
            raise NotImplementedError("Generalized Cone is not yet implemented")
        try:
            ctor = getattr(components, tag)
            return ctor(elem)
        except AttributeError:
            raise NotImplementedError("{0!s} is not implemented".format(tag))

    def isBinary(self, elem):
        """
        If the element's tag identifies it as a binary
        operation, this function returns True. Otherwise,
        it returns False.
        """
        tag = elem.tag
        if tag == "difference":
            return True
        else:
            return False

    #def makeBinary(self, elem):
        """
        Using the element's tag, this function creates the
        correct basic Python object, which is then returned.
        If the element is not (yet) implemented in this
        repository, a NotImplementedError is raised.
        """
        """if not self.containsop:
            self.containsop = True
        tag = elem.tag.title()
        try:
            ctor = getattr(operations, tag)
            return ctor()
        except AttributeError:
            raise NotImplementedError("{0!s} is not implemented".format(tag))"""
            
    def isNary(self, elem):
      """
      If the element's tag identifies it as a Nary
      operation, this function returns True. Otherwise,
      it returns False.
      """
      tag = elem.tag
      if tag == "union" or tag == "intersection":
          return True
      else:
          return False

    def makeNary(self, elem):
      """
      Using the element's tag, this function creates the
      correct basic Python object, which is then returned.
      If the element is not (yet) implemented in this
      repository, a NotImplementedError is raised.
      """
      if not self.containsop:
          self.containsop = True
      tag = elem.tag.title()
      try:
          ctor = getattr(operations, tag)
          return ctor()
      except AttributeError:
          raise NotImplementedError("{0!s} is not implemented".format(tag))

    def isUnary(self, elem):
        """
        If the element's tag identifies it as an unary
        operation, this function returns True. Otherwise,
        it returns False. If the element is a reversal,
        a NotImplementedError is raised, as the reversal operation
        has not yet been implemented in this repository. This will
        be removed later.
        """
        if not self.containsop:
            self.containsop = True
        tag = elem.tag
        if tag == "dilation" or tag == "reflection" or tag == "rotation" or tag == "translation":
            return True
        elif tag == "reversal":
            raise NotImplementedError("Reversal is not yet implemented")
        else:
            return False

    def makeUnary(self, elem, attrs):
        """
        Using the element's tag and the attributes determined
        in the getRootElems() function, this function creates the
        correct basic Python object, which is then returned.
        If the element is not (yet) implemented in this
        repository, a NotImplementedError is raised. The extra
        code in this function compared to the other "make" functions
        is used to pass the correct attributes into the constructor
        for the Python object being made.
        """
        tag = elem.tag
        assert(len(attrs) > 0)
        if tag == "dilation":
            assert(attrs[0].tag == "scale")
            return operations.Dilation(float(attrs[0].text))
        elif tag == "reflection":
            assert(attrs[0].tag == "vector")
            return operations.Reflection(attrs[0].text)
        elif tag == "reversal":
            raise NotImplementedError("Reversal is not yet implemented")
        elif tag == "rotation":
            assert(len(attrs) >= 2)
            assert((attrs[0].tag == "angle" and attrs[1].tag == "vector")
                or (attrs[0].tag == "vector" and attrs[1].tag == "angle"))
            angle = None
            vector = None
            if attrs[0].tag == "angle":
                angle = attrs[0]
                vector = attrs[1]
            else:
                angle = attrs[1]
                vector = attrs[0]
            return operations.Rotation(angle.text, vector)
        elif tag == "translation":
            assert(attrs[0].tag == "vector")
            return operations.Translation(attrs[0])
        else:
            raise NotImplementedError("{0!s} is not implemented".format(tag))

    def printTorusModule(self):
        """
        Returns a string containing the OpenSCAD code
        for the Torus module. When a torus is used,
        the string will be added to the beginning of
        the OpenSCAD file.
        """
        return """module Torus(major, minor) {
    rotate_extrude(convexity = 10, $fn=100)
    translate([major, 0, 0])
    circle(r = minor, $fn = 100);
}\n\n"""

    def createSCAD(self):
        """
        This function creates the OpenSCAD file from a Parser object.
        """
        fname = self.filename[:-3] + "scad"
        scadfile = open(fname, "w+")
        # If the XML file contains a torus, the torus module is
        # added to the beginning of the OpenSCAD file.
        if self.containsTorus:
            scadfile.write(self.printTorusModule())
        # This for loop causes any root elements that do not have
        # children to not be printed to the OpenSCAD file.
        for elem in self.rootelems:
            if self.containsop and elem.isComp():
                continue
            scadfile.write("{0!s}".format(elem))
        scadfile.close()
        return
