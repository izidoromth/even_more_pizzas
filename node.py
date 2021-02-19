class Node:
    def __init__(self):
        self.parent = None
        self.child = []
        self.data = None

    def appendChild(self, child):
        child.parent = self
        self.child.append(child)