import networkx as nx

class ConnGraph_Infos:

    def __init__(self):

        self.nxGraph = None
        self.dictGraph = None

        self.idName = {}  # Link between ID and Name of each area -> {ID_Node: Name}
        self.areaInfos = {}  # Area Informations 
                             # {Name: {SumConnectivity, RGBA, Side, Wider_Area, ID_Opposite, 3D_Coos} List: [List Order]} -> FLUT File
        self.areasOrder = []  # Order of areas (with blanks)
        self.edgesValues = {}  # Value of each edge in the graph -> {ID_Node: [(ID_Next, Value)]}

        self.numberOfNodes = 0
        self.numberOfEdges = 0

        self.edgesValues_withoutDuplicata = {}
        self.adjacencyMatrix = []
        self.degree = []

    # =========================
    # Define the Graph Variable
    # =========================
    def SetGraph(self, nxGraph: nx.Graph):

        self.nxGraph = nxGraph
        self.dictGraph = nx.to_dict_of_dicts(self.nxGraph)

        if nx.empty_graph(self.nxGraph):
            self.edgesValues_withoutDuplicata = nx.get_edge_attributes(self.nxGraph, 'weight')
            self.adjacencyMatrix = nx.adjacency_matrix(self.nxGraph).todense()
            self.degree = [(node, val) for (node, val) in self.nxGraph.degree()]
        self.nxGraph.number_of_nodes()

    # ===================================
    # Define the Number of Nodes Variable
    # ===================================
    def SetNumberOfNodes(self, numberOfNodes: int):
        self.numberOfNodes = numberOfNodes

    # ===================================
    # Define the Number of Edges Variable
    # ===================================
    def SetNumberOfEdges(self, numberOfEdges: int):
        self.numberOfEdges = numberOfEdges

    # =============================
    # Define the Area Info Variable
    # =============================
    def SetAreaInfos(self, areaInfos: dict):
        self.areaInfos = areaInfos

    # =============================
    # Define the Area Info Variable
    # =============================
    def SetAreasOrder(self, areasOrder: list):
        self.areasOrder = areasOrder
        
    # ================================
    # Define the Edges Values Variable
    # ================================
    def SetEdgesValues(self, edgesValues: dict):
        self.edgesValues = edgesValues

    # ===========================
    # Define the ID/Name Variable
    # ===========================
    def SetIDName(self, idName: dict):
        self.idName = idName

    # ============================================
    # Return the name corresponding to a region ID
    # ============================================
    def GetRegionNameWithID(self, ID: int):
        for regionID, regionName in self.idName.items():
            if regionID == ID:
                return regionName
        return None

    # ============================================
    # Return the ID corresponding to a region name
    # ============================================
    def GetRegionIDWithName(self, name: str):
        for regionID, regionName in self.idName.items():
            if regionName == name:
                return regionID
        return None

    # ============================================================================
    # Return the list of name with connectivity (remove name without connectivity)
    # ============================================================================
    def GetAllNameWithConnectivity(self):

        namesWithConnectivity = []
        for id in self.edgesValues.keys():
            namesWithConnectivity.append(self.GetRegionNameWithID(id))

        return namesWithConnectivity
    
    # ====================================
    # Return a list of all weight of edges
    # ====================================
    def GetAllValues(self):

        return list(self.edgesValues_withoutDuplicata.values())

    # =========================================================
    # Return a list of all edges with detailed infos about them
    # =========================================================
    def GetEdgesDetails(self):
        edgesDetails = []

        for edge, nextEdgeValues in self.edgesValues.items():
            for nextEdgeValue in nextEdgeValues:

                region_1 = self.GetRegionNameWithID(edge)
                region_2 = self.GetRegionNameWithID(nextEdgeValue[0])

                #TODO : determine conn type

                details = [edge, nextEdgeValue[0], region_1, region_2, "type connexion", nextEdgeValue[1]]

                edgesDetails.append(details)

        return edgesDetails

    # ====================================================================
    # Return a dict of all connectivity (nextNodeName, weight) from a node
    # ====================================================================
    def GetAllConnectivityWithName(self, name: str):

        id_name = self.GetRegionIDWithName(name)

        connectivities = {}
        for nextIDwithValue in self.edgesValues[id_name]:
            connectivities[self.GetRegionNameWithID(nextIDwithValue[0])] = nextIDwithValue[1]
            
        return connectivities

    # ===============
    # Print all infos
    # ===============
    def Print(self):

        print("ID_Name", self.idName)
        print("Area_Infos", self.areaInfos)
        print("Area_Infos_len", len(self.areaInfos))
        #print("Edges_Values", self.Edges_Values)




# A faire lorsqu'on utilisera FLUT File (pour récupérer les élements avec une fonction et non self.truc[0])
def GetName_FLUT():
    pass

# other RGBA / Side, ID_Opposite, Wider_Area, 3D_coos