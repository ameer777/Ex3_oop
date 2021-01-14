import json

class NodeData:

    def __init__(self, key, pos=None):
        self.key = key
        self.tag = -1
        self.info = "white"
        self.nodeW = -1
        self.location = pos
        self.in_edges = []
        self.out_edges = []

    def getKey(self):
        return self.key

    def getLocation(self):
        return self.location

    def setLocation(self, x, y):
        self.location = [x, y]

    def getWeight(self):
        return self.nodeW

    def setWeight(self, w):
        self.nodeW = w

    def getInfo(self):
        return self.info

    def setInfo(self, s):
        self.info = s

    def getTag(self):
        return self.tag

    def setTag(self, t):
        self.tag = t

    def getInEdges(self):
        return self.in_edges

    def getOutEdges(self):
        return self.out_edges

    def addInEdge(self, e):
        if e not in self.in_edges:
            self.in_edges.append(e)

    def removeInEdge(self, e):
        if e in self.in_edges:
            self.in_edges.remove(e)

    def addOutEdge(self, e):
        if e not in self.out_edges:
            self.out_edges.append(e)

    def removeOutEdge(self, e):
        if e in self.in_edges:
            self.out_edges.remove(e)

    def addAllInEdges(self, InEdges):
        self.in_edges = InEdges

    def addAllOutEdges(self, OutEdges):
        self.out_edges = OutEdges

    def compareTo(self, node_data):
        if self.nodeW - node_data.getWeight() > 0:
            return 1
        elif self.nodeW - node_data.getWeight() < 0:
            return -1
        return 0

    def __lt__(self, other):
        if self.key != other.getKey():
            return True
        else:
            return False

    def __eq__(self, other):
        if self.key == other.getKey():
            return True
        else:
            return False

    def __cmp__(self, other):
        if self.key == other.getKey():
            return 1
        else:
            return 0
