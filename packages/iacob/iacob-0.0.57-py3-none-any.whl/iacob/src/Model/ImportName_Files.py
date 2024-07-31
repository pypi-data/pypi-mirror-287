import os

from src.Model.Data_Storage.ConnGraph_Model import ConnGraph_Infos

class ParserName_Files:
    def __init__(self):
        
        # File Part
        self.fileName = None

        self.allLines = None

        self.idName = {}  # {ID_Node: Name}
        self.connGraph = ConnGraph_Infos

    # ============================
    # Open - Read - Close the File
    # ============================
    def LoadFile(self):

        # Load the graph from the given file
        try:
            dataFile = open(os.path.abspath(self.fileName), 'r')
        except FileNotFoundError:
            raise Exception("Opening Error - {}".format(self.fileName))
        
        self.allLines = dataFile.readlines()
        
        dataFile.close()

    # ==========================
    # Method to parse Name Files
    # ==========================
    def NameFile_Parser(self, fileName):
        
        self.fileName = fileName

        # Recovert and verify the file extension
        extension = os.path.splitext(self.fileName)[1]

        if extension != ".txt":
            raise Exception("Wrong Extension Error - Extension not allowed")

        # Load and Recovert All Lines from the File
        self.LoadFile()

        if len(self.allLines) != 1:
            raise Exception("Wrong Format - Only 1 line with Name is require")
        
        indexName = 0

        # Stock all Name with an abitratry ID
        for name in self.allLines[0].split():

            self.idName[indexName] = name
            indexName += 1

        return self.idName