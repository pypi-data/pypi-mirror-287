import os

import networkx as nx
from scipy.io import loadmat

from src.Model.Data_Storage.ConnGraph_Model import ConnGraph_Infos

class ParserData_Files:

    def __init__(self):

        # File Part
        self.fileName = None
        self.fileType = None  # File Type (.mat / .txt / .flut)
        self.allLines = None

        self.idName = {}  # {ID_Node: Name} -> Matrix Files
        self.areaInfos = {}  # {Name: {ID_Node, RGBA, Side, Wider_Area, ID_Opposite, 3D_Coos} List: [List Order]} -> FLUT File
        self.areasOrder = []  # Order of areas (with blanks)
        self.edgesValues = {}  # {ID_Node: [(ID_Next, Value)]}

        self.numberOfNodes = 0
        self.numberOfEdges = 0

        # Graph Part 
        self.graph = None
        self.connGraph = ConnGraph_Infos()

    # ==================================================
    # Open / Close the File and Start the correct Parser
    # ==================================================
    def LoadFile(self):

        self.graph = nx.Graph()

        # Reset ID_Name association
        self.idName = {}
        
        # Recovert and verify the file extension
        extension = os.path.splitext(self.fileName)[1]

        if extension not in ['.txt', '.mat', '.flut']:
            raise Exception("Wrong Extension Error - Extension not allowed")
        
        # Reset values depending of the extension
        if extension in ['.txt', '.mat']:
            self.edgesValues = {}

        # FLUT File
        elif extension == '.flut':
            self.areaInfos = {}

        # Load the graph from the given file
        try:
            dataFile = open(os.path.abspath(self.fileName), 'r')
        except FileNotFoundError:
            raise Exception("Opening Error - {}".format(self.fileName))

        match extension:
            case '.txt':
                self.ReadTXT(dataFile)

            case '.mat':
                dataFile.close()
                self.fileType = "MatLab File"
                self.ReadMAT()
                
            case '.flut':
                self.fileType = "FLUT File"
                self.ReadFLUT(dataFile)

        dataFile.close()

    # ========================
    # Method to read txt files
    # ========================
    def ReadTXT(self, dataFile):

        self.allLines = dataFile.readlines()

        # Recovert Line / Column Number
        linesNumber = len(self.allLines)

        # Handle Empty File Exception
        if linesNumber == 0:
            dataFile.close()
            raise Exception("Wrong Format Error - Empty Given File")

        columnsNumber = len(self.allLines[0].split())

        try:
            # Determine the File Type
            if linesNumber == 1:
                self.fileType = "Single Line - TXT File"
                self.SingleLineFile_Parser()

            else:
                if columnsNumber == 3:

                    self.fileType = "Triplet - TXT File"
                    self.TripletFile_Parser()

                else:
                    self.fileType = "Matrix - TXT File"
                    self.MatrixFile_Parser()

        except Exception as exception:
            dataFile.close()
            raise Exception(exception.args[0])

    # =========================
    # Method to read flut files
    # =========================
    def ReadFLUT(self, dataFile):

        self.areasOrder = []
        self.allLines = dataFile.readlines()

        # Recovert Line / Column Number
        linesNumber = len(self.allLines)

        # Handle Empty File Exception
        if linesNumber == 0:
            dataFile.close()
            raise Exception("Wrong Format Error - Empty Given File")

        self.FlutFile_Parser()

    # ========================
    # Method to read mat files
    # ========================
    def ReadMAT(self):

        try:
            # Load MatLab File
            loadMatLabFile = loadmat(self.fileName)

            # Name List Parsing
            self.MatLabNameList_Parser(loadMatLabFile["name"][0])

            # Data Matrix Parsing
            self.allLines = loadMatLabFile["connectivity"]
            self.MatLabConnectivityMatrix_Parser()

        except KeyError:
            raise Exception("Wrong Format Error - Variable(s) Inexistance")

    # =================================================================
    # Method to add edges (and nodes) in the graph (code factorisation)
    # =================================================================
    def AddEdgeInGraph (self, idCurrent, idNext, edgeValue):

        # If it is the first appearance of the node 
        if not self.graph.has_node(idCurrent):
            self.graph.add_node(idCurrent)
            self.edgesValues[idCurrent] = []

        if not self.graph.has_node(idNext):
            self.graph.add_node(idNext)
            self.edgesValues[idNext] = []

        self.edgesValues[idCurrent].append((idNext, edgeValue))
        self.edgesValues[idNext].append((idCurrent, edgeValue))

        # Add Weighted Edge to the Graph
        self.graph.add_weighted_edges_from([(idCurrent, idNext, edgeValue)])
        
    # ======================================
    # Method to parse Files with Single Line
    # ======================================
    def SingleLineFile_Parser(self):

        print("\u27A2 Loading Single Line - TXT file")
        raise Exception("Single Line File - TODO")

    # ============================
    # Method to parse Matrix Files
    # ============================
    def MatrixFile_Parser(self):
        print("\u27A2 Loading Matrix - TXT file")

        skipLine = 0

        # In the case of matrix with ID/Name
        if self.allLines[0][0:4] == "data":

            skipLine = 2

            # Conn_Num_line = self.All_Lines[0].split()[2:]
            namesLine = self.allLines[1].replace("data", "").split()
            matrixLength = self.allLines[0].replace("data", "").split()
            lengthLine = len(namesLine)

            # Handle Exception (different number of ID/Name)
            if (len(matrixLength) != lengthLine):
                raise Exception("Wrong Format - Different number of Conn_Num/Name")
            
            # Associate ID (manually) with Name area
            for indexName, name in enumerate(namesLine):
                self.idName[indexName] = name

        else:
            lengthLine = len(self.allLines[0].split())

        self.numberOfNodes = lengthLine

        # Assign manual ID to each area
        idLines = [indexLine for indexLine in range(lengthLine)]

        # For each (other) line in the File
        for indexLine, line in enumerate(self.allLines[skipLine:]):
            
            lineSplit = line.split()[skipLine:]

            for indexElement, element in enumerate(lineSplit[:indexLine]):

                # If the connectivity value isn't NULL
                if float(element) == 0.0:
                    continue
                    
                idCurrent = int(idLines[indexLine])
                idNext = int(idLines[indexElement])
                edgeValue = float(element)

                self.AddEdgeInGraph(idCurrent, idNext, edgeValue)

    # =============================
    # Method to parse Triplet Files
    # =============================
    def TripletFile_Parser(self):
        print("\u27A2 Loading Triplet - TXT file")

        # For each line in the File
        for indexLine, line in enumerate(self.allLines):
            
            lineSplit = line.split()

            if len(lineSplit) != 3:
                raise Exception("Wrong Format - Line {}".format(indexLine))

            idCurrent = int(lineSplit[0])
            idNext = int(lineSplit[1])
            edgeValue = float(lineSplit[2])

            self.AddEdgeInGraph(idCurrent, idNext, edgeValue)

    # =====================================================
    # Method to parse MatLab Connectivity Matrix (in Files)
    # =====================================================
    def MatLabConnectivityMatrix_Parser(self):

        lengthLine = len(self.allLines[0])
        
        if lengthLine != len(self.idName):
            raise Exception ("Wrong Format - Different number of Name/Value")
        
        self.numberOfNodes = lengthLine

        # Assign manual ID to each area
        idLines = [indexLine for indexLine in range(lengthLine)]

        # For each (other) line in the File
        for indexLine, line in enumerate(self.allLines):
            for indexElement, element in enumerate(line[:indexLine]):
                
                # If the connectivity value isn't NULL
                if float(element) == 0.0:
                    continue
                    
                idCurrent = int(idLines[indexLine])
                idNext = int(idLines[indexElement])
                edgeValue = float(element)

                self.AddEdgeInGraph(idCurrent, idNext, edgeValue)

    # =====================================================
    # Method to parse MatLab Name List (in Files)
    # =====================================================
    def MatLabNameList_Parser(self, nameList: list):

        currentIndex = 0
        name = ''
        
        # Using chr() Method
        for value in nameList:
            if value == 10:  # Value 10 is the end of the name

                # Don't add empty Name
                if name != '':
                    self.idName[currentIndex] = str(name)
                    currentIndex += 1
                    name = ''

                continue

            name = name + chr(value)

    # ==========================
    # Method to parse Flut Files
    # ==========================
    def FlutFile_Parser(self):
        print("\u27A2 Loading FLUT file")

        # For each line
        for line in self.allLines:

            lineSplit = line.split()

            nameCurrent = lineSplit[1]
            
            if (int(lineSplit[0]) == 0 or nameCurrent == "xxxx"):

                self.areasOrder.append((nameCurrent, lineSplit[0]))
                continue  # Not Area -> blanc in the graph
            
            # Fill the Area Infos Dictionary
            self.areaInfos[nameCurrent] = {}
            self.areaInfos[nameCurrent]["SumConnectivity"] = int(lineSplit[0])
            self.areaInfos[nameCurrent]["RGBA"] = (int(lineSplit[2]), int(lineSplit[3]), int(lineSplit[4]), float(lineSplit[5]))
            self.areaInfos[nameCurrent]["Side"] = int(lineSplit[6])
            self.areaInfos[nameCurrent]["Wider_Area"] = lineSplit[7]
            self.areaInfos[nameCurrent]["ID_Opposite"] = int(lineSplit[8])
            self.areaInfos[nameCurrent]["3D_Coos"] = (int(lineSplit[9]), int(lineSplit[10]), int(lineSplit[11]))

    # ===========================================================================
    # Based on the File -> create the NetworkX Graph stored in a ConnGraph Object
    # ===========================================================================
    def GraphCreation(self, FileName: str) -> ConnGraph_Infos:
        
        self.fileName = FileName

        print("\u27A2 Loading connectivity Graph (based on the file)")

        # Load the File -> generate Arcs Dictionary
        self.LoadFile()

        print("\u27A2 Loading connectivity Graph Done")

        # Complete the ConnGraph Object 
        if self.fileType == "FLUT File":
            self.connGraph.SetAreaInfos(self.areaInfos)
            self.connGraph.SetAreasOrder(self.areasOrder)

        elif self.fileType in ["Single Line - TXT File", "Triplet - TXT File"]:
            self.connGraph.SetGraph(self.graph)
            self.connGraph.SetEdgesValues(self.edgesValues)

            self.connGraph.SetIDName(self.idName)

            self.connGraph.SetNumberOfNodes(self.graph.number_of_nodes())

        elif self.fileType in ["Matrix - TXT File", "MatLab File"]:
            self.connGraph.SetGraph(self.graph)
            self.connGraph.SetEdgesValues(self.edgesValues)

            self.connGraph.SetIDName(self.idName)
            self.connGraph.SetNumberOfNodes(self.numberOfNodes)

        self.connGraph.SetNumberOfEdges(len(self.edgesValues))

        return self.connGraph, self.fileType

