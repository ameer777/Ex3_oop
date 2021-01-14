

class EdgeData:

    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.edgeW = weight
        self.tag = -1
        self.info = "white"

    def getSrc(self):
        return self.src

    def getDest(self):
        return self.dest

    def getWeight(self):
        return self.edgeW

    def getInfo(self):
        return self.info

    def setInfo(self, s):
        self.info = s

    def getTag(self):
        return self.tag

    def setTag(self, s):
        self.tag = s