import networkx as nx

class ConnGraph_Infos:

    def __init__(self):

        self.nxGraph = None
        self.dictGraph = None

        self.idName = {}  # Link between ID and Name of each area -> {ID_Node: Name}
        self.areaInfos = {}  # Area Informations 
                             # {Name: {ID, RGBA, Side, MajorRegion, ID_Opposite, 3D_Coos}} -> FLUT File
        self.areasOrder = []  # Order of areas (with blanks)
        self.edgesValues = {}  # Value of each edge in the graph -> {ID_Node: {ID_Next: Value}}
        self.edgesTypeConnexion = {}  # Connexion Type -> ID_Node: {ID_Next: Value}
                                      # Value in ("Contralateral", "Homotopic", "Ipsilateral", "Other")

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

    def SetTypeConnexion(self):

        for edge_source, edgesDestValue in self.edgesValues.items():

            name_source = self.idName[edge_source]
            if edge_source not in self.edgesTypeConnexion:
                self.edgesTypeConnexion[edge_source] = {}

            for edge_dest in edgesDestValue.keys():

                name_dest = self.idName[edge_dest]

                # Ipsilateral Connexion
                if self.areaInfos[name_source]["Side"] == self.areaInfos[name_dest]["Side"]:
                    self.edgesTypeConnexion[edge_source][edge_dest] = "Ipsilateral"

                elif self.areaInfos[name_source]["Side"] != self.areaInfos[name_dest]["Side"]:

                    # 2 -> 0 or 0 -> 2 => Other Connexion
                    if self.areaInfos[name_source]["Side"] == 0 or self.areaInfos[name_dest]["Side"] == 0:
                        self.edgesTypeConnexion[edge_source][edge_dest] = "Other"

                    # Contralateral or Homotopic Connexion
                    else:
                        if self.areaInfos[name_source]["ID_Opposite"] == self.areaInfos[name_dest]["ID"]:
                            self.edgesTypeConnexion[edge_source][edge_dest] = "Homotopic"
                        else:
                            self.edgesTypeConnexion[edge_source][edge_dest] = "Contralateral"
                            
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

        for edge_source, nextEdgeValues in self.edgesValues.items():
            for edge_dest, value in nextEdgeValues.items():

                area_1 = self.GetRegionNameWithID(edge_source)
                area_2 = self.GetRegionNameWithID(edge_dest)

                region_1 = self.areaInfos[area_1]["MajorRegion"]
                region_2 = self.areaInfos[area_2]["MajorRegion"]

                connectionType = self.edgesTypeConnexion[edge_source][edge_dest]

                details = [edge_source, edge_dest, area_1, area_2, region_1, region_2, connectionType, value]

                edgesDetails.append(details)

        return edgesDetails

    # ====================================================================
    # Return a dict of all connectivity (nextNodeName, weight) from a node
    # ====================================================================
    def GetAllConnectivityWithName(self, name: str):

        id_name = self.GetRegionIDWithName(name)

        connectivities = {}
        for edge_dest, value in self.edgesValues[id_name].items():
            nextName = self.GetRegionNameWithID(edge_dest)
            connectivities[nextName] = (value, self.areaInfos[nextName]["RGBA"])

        return connectivities

    # =====================================================
    # Return a dict of sum of all Major Regions from a node
    # =====================================================
    def GetAllMajorRegionsWithName(self, name: str):

        id_name = self.GetRegionIDWithName(name)

        majorRegions = {}
        for edge_dest, edge_value in self.edgesValues[id_name].items():
            
            majorRegion = self.areaInfos[self.GetRegionNameWithID(edge_dest)]["MajorRegion"]
            if majorRegion not in majorRegions:
                majorRegions[majorRegion] = 0.0

            majorRegions[majorRegion] += edge_value

        return majorRegions

    # =======================================================
    # Return a dict of sum of all Connection Type from a node
    # =======================================================
    def GetAllConnectionTypeWithName(self, name: str):

        id_name = self.GetRegionIDWithName(name)

        connectionsType = {"Contralateral": 0.0, "Homotopic": 0.0, "Ipsilateral": 0.0, "Other": 0.0}
        for edge_dest, connectionType in self.edgesTypeConnexion[id_name].items():
            connectionsType[connectionType] += self.edgesValues[id_name][edge_dest]

        return connectionsType
    
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