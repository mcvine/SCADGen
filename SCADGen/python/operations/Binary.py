class Binary:

    def __init__(self):
        self.comp1 = None
        self.comp2 = None
        return

    def isComp(self):
        return False

    def __eq__(self, rhs):
        """
        Returns true if two Binary operations are equal. Returns false otherwise.
        """
        if type(self) != type(rhs):
            return False
        elif self.comp1 != rhs.comp1 or self.comp2 != rhs.comp2:
            return False
        else:
            return True
