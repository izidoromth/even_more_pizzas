class Node:
    def __init__(self):
        self.parent = None
        self.child = []
        self.data = None

    def appendChild(self, child):
        child.parent = self
        self.child.append(child)

def findAllPaths(node, paths):
    if (len(node.child) == 0):
        paths.append(getPath(node))
    else:
        for c in node.child:
            findAllPaths(c, paths)


def getPath(node):
    path = []
    aux = node
    while (aux != None):
        path.append(aux)
        aux = aux.parent
    return path

a = Node()
a.data = "a"
b = Node()
b.data = "b"
c = Node()
c.data = "c"
d = Node()
d.data = "d"
e = Node()
e.data = "e"

b.appendChild(d)
b.appendChild(e)

a.appendChild(b)
a.appendChild(c)

paths = []
findAllPaths(a, paths)

teste = 5