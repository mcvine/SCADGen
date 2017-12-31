from components import Block, Cone, Cylinder, Sphere, Torus
from operations import Binary, Difference, Dilation, Intersection
from operations import Reflection, Rotation, Transformation, Translation, Union
from Parser import Parser

parser = Parser("test4.xml")
parser.createSCAD()
