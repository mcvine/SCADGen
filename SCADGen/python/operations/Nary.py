class Nary:

    def __init__(self):
        self.comps = []
        self.num_comps = 0
        return

    def isComp(self):
        return False

    def addComp(self, component):
        self.comps.append(component)
        self.num_comps += 1
