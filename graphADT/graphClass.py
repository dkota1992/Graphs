class Graph(object):
    
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
    
    def addVertex(self,key):
        newVertex = Vertex(key)
        self.numVertices += 1
        self.vertList[key] = newVertex
    
    def addEdge(self,fromVert,toVert,weight=None):
        if fromVert not in self.vertList: self.addVertex(fromVert)
        if toVert not in self.vertList: self.addVertex(toVert)
        self.vertList[fromVert].addNeighbour(self.vertList[toVert],weight)   
        
    def __str__(self):     
        return str([str(v) for k,v in self.vertList.items()])
    
    def getVertex(self,vertKey):
        if vertKey in self.vertList:
            return self.vertList[vertKey]
        else: return None
        
    def __contains__(self,key):
        return key in self.vertList
    
    def getVertices(self):
        return self.vertList.keys()
    
    def __iter__(self):
        return iter(self.vertList.values())
    
    
class Vertex(object):
    
    def __init__(self,key):
        self.id = key
        self.connectedto = {}
        
    def addNeighbour(self,nbr,weight=None):
        self.connectedto[nbr] = weight
        
    def __str__(self):
        return str(self.id) + " Connected to " + \
            str(["{} with weight {}".format(k,v) for k,v in self.connectedto.items()])
            
    def getConnections(self):
        return self.connectedto.keys()
    
    def getId(self):
        return self.id
    
    def getWeight(self,nbr):
        return self.connectedto[nbr]
        
    
    
    
    
    