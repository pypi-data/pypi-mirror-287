import os
import math
import statistics

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QListWidgetItem, QListWidgetItem, QTableWidgetItem, QAbstractItemView, QToolTip
from PyQt5.QtCore import Qt

from src.Model.ImportData_Files import ParserData_Files
from src.Model.ImportName_Files import ParserName_Files
from src.Model.ImportPreviousFiles import ParserPreviousFiles
from src.Model.ExportPreviousFiles import ExportPreviousFiles

from src.Model.Data_Storage.ConnGraph_Model import ConnGraph_Infos
from src.Model.Data_Storage.Filters_Model import Filters_Infos
from src.Model.Data_Storage.Project_Model import Project_Infos

class ImportFile_Controller:
    connGraph: ConnGraph_Infos
    filtre: Filters_Infos
    project: Project_Infos

    def __init__(self, ImportFile_View):

        self.importFile_View = ImportFile_View

        self.parserDataFile = ParserData_Files()
        self.parserNameFile = ParserName_Files()
        self.connGraph = None

        self.threshold = None
        self.filters = Filters_Infos()

        self.project = Project_Infos()

        # Loaded File
        self.flutFile = None
        self.dataFile = None
        self.nameFile = None

        self.previousFiles = {"DataFiles": {}, "NameFiles": {}, "FlutFiles": [], "ConfigFiles": [], "ProjectFiles": []}

        self.graph = None
        self.graphValues = []
        self.minMax = None  # (Min, Max)

        self.valueRound = 4
        self.limitedCurve = None

        # Create all actions used by wingets
        self._ActionCreation()

        # Other Initial Value
        self._OtherInit()

    ##############################
    #       INITIALIZATION
    ##############################

    # ==================================================================
    # Method to create all actions to each winget when the app is opened
    # ==================================================================
    def _ActionCreation(self):

        # Action Creation - Open Data File
        self.OpenDataFile_Qaction = QtWidgets.QAction('ImportDataFile', self.importFile_View)
        self.OpenDataFile_Qaction.triggered.connect(self.OpenDataFile)

        # Action Creation - Open Name File
        self.OpenNameFile_Qaction = QtWidgets.QAction('ImportNameFile', self.importFile_View)
        self.OpenNameFile_Qaction.triggered.connect(self.OpenNameFile)

        # Action Creation - Open Config File
        self.OpenConfigFile_Qaction = QtWidgets.QAction('ImportConfigFile', self.importFile_View)
        self.OpenConfigFile_Qaction.triggered.connect(self.OpenConfigFile)

        # Action Creation - Open Project File
        self.OpenProjectFile_Qaction = QtWidgets.QAction('ImportProjectFile', self.importFile_View)
        self.OpenProjectFile_Qaction.triggered.connect(self.OpenProjectFile)

        # Action Creation - Data/Filter Validation 
        self.Validation_Qaction = QtWidgets.QAction('Validation', self.importFile_View)
        self.Validation_Qaction.triggered.connect(self.Validation)

        # Action when Slider / Spin value change
        self.importFile_View.threshold_Slider.sliderReleased.connect(lambda: self.SliderValue())
        self.importFile_View.thresholdValue_DoubleSpinBox.valueChanged.connect(lambda: self.SpinValue())

        # Action when row in the Table is clicked
        self.importFile_View.percentageTable_TableWidget.itemClicked.connect(self.TablePercentageValue)
        self.importFile_View.nbTable_TableWidget.itemClicked.connect(self.TableNbValue)

    # ================================
    # Method to initialize other value 
    # ================================
    def _OtherInit(self):

        # Widget List Initialization
        try:
            # Previous File Initialization 
            parserPreviousFiles = ParserPreviousFiles()
            self.previousFiles = parserPreviousFiles.LoadFile()

        except Exception as exception:
            print("[ERROR]", exception.args[0])

        # For each File (Data / Flut / Config / Project)
        for dataFile_fullPath, fileType in self.previousFiles["DataFiles"].items():

            # Check if the Data File is associated with a Name File
            if dataFile_fullPath in self.previousFiles["NameFiles"]:

                nameFile = self.previousFiles["NameFiles"][dataFile_fullPath]
                newItem = QListWidgetItem("".join(["\u21A6\t(Data File) ", os.path.basename(dataFile_fullPath), "\n", \
                                                    "\u21AA\t(Name File) ", os.path.basename(nameFile)]))
                newItem.setData(Qt.UserRole, [dataFile_fullPath, nameFile])
                newItem.setToolTip("".join(["\u21A6 (Data File) ", dataFile_fullPath, "\n", \
                                             "\u21AA (Name File) ", nameFile]))

            else:
                newItem = QListWidgetItem("\u21A6\t({}) {}".format(fileType, os.path.basename(dataFile_fullPath)))
                newItem.setData(Qt.UserRole, [dataFile_fullPath])
                newItem.setToolTip("\u21A6 ({}) {}".format(fileType, dataFile_fullPath))

            self.importFile_View.previousDataFiles_List.addItem(newItem)

        for flutFile in self.previousFiles["FlutFiles"]:

            newItem = QListWidgetItem("\u21A6\t{}".format(os.path.basename(flutFile)))
            newItem.setData(Qt.UserRole, flutFile)
            newItem.setToolTip(flutFile)
            self.importFile_View.previousFlutFiles_List.addItem(newItem)

        for configFile in self.previousFiles["ConfigFiles"]:

            newItem = QListWidgetItem("\u21A6\t{}".format(os.path.basename(configFile)))
            newItem.setData(Qt.UserRole, configFile)
            self.importFile_View.previousConfigFile_List.addItem(newItem)

        for projectFile in self.previousFiles["ProjectFiles"]:

            newItem = QListWidgetItem("\u21A6\t{}".format(os.path.basename(projectFile)))
            newItem.setData(Qt.UserRole, projectFile)
            self.importFile_View.previousProjectFile_List.addItem(newItem)

        # Other Initialization
        #self.ImportFile_View.Loading_ProgressBar.setValue(0)
        self.importFile_View.limitedGraph_TabWidget.setCurrentIndex(0)
        self.importFile_View.importFiles_TabWidget.setCurrentIndex(1)

        # Makes All Label in the QListWidget double Clickable
        self.importFile_View.previousDataFiles_List.itemDoubleClicked.connect(self.PreviousDataFile_Click)
        self.importFile_View.previousFlutFiles_List.itemDoubleClicked.connect(self.PreviousFlutFile_Click)

    # =====================================================
    # Method to open a file when the File button is clicked
    # =====================================================
    def OpenDataFile(self):

        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self.importFile_View,
                                                "Open Data File",
                                                "~",
                                                "All Files (*)",
                                                options=options)

        if fileName:
            self.LoadData(fileName)

    # ==========================================================
    # Method to open a file when the Name File button is clicked
    # ==========================================================
    def OpenNameFile(self):

        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self.importFile_View,
                                                "Open Name File",
                                                "~",
                                                "All Files (*)",
                                                options=options)

        if fileName:
            self.LoadName(fileName)

    # =======================================================
    # Method to open a file when the Config button is clicked
    # =======================================================
    def OpenConfigFile(self):

        print("TODO")

    # ========================================================
    # Method to open a file when the Project button is clicked
    # ========================================================
    def OpenProjectFile(self):

        print("TODO")

    # =======================================================================
    # Method to valide filters and Data when the Validation button is clicked
    # =======================================================================
    def Validation(self):
        
        # Handle Data File Missing
        if self.dataFile == None:

            self.importFile_View.errorValidation_Label.show()
            self.importFile_View.errorValidation_Label.setText("Data File Missing")

        # Handle Flut File Missing
        elif self.flutFile == None:

            self.importFile_View.errorValidation_Label.show()
            self.importFile_View.errorValidation_Label.setText("FLUT File Missing")

        # Handle Name File Missing
        elif self.nameFile == None:

            self.importFile_View.errorValidation_Label.show()
            self.importFile_View.errorValidation_Label.setText("Name File Missing")

        elif self.connGraph:

            # Initialize Filters Object
            self.filters.threshold = self.threshold
            self.filters.valueRound = self.valueRound
 
            # Initialize Project Object
            self.project.currentDataFile = self.dataFile
            self.project.currentNameFile = self.nameFile
            self.project.currentFlutFile = self.flutFile

            # Verify the coherence between Data and FLUT Files
            self.CoherenceVerification_NAMEFLUT()

            # If everything is OK, we load the graph object in the MainWindow, then we close this window
            self.importFile_View.parent().mainWindow_controller.LoadDataMainWindow(self.connGraph, self.filters, self.project)
            self.importFile_View.close()

    # =======================================================
    # Method to re-open a Data file when the label is clicked
    # =======================================================
    def PreviousDataFile_Click(self, item: QListWidgetItem):

        # Recovert the full path
        dataItem = item.data(Qt.UserRole)

        # Len = 1 -> Only Data File 
        if len(dataItem) == 1:
            self.LoadData(dataItem[0])

        # Len = 2 -> Data File + Name File
        else:
            self.LoadData(dataItem[0])
            self.LoadName(dataItem[1])

    # =======================================================
    # Method to re-open a Flut file when the label is clicked
    # =======================================================
    def PreviousFlutFile_Click(self, item: QListWidgetItem):

        # Recovert the full path
        self.LoadData(item.data(Qt.UserRole))


    #############################
    #       FILES LOADING
    #############################

    # =======================================
    # Method called when Data File is loading
    # =======================================
    def LoadData(self, fileName: str):

        self.importFile_View.errorFile_Label.hide()

        try:
            # Parser the File
            self.connGraph, fileType = self.parserDataFile.GraphCreation(fileName)

            # Update other element (Last File Opened)
            self.UpdateOpenedDataFlutFile(fileName, fileType)

            # FLUT File
            if fileType == "FLUT File":

                self.flutFile = fileName

                self.UpdatePreviousFlutFiles(fileName)
                self.importFile_View.currentFlutFile_Label.setText(os.path.basename(fileName))

            # TXT / MAT File
            else:

                self.dataFile = fileName
                self.nameFile = None

                # Update Display Label
                self.UpdatePreviousDataFiles(fileName)
                self.importFile_View.currentDataFile_Label.setText(os.path.basename(fileName))

                # Graph Initialization and Display Graph Informations
                self.SetUpGraphValues()
                self.GraphPreparation()
                self.InformationsInitialization()

        except Exception as exception:
            print("[ERROR]", exception.args[0])
            self.importFile_View.errorFile_Label.show()
            self.importFile_View.errorFile_Label.setText(exception.args[0])

    # =======================================
    # Method called when Name File is loading
    # =======================================
    def LoadName(self, fileName: str):

        self.importFile_View.errorFile_Label.hide()

        try:
            self.connGraph.idName = self.parserNameFile.NameFile_Parser(fileName)
            self.CoherenceVerification_NAMEDATA()

            self.nameFile = fileName
            self.previousFiles["NameFiles"][self.dataFile] = self.nameFile

            # Update other element (Last File Opened)
            self.DisplayImportNamePart()
            self.UpdateOpenedNameFile(fileName)

            # Update other element (List File Opened) 
            self.UpdatePreviousNameFiles(fileName)

            # Update other element (Current File Infos) 
            previousFileName_basename = os.path.basename(self.dataFile)
            fileName_basename = os.path.basename(fileName)

            self.importFile_View.currentDataFile_Label.setText("".join([previousFileName_basename, " + ", fileName_basename]))

        except Exception as exception:
            print("[ERROR]", exception.args[0])
            self.importFile_View.errorFile_Label.show()
            self.importFile_View.errorFile_Label.setText(exception.args[0])

    # ==============================================
    # Method called when Data & Name File are loaded
    # ==============================================
    def CoherenceVerification_NAMEDATA(self):

        # Verify the correct relation between the Connectivity Matrix and Names
        if self.connGraph.numberOfNodes != len(self.connGraph.idName):
            raise Exception("Wrong Format - Different Number of Name/Nodes")

    # ==========================================================
    # Method called when Data & Name File + FLUT File are loaded
    # ==========================================================
    def CoherenceVerification_NAMEFLUT(self):

        # Verify the Correlation between Name and Flut (Name and Number of Name)
        if len(self.connGraph.idName) > len(self.connGraph.areaInfos):
            raise Exception("Wrong Format - Different Number of Name")

        # For each Name, compare with Flut Name
        for name in self.connGraph.idName.values():
            if name not in self.connGraph.areaInfos:
                raise Exception("Wrong Format - Name incoherence")

    # =========================================
    # Method called when Config File is loading
    # =========================================
    def LoadConfig(self, configName: str):
        pass

    # ==========================================
    # Method called when Project File is loading
    # ==========================================
    def LoadProject(self, projectName: str):
        pass


    #######################################
    #       INTERFACE INITIALIZATION
    #######################################

    # ==============================================================
    # Fill the Informations Part with the Informations from the File
    # ==============================================================
    def InformationsInitialization(self):

        # Nb Nodes / Connections
        self.importFile_View.nbNodesValue_Label.setText(str(self.connGraph.numberOfNodes))
        self.importFile_View.nbConnectionsValue_Label.setText(str(self.connGraph.numberOfEdges))

        # ABS Mean / ABS Sum
        meanAbs = round(statistics.fmean(map(abs, self.graphValues)), self.valueRound)
        sumAbs = sum(map(abs, self.graphValues))

        self.importFile_View.meanAbsValue_Label.setText(str(meanAbs))
        self.importFile_View.sumAbsValue_Label.setText(str(sumAbs))

        self.importFile_View.minValue_Label.setText(str(self.minMax[0]))
        self.importFile_View.maxValue_Label.setText(str(self.minMax[1]))

        # Standard Deviation
        self.importFile_View.standardDeviationValue_Label.setText(str(round(statistics.stdev(self.graphValues), self.valueRound)))

    # ================================================
    # Method to initialize Graph value and value round
    # ================================================
    def SetUpGraphValues(self):

        self.graphValues = list(self.connGraph.GetAllValues())

        # Min / Max
        self.minMax = (min(self.graphValues, key=abs), max(self.graphValues, key=abs))
        self.threshold = self.minMax[0]

        difference = abs(self.minMax[1]) - abs(self.minMax[0])

    # ====================================================
    # Method to show all informations from the loaded file
    # ====================================================
    def GraphPreparation(self):

        self.importFile_View.graphSection_Widget.show()

        self.DisplayInitialGraph()

        minValue = int(abs(self.minMax[0]))
        maxValue = int(abs(self.minMax[1]))

        # Set up the Spin / Slider Parameters
        self.importFile_View.threshold_Slider.setRange(minValue, maxValue)
        self.importFile_View.threshold_Slider.setValue(minValue)

        minText = f"Min :<span style='font-weight: bold; text-decoration: none;'> {minValue}</span>"
        self.importFile_View.minSlider_Label.setText(minText)

        maxText = f"Max :<span style='font-weight: bold; text-decoration: none;'> {maxValue}</span>"
        self.importFile_View.maxSlider_Label.setText(maxText)

        self.importFile_View.thresholdValue_DoubleSpinBox.setRange(minValue, maxValue)
        self.importFile_View.thresholdValue_DoubleSpinBox.setSingleStep(0.01)
        self.importFile_View.thresholdValue_DoubleSpinBox.setValue(float(minValue))

        # Fill percentage Table 
        self.importFile_View.percentageTable_TableWidget.setRowCount(0)  # Reset Table between File
        self.importFile_View.percentageTable_TableWidget.setColumnCount(2)
        self.importFile_View.percentageTable_TableWidget.setHorizontalHeaderLabels(['Name', 'Mean Value'])
        self.importFile_View.percentageTable_TableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)  # Action when Row clicked
        self.importFile_View.percentageTable_TableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)  # Disable Modification
        self.importFile_View.percentageTable_TableWidget.resizeColumnsToContents()  # Adapte Table Size to Content
        self.importFile_View.percentageTable_TableWidget.verticalHeader().setVisible(False)

        self.PercentageTableLoading()

        # Fill Number Table
        self.importFile_View.nbTable_TableWidget.setRowCount(0)  # Reset Table between File
        self.importFile_View.nbTable_TableWidget.setColumnCount(2)
        self.importFile_View.nbTable_TableWidget.setHorizontalHeaderLabels(['Name', 'Mean Value'])
        self.importFile_View.nbTable_TableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)  # Action when Row clicked
        self.importFile_View.nbTable_TableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)  # Disable Modification
        self.importFile_View.nbTable_TableWidget.resizeColumnsToContents()  # Adapte Table Size to Content
        self.importFile_View.nbTable_TableWidget.verticalHeader().setVisible(False)

        self.NbTableLoading()

    # ============================================
    # Method to load all informations in the table
    # ============================================
    def PercentageTableLoading(self):

        sizeValues = len(self.graphValues)
        sortedValues = sorted(self.graphValues, reverse=True, key=abs)
        absSortedValues = [abs(value) for value in sortedValues]

        # Insert Row in the Table
        self.importFile_View.percentageTable_TableWidget.insertRow(0)
        item1p = QTableWidgetItem("1%")
        item1p.setData(Qt.UserRole, absSortedValues[math.ceil(sizeValues * 0.01) - 1])  # Graph Threshold
        item1p.setTextAlignment(Qt.AlignCenter)
        self.importFile_View.percentageTable_TableWidget.setItem(0, 0, item1p)
        item1fm = QTableWidgetItem(str(round(statistics.fmean(absSortedValues[:math.ceil(sizeValues * 0.01)]), self.valueRound)))
        item1fm.setTextAlignment(Qt.AlignCenter)
        self.importFile_View.percentageTable_TableWidget.setItem(0, 1, item1fm)

        self.importFile_View.percentageTable_TableWidget.insertRow(1)
        item10p = QTableWidgetItem("10%")
        item10p.setData(Qt.UserRole, absSortedValues[math.ceil(sizeValues * 0.1) - 1])  # Graph Threshold
        item10p.setTextAlignment(Qt.AlignCenter)
        self.importFile_View.percentageTable_TableWidget.setItem(1, 0, item10p)
        item10fm = QTableWidgetItem(str(round(statistics.fmean(absSortedValues[:math.ceil(sizeValues * 0.1)]), self.valueRound)))
        item10fm.setTextAlignment(Qt.AlignCenter)
        self.importFile_View.percentageTable_TableWidget.setItem(1, 1, item10fm)

        self.importFile_View.percentageTable_TableWidget.insertRow(2)
        item25p = QTableWidgetItem("25%")
        item25p.setData(Qt.UserRole, absSortedValues[math.ceil(sizeValues * 0.25) - 1])  # Graph Threshold
        item25p.setTextAlignment(Qt.AlignCenter)
        self.importFile_View.percentageTable_TableWidget.setItem(2, 0, item25p)
        item25fm = QTableWidgetItem(str(round(statistics.fmean(absSortedValues[:math.ceil(sizeValues * 0.25)]), self.valueRound)))
        item25fm.setTextAlignment(Qt.AlignCenter)
        self.importFile_View.percentageTable_TableWidget.setItem(2, 1, item25fm)

        self.importFile_View.percentageTable_TableWidget.insertRow(3)
        item50p = QTableWidgetItem("50%")
        item50p.setData(Qt.UserRole, absSortedValues[math.ceil(sizeValues * 0.5) - 1])  # Graph Threshold
        item50p.setTextAlignment(Qt.AlignCenter)
        self.importFile_View.percentageTable_TableWidget.setItem(3, 0, item50p)
        item50fm = QTableWidgetItem(str(round(statistics.fmean(absSortedValues[:math.ceil(sizeValues * 0.5)]), self.valueRound)))
        item50fm.setTextAlignment(Qt.AlignCenter)
        self.importFile_View.percentageTable_TableWidget.setItem(3, 1, item50fm)

        self.importFile_View.percentageTable_TableWidget.insertRow(4)
        item75p = QTableWidgetItem("75%")
        item75p.setData(Qt.UserRole, absSortedValues[math.ceil(sizeValues * 0.75) - 1])  # Graph Threshold
        item75p.setTextAlignment(Qt.AlignCenter)
        self.importFile_View.percentageTable_TableWidget.setItem(4, 0, item75p)
        item75fm = QTableWidgetItem(str(round(statistics.fmean(absSortedValues[:math.ceil(sizeValues * 0.75)]), self.valueRound)))
        item75fm.setTextAlignment(Qt.AlignCenter)
        self.importFile_View.percentageTable_TableWidget.setItem(4, 1, item75fm)

        self.importFile_View.percentageTable_TableWidget.insertRow(5)
        item90p = QTableWidgetItem("90%")
        item90p.setData(Qt.UserRole, absSortedValues[math.ceil(sizeValues * 0.9) - 1])  # Graph Threshold
        item90p.setTextAlignment(Qt.AlignCenter)
        self.importFile_View.percentageTable_TableWidget.setItem(5, 0, item90p)
        item90fm = QTableWidgetItem(str(round(statistics.fmean(absSortedValues[:math.ceil(sizeValues * 0.9)]), self.valueRound)))
        item90fm.setTextAlignment(Qt.AlignCenter)
        self.importFile_View.percentageTable_TableWidget.setItem(5, 1, item90fm)

        self.importFile_View.percentageTable_TableWidget.insertRow(6)
        item95p = QTableWidgetItem("95%")
        item95p.setData(Qt.UserRole, absSortedValues[math.ceil(sizeValues * 0.95) - 1])  # Graph Threshold
        item95p.setTextAlignment(Qt.AlignCenter)
        self.importFile_View.percentageTable_TableWidget.setItem(6, 0, item95p)
        item95fm = QTableWidgetItem(str(round(statistics.fmean(absSortedValues[:math.ceil(sizeValues * 0.95)]), self.valueRound)))
        item95fm.setTextAlignment(Qt.AlignCenter)
        self.importFile_View.percentageTable_TableWidget.setItem(6, 1, item95fm)

    # ============================================
    # Method to load all informations in the table
    # ============================================
    def NbTableLoading(self):

        sizeValues = len(self.graphValues)
        sortedValues = sorted(self.graphValues, reverse=True, key=abs)
        absSortedValues = [abs(value) for value in sortedValues]

        # Insert Row in the Table
        if sizeValues > 10:
            self.importFile_View.nbTable_TableWidget.insertRow(0)
            item10th = QTableWidgetItem("10th")
            item10th.setData(Qt.UserRole, absSortedValues[9])  # Graph Threshold
            item10th.setTextAlignment(Qt.AlignCenter)
            self.importFile_View.nbTable_TableWidget.setItem(0, 0, item10th)
            item10fm = QTableWidgetItem(str(round(statistics.fmean(absSortedValues[:10]), self.valueRound)))
            item10fm.setTextAlignment(Qt.AlignCenter)
            self.importFile_View.nbTable_TableWidget.setItem(0, 1, item10fm)

        if sizeValues > 25:
            self.importFile_View.nbTable_TableWidget.insertRow(1)
            item25th = QTableWidgetItem("25th")
            item25th.setData(Qt.UserRole, absSortedValues[24])  # Graph Threshold
            item25th.setTextAlignment(Qt.AlignCenter)
            self.importFile_View.nbTable_TableWidget.setItem(1, 0, item25th)
            item25fm = QTableWidgetItem(str(round(statistics.fmean(absSortedValues[:25]), self.valueRound)))
            item25fm.setTextAlignment(Qt.AlignCenter)
            self.importFile_View.nbTable_TableWidget.setItem(1, 1, item25fm)

        if sizeValues > 50:
            self.importFile_View.nbTable_TableWidget.insertRow(2)
            item50th = QTableWidgetItem("50th")
            item50th.setData(Qt.UserRole, absSortedValues[49])  # Graph Threshold
            item50th.setTextAlignment(Qt.AlignCenter)
            self.importFile_View.nbTable_TableWidget.setItem(2, 0, item50th)
            item50fm = QTableWidgetItem(str(round(statistics.fmean(absSortedValues[:50]), self.valueRound)))
            item50fm.setTextAlignment(Qt.AlignCenter)
            self.importFile_View.nbTable_TableWidget.setItem(2, 1, item50fm)

        if sizeValues > 100:
            self.importFile_View.nbTable_TableWidget.insertRow(3)
            item100th = QTableWidgetItem("100th")
            item100th.setData(Qt.UserRole, absSortedValues[99])  # Graph Threshold
            item100th.setTextAlignment(Qt.AlignCenter)
            self.importFile_View.nbTable_TableWidget.setItem(3, 0, item100th)
            item100fm = QTableWidgetItem(str(round(statistics.fmean(absSortedValues[:100]), self.valueRound)))
            item100fm.setTextAlignment(Qt.AlignCenter)
            self.importFile_View.nbTable_TableWidget.setItem(3, 1, item100fm)

        if sizeValues > 200:
            self.importFile_View.nbTable_TableWidget.insertRow(4)
            item200th = QTableWidgetItem("200th")
            item200th.setData(Qt.UserRole, absSortedValues[199])  # Graph Threshold
            item200th.setTextAlignment(Qt.AlignCenter)
            self.importFile_View.nbTable_TableWidget.setItem(4, 0, item200th)
            item200fm = QTableWidgetItem(str(round(statistics.fmean(absSortedValues[:200]), self.valueRound)))
            item200fm.setTextAlignment(Qt.AlignCenter)
            self.importFile_View.nbTable_TableWidget.setItem(4, 1, item200fm)

        if sizeValues > 300:
            self.importFile_View.nbTable_TableWidget.insertRow(5)
            item300th = QTableWidgetItem("300th")
            item300th.setData(Qt.UserRole, absSortedValues[299])  # Graph Threshold
            item300th.setTextAlignment(Qt.AlignCenter)
            self.importFile_View.nbTable_TableWidget.setItem(5, 0, item300th)
            item300fm = QTableWidgetItem(str(round(statistics.fmean(absSortedValues[:300]), self.valueRound)))
            item300fm.setTextAlignment(Qt.AlignCenter)
            self.importFile_View.nbTable_TableWidget.setItem(5, 1, item300fm)

        if sizeValues > 400:
            self.importFile_View.nbTable_TableWidget.insertRow(6)
            item400th = QTableWidgetItem("400th")
            item400th.setData(Qt.UserRole, absSortedValues[399])  # Graph Threshold
            item400th.setTextAlignment(Qt.AlignCenter)
            self.importFile_View.nbTable_TableWidget.setItem(6, 0, item400th)
            item400fm = QTableWidgetItem(str(round(statistics.fmean(absSortedValues[:400]), self.valueRound)))
            item400fm.setTextAlignment(Qt.AlignCenter)
            self.importFile_View.nbTable_TableWidget.setItem(6, 1, item400fm)

        if sizeValues > 500:
            self.importFile_View.nbTable_TableWidget.insertRow(7)
            item500th = QTableWidgetItem("500th")
            item500th.setData(Qt.UserRole, absSortedValues[499])  # Graph Threshold
            item500th.setTextAlignment(Qt.AlignCenter)
            self.importFile_View.nbTable_TableWidget.setItem(7, 0, item500th)
            item500fm = QTableWidgetItem(str(round(statistics.fmean(absSortedValues[:500]), self.valueRound)))
            item500fm.setTextAlignment(Qt.AlignCenter)
            self.importFile_View.nbTable_TableWidget.setItem(7, 1, item500fm)


    #################################
    #       INTERFACE ACTIONS
    #################################

    # =============================================================
    # Modify the Data FileName Label by the name of the Opened File
    # =============================================================
    def UpdateOpenedDataFlutFile(self, fileName: str, fileType: str):

        fileName_basename = os.path.basename(fileName)

        if fileType == "FLUT File":
            self.importFile_View.openedDataFlutFile_Label.setText("Opened FLUT File : {}".format(fileName_basename))

        else:
            self.importFile_View.openedDataFlutFile_Label.setText("Opened Data File : {}".format(fileName_basename))

    # =============================================================
    # Modify the Name FileName Label by the name of the Opened File
    # =============================================================
    def UpdateOpenedNameFile(self, fileName: str):

        fileName_basename = os.path.basename(fileName)
        self.importFile_View.openedNameFile_Label.setText("Opened Name File : {}".format(fileName_basename))

    # ==========================================================
    # Modify / Fill the List by the name of the Opened Data File
    # ==========================================================
    def UpdatePreviousDataFiles(self, fileName: str):

        secondaryFileType = None

        # Hide or Display Name File Part if the Data File doesn't associate name with value
        if not self.connGraph.idName:
            self.DisplayImportNamePart()
            secondaryFileType = "DataFile"
        else:
            self.HideImportNamePart()
            secondaryFileType = "DataNameFile"
            self.nameFile = False  # Don't need Name File

        # Check if the File isn't already in the list
        if fileName not in self.previousFiles["DataFiles"]:

            if len(self.previousFiles["DataFiles"]) == 5:
                firstItem = self.importFile_View.previousDataFiles_List.item(0)
                del self.previousFiles["DataFiles"][firstItem.data(Qt.UserRole)[0]]
                self.importFile_View.previousDataFiles_List.takeItem(self.importFile_View.previousDataFiles_List.row(firstItem))

            fileName_basename = os.path.basename(fileName)
            self.previousFiles["DataFiles"][fileName] = secondaryFileType

            # Add the new File
            newItem = QListWidgetItem("\u21A6\t({}) {}".format(secondaryFileType, fileName_basename))
            newItem.setData(Qt.UserRole, [fileName])
            newItem.setToolTip("\u21A6 ({}) {}".format(secondaryFileType, fileName))
            self.importFile_View.previousDataFiles_List.addItem(newItem)

    # =====================================================
    # Find and Modify the FileName Label (with + Name File)
    # =====================================================
    def UpdatePreviousNameFiles(self, fileName: str):

        # Iterate through all items in the QListWidget
        for index in range(self.importFile_View.previousDataFiles_List.count()):

            # Get the item at the current index
            itemDataList = self.importFile_View.previousDataFiles_List.item(index)

            # Check if the item data matches the data_to_find
            if itemDataList.data(Qt.UserRole)[0] == self.dataFile:

                previousFileName_basename = os.path.basename(self.dataFile)
                fileName_basename = os.path.basename(fileName)

                itemDataList.setText("".join(["\u21A6\t(Data File) ", previousFileName_basename, "\n", \
                                      "\u21AA\t(Name File) ", fileName_basename]))
                itemDataList.setData(Qt.UserRole, [self.dataFile, fileName])
                itemDataList.setToolTip("".join(["\u21A6 (Data File) ", self.dataFile, "\n", \
                                         "\u21AA (Name File) ", fileName]))

    # ==========================================================
    # Modify / Fill the List by the name of the Opened Flut File
    # ==========================================================
    def UpdatePreviousFlutFiles(self, fileName: str):

        # Check if the File isn't already in the list
        if fileName not in self.previousFiles["FlutFiles"]:

            if len(self.previousFiles["FlutFiles"]) == 5:
                firstItem = self.importFile_View.previousFlutFiles_List.item(0)
                del self.previousFiles["FlutFiles"][firstItem.data(Qt.UserRole)]
                self.importFile_View.previousFlutFiles_List.takeItem(self.importFile_View.previousFlutFiles_List.row(firstItem))

            # Add the new File
            newItem = QListWidgetItem("\u21A6\t{}".format(os.path.basename(fileName)))
            newItem.setData(Qt.UserRole, fileName)
            self.importFile_View.previousFlutFiles_List.addItem(newItem)
            self.previousFiles["FlutFiles"].append(fileName)

    # =============================
    # Display Import Name File Part
    # =============================
    def DisplayImportNamePart(self):

        self.importFile_View.openedNameFile_Label.setText("")
        self.importFile_View.openedNameFile_Label.show()
        self.importFile_View.importNameFile_Button.show()

    # ==========================
    # Hide Import Name File Part
    # ==========================
    def HideImportNamePart(self):

        self.importFile_View.openedNameFile_Label.hide()
        self.importFile_View.importNameFile_Button.hide()

    # =========================================================
    # Method to recovert the value when the Slider value change
    # =========================================================
    def SliderValue (self):

        sliderValue = self.importFile_View.threshold_Slider.value()

        # Return the minimal value instead of compute the logarithm value
        if sliderValue == self.minMax[0]:
            logValue = self.minMax[0]
        else:
            # Change the value in logarithm scale
            logValue = abs(self.minMax[0]) * (abs(self.minMax[1]) / abs(self.minMax[0])) \
                        ** (sliderValue / (abs(self.minMax[1]) - abs(self.minMax[0])))
            
        self.importFile_View.thresholdValue_DoubleSpinBox.blockSignals(True)
        self.importFile_View.thresholdValue_DoubleSpinBox.setValue(logValue)
        self.importFile_View.thresholdValue_DoubleSpinBox.blockSignals(False)

        # Update Threshold (Filters)
        self.threshold = logValue

        # Update Graph
        self.UpdateGraph(logValue)

    # ========================================================
    # Method to recovert the value when the SpinBox is changed
    # ========================================================
    def SpinValue(self):

        spinValue = self.importFile_View.thresholdValue_DoubleSpinBox.value()

        logValueInversed = (abs(self.minMax[1]) - abs(self.minMax[0])) \
                    * (math.log(spinValue / abs(self.minMax[0])) / math.log(abs(self.minMax[1]) / abs(self.minMax[0])))
        self.importFile_View.threshold_Slider.setValue(int(logValueInversed))

        # Update Threshold (Filters)
        self.threshold = spinValue

        # Update Graph
        self.UpdateGraph(spinValue)

    # =================================================================
    # Method to recovert the value when a row from the table is clicked
    # =================================================================
    def TablePercentageValue(self, item: QTableWidgetItem):

        self.importFile_View.nbTable_TableWidget.clearSelection()
        row = item.row()

        # Update Threshold (Filters)
        percentageValue = float(self.importFile_View.percentageTable_TableWidget.item(row, 0).data(Qt.UserRole))
        self.threshold = percentageValue

        # Update Graph 
        self.UpdateGraph(percentageValue)

    # =================================================================
    # Method to recovert the value when a row from the table is clicked
    # =================================================================
    def TableNbValue(self, item: QTableWidgetItem):

        self.importFile_View.percentageTable_TableWidget.clearSelection()
        row = item.row()

        # Update Threshold (Filters)
        nbValue = float(self.importFile_View.nbTable_TableWidget.item(row, 0).data(Qt.UserRole))
        self.threshold = nbValue

        # Update Graph 
        self.UpdateGraph(nbValue)

    # ====================================
    # Based on the File, display the Graph
    # ====================================
    def DisplayInitialGraph(self):

        # Clear the previous plot and Create a new one
        self.importFile_View.graph.clear()
        self.graph = self.importFile_View.graph.add_subplot(111)

        # Sort Values -> Initial value
        positiveValues = [value for value in self.graphValues if value > 0]
        negativeValues = [value for value in self.graphValues if value < 0]

        sortedValues = sorted(negativeValues, reverse=True) + sorted(positiveValues, reverse=True)

        x_coords = list(range(len(sortedValues)))
        y_coords = [abs(val) for val in sortedValues]

        self.graph.plot(x_coords, y_coords, label='Initial Curve')

        # Limited plot (initially empty)
        self.limitedCurve, = self.graph.plot([], [], label='Limited Curve')

        # Set the y-axis to logarithmic scale
        self.graph.set_yscale('log')

        # Add title and labels
        self.graph.set_title('Values in Curve', fontsize=20)
        self.graph.set_xlabel('Value', fontsize=15)
        self.graph.set_ylabel('Absolute Value', fontsize=15)

        # Remove x-tick labels
        self.graph.set_xticks([])
        self.graph.set_xticklabels([])

        self.graph.tick_params(axis='y', which='major', labelsize=15)
        self.graph.legend(fontsize=15)

        # Draw the canvas
        self.importFile_View.canvas.draw()

    # ====================================
    # Based on the value, update the Graph
    # ====================================
    def UpdateGraph(self, newValue: float):

        # Update the limited curve data
        if newValue == abs(min(self.graphValues, key=abs)):

            # Limited plot (equal to initial Curve)
            self.limitedCurve.set_data([], [])

        else:
            positiveValuesLimited = [value for value in self.graphValues if value > 0]
            negativeValuesLimited = [value for value in self.graphValues if value < 0]

            sortedValuesLimited = sorted(negativeValuesLimited, reverse=True) + sorted(positiveValuesLimited, reverse=True)

            x_coordsLimited = list(range(len(sortedValuesLimited)))
            y_coordsLimited = [abs(value) if abs(value) > newValue - 1 else None for value in sortedValuesLimited]

            self.limitedCurve.set_data(x_coordsLimited, y_coordsLimited)

        # Update the canvas
        self.graph.relim()
        self.graph.autoscale_view()
        self.importFile_View.canvas.draw()

    #################################
    #       INTERFACE CLOSING
    #################################

    # =======================================
    # Method called when the window is closed
    # =======================================
    def SaveData(self):

        # Save Previous Files
        exportPreviousFiles = ExportPreviousFiles()
        exportPreviousFiles.SaveFile(self.previousFiles)
