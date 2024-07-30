import os
import statistics
from pathlib import Path

import numpy as np
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMenu, QAction, QTableWidgetItem

from src.Model.Data_Storage.ConnGraph_Model import ConnGraph_Infos
from src.Model.Data_Storage.Filters_Model import Filters_Infos
from src.Model.Data_Storage.Project_Model import Project_Infos

from src.View.CustomWidgets.ConnGraphic_Widget import ConnGraphic_Widget
from src.View.CustomWidgets.FlowLayout_Layout import FlowLayout
from src.View.CustomWidgets.Graphic_Widget import GraphicWidget
from src.View.ImportFile_View import ImportFile_View


class MainWindow_Controller:
    graph_curve: ConnGraph_Infos
    filtre: Filters_Infos
    project: Project_Infos

    def __init__(self, mainWindow_view):

        self.mainWindow_view = mainWindow_view
        #self.mainWindow_view.resized.connect(self.on_resize)

        self.projectOpened = False

        self.connGraph = None
        self.filters = None
        self.project = None

        # File Infos Part
        self.graph_curve = None
        self.limitedCurve = None

        # Pie Part
        self.displayedPies = []

        self._InitActions()
        self._InitFilter()
        self._InitOther()

    def _InitActions(self):

        # ToolBar actions
        createProject_action = QAction("Create new project", self.mainWindow_view.menuBar)
        openProject_action = QAction("Open existing project", self.mainWindow_view.menuBar)
        closeProject_action = QAction("Close project", self.mainWindow_view.menuBar)
        help_action = QAction("Help", self.mainWindow_view.menuBar)
        about_action = QAction("About", self.mainWindow_view.menuBar)
        test_action = QAction("Test button", self.mainWindow_view.menuBar)

        createProject_action.triggered.connect(self.CreateNewProject_ToolBarFunction)
        openProject_action.triggered.connect(self.OpenExistingProject_ToolBarFunction)
        closeProject_action.triggered.connect(self.CloseProject_ToolBarFunction)
        help_action.triggered.connect(self.Help_ToolBarFunction)
        about_action.triggered.connect(self.About_ToolBarFunction)
        test_action.triggered.connect(self.TestFunction_ToolBarFunction)

        #TODO : move it into the graphic_view

        # & define a quick key to jump to this menu by pressing alt+F
        self.mainWindow_view.file_toolBarMenu = self.mainWindow_view.menuBar.addMenu("&Files")
        self.mainWindow_view.file_toolBarMenu.addActions([
            createProject_action,
            openProject_action,
            closeProject_action
        ])

        self.mainWindow_view.help_toolBarAction = self.mainWindow_view.menuBar.addAction(help_action)
        self.mainWindow_view.about_toolBarAction = self.mainWindow_view.menuBar.addAction(about_action)
        self.mainWindow_view.test_toolBarAction = self.mainWindow_view.menuBar.addAction(test_action)

        # Action triggered when tab is changed in tabWidget
        self.mainWindow_view.mainTabWidget.currentChanged.connect(self.TabWidgetIndexChanged)

    def _InitFilter(self):
        if self.connGraph is None:
            # Set value for weight and conn infos labels
            weightSum = 0
            weightMean = 0
            connectionNumber = 0
        else:
            # TODO : mettre les bonnes valeurs
            weightSum = self.connGraph.numberOfNodes
            weightMean = 0
            connectionNumber = self.connGraph.numberOfNodes

        self.mainWindow_view.weightSumValue_label.setText(f"{weightSum}")
        self.mainWindow_view.weightMeanValue_label.setText("%.2f" % weightMean)
        self.mainWindow_view.connNumValue_label.setText(f"{connectionNumber}")
    
    def _InitOther(self):
        
        self._InitPie()
        self._InitList()
        
    # --------- Menu bar actions ---------

    def CreateNewProject_ToolBarFunction(self):
        self.RemoveDataMainWindow()
        print("Create new project...")
        self.OpenImportWindows_ToolBarFunction()

    def OpenExistingProject_ToolBarFunction(self):
        self.RemoveDataMainWindow()

        print("Open existing project...")
        self.OpenImportWindows_ToolBarFunction()

    def CloseProject_ToolBarFunction(self):
        print("Close project...")

        self.projectOpened = False
        self.HideItems()
        self.RemoveDataMainWindow()

    def Help_ToolBarFunction(self):
        print("Help...")

    def About_ToolBarFunction(self):
        print("About...")

    def PrintAllGraphData_TempFunction(self):
        print("nx_graph :   ", self.connGraph.nxGraph)
        print("dict_graph : ", self.connGraph.dictGraph)
        print("id_name :    ", self.connGraph.idName)
        print("area_info :  ", self.connGraph.areaInfos)
        print("edges_val :  ", self.connGraph.edgesValues)
        print("num_nodes :  ", self.connGraph.numberOfNodes)
        print("num_edges :  ", self.connGraph.numberOfEdges)
        print("adjacency :  ", self.connGraph.adjacencyMatrix)
        print("degree :     ", self.connGraph.degree)
        infos = self.connGraph.GetEdgesDetails()
        print(infos)

    # ---------- Interface Initialization ----------

    def TabWidgetIndexChanged(self, tabIndex: int):

        # Hide the dock widget for the "FileInfo" tab only
        if tabIndex == 0:
            self.mainWindow_view.dockWidget.hide()
        else:
            self.mainWindow_view.dockWidget.show()

    def OpenImportWindows_ToolBarFunction(self):
        ImportFileWindow = ImportFile_View(parent=self.mainWindow_view)
        ImportFileWindow.show()

        resourcedir = Path(__file__).parent.parent.parent / 'resources'
        with open(os.path.join(resourcedir, "Style_Application.qss"), 'r') as file:
            stylesheet = file.read()
            ImportFileWindow.setStyleSheet(stylesheet)

    def TestFunction_ToolBarFunction(self):
        self.RemoveDataMainWindow()
        print("Test function call :")
        self.OpenImportWindows_ToolBarFunction()

    # ---------- Interface Update ----------

    def LoadDataMainWindow(self, connGraph: ConnGraph_Infos, filters: Filters_Infos, project: Project_Infos):

        self.projectOpened = True
    
        self.connGraph = connGraph
        self.filters = filters
        self.project = project

        self.ShowItems()

        self.UpdateFileInfo()
        self.UpdateGraph()
        self.UpdatePie()
        self.UpdateList()
        self.UpdateGT()

    def RemoveDataMainWindow(self):

        # ==== Graph Part ====
        layout = self.mainWindow_view.circularPlot_widget.layout()

        if layout.count() != 0:
            item = self.mainWindow_view.circularPlot_widget.layout().takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            else:
                layout.removeItem(item)

        # ==== Pie Part ====
        
        # Clear the FlowLayout
        self.mainWindow_view.region_scroll_layout.clear()
        self.mainWindow_view.region_menu.clear()
        self.displayedPies = []

        # ==== List Part ====

        # Clear the tableWidget before inserting data
        self.mainWindow_view.infoList_tableWidget.setRowCount(0)

    def HideItems(self):

        # Tab1 : File Infos
        self.mainWindow_view.fileInfosSupport_Frame.hide()
        self.mainWindow_view.noInfoTab1_Label.show()

        # Tab2 : Graph Circular
        self.mainWindow_view.circularPlot_widget.hide()
        self.mainWindow_view.noInfoTab2_Label.show()

        # Tab3 : Pie
        self.mainWindow_view.pieTabWidget.hide()
        self.mainWindow_view.noInfoTab3_Label.show()

        # Tab4 : List
        self.mainWindow_view.infoList_tableWidget.hide()
        self.mainWindow_view.noInfoTab4_Label.show()

        # Tab5 : GT
        self.mainWindow_view.noInfoTab5_Label.show()

    def ShowItems(self):

        # Tab1 : File Infos
        self.mainWindow_view.fileInfosSupport_Frame.show()
        self.mainWindow_view.noInfoTab1_Label.hide()

        # Tab2 : Graph Circular
        self.mainWindow_view.circularPlot_widget.show()
        self.mainWindow_view.noInfoTab2_Label.hide()

        # Tab3 : Pie
        self.mainWindow_view.pieTabWidget.show()
        self.mainWindow_view.noInfoTab3_Label.hide()

        # Tab4 : List
        self.mainWindow_view.infoList_tableWidget.show()
        self.mainWindow_view.noInfoTab4_Label.hide()

        # Tab5 : GT
        self.mainWindow_view.noInfoTab5_Label.hide()

    # =========================
    #       Tab File Info
    # =========================
    def UpdateFileInfo(self):
        
        self.InformationsInitialization()
        self.DisplayInitialGraphCurves()
        self.UpdateGraphCurves(self.filters.threshold)

    def InformationsInitialization(self):

        if self.project.currentNameFile:
            self.mainWindow_view.currentDataFile_Label.setText("".join([os.path.basename(self.project.currentDataFile), " + ", os.path.basename(self.project.currentNameFile)]))
        else:
            self.mainWindow_view.currentDataFile_Label.setText(os.path.basename(self.project.currentDataFile))

        self.mainWindow_view.currentFlutFile_Label.setText(os.path.basename(self.project.currentFlutFile))

        graphCurveValues = self.connGraph.edgesValues_withoutDuplicata.values()

        # Nb Nodes / Connections
        self.mainWindow_view.nbNodesValue_Label.setText(str(self.connGraph.numberOfNodes))
        self.mainWindow_view.nbConnectionsValue_Label.setText(str(self.connGraph.numberOfEdges))

        # ABS Mean / ABS Sum
        meanAbs = round(statistics.fmean(map(abs, graphCurveValues)), self.filters.valueRound)
        sumAbs = sum(map(abs, graphCurveValues))

        self.mainWindow_view.meanAbsValue_Label.setText(str(meanAbs))
        self.mainWindow_view.sumAbsValue_Label.setText(str(sumAbs))

        minMax = (min(graphCurveValues, key=abs), max(graphCurveValues, key=abs))
        self.mainWindow_view.minValue_Label.setText(str(minMax[0]))
        self.mainWindow_view.maxValue_Label.setText(str(minMax[1]))

        # Standard Deviation
        self.mainWindow_view.standardDeviationValue_Label.setText(str(round(statistics.stdev(graphCurveValues), self.filters.valueRound)))

        # Threshold
        self.mainWindow_view.thresholdValue_Label.setText(str(self.filters.threshold))

    def DisplayInitialGraphCurves(self):

        # Clear the previous plot and Create a new one
        self.mainWindow_view.graph_curve.clear()
        self.graph_curve = self.mainWindow_view.graph_curve.add_subplot(111)

        graphCurveValues = self.connGraph.edgesValues_withoutDuplicata.values()

        # Sort Values -> Initial value
        positiveValues = [value for value in graphCurveValues if value > 0]
        negativeValues = [value for value in graphCurveValues if value < 0]

        sortedValues = sorted(negativeValues, reverse=True) + sorted(positiveValues, reverse=True)

        x_coords = list(range(len(sortedValues)))
        y_coords = [abs(val) for val in sortedValues]

        self.graph_curve.plot(x_coords, y_coords, label='Initial Curve')

        # Limited plot (initially empty)
        self.limitedCurve, = self.graph_curve.plot([], [], label='Limited Curve')

        # Set the y-axis to logarithmic scale
        self.graph_curve.set_yscale('log')

        # Add title and labels
        self.graph_curve.set_title('Values in Curve', fontsize=20)
        self.graph_curve.set_xlabel('Value', fontsize=15)
        self.graph_curve.set_ylabel('Absolute Value', fontsize=15)

        # Remove x-tick labels
        self.graph_curve.set_xticks([])
        self.graph_curve.set_xticklabels([])

        self.graph_curve.tick_params(axis='y', which='major', labelsize=15)
        self.graph_curve.legend(fontsize=15)

        # Draw the canvas
        self.mainWindow_view.canvas.draw()

    def UpdateGraphCurves(self, newValue: float):
        
        graphCurveValues = self.connGraph.edgesValues_withoutDuplicata.values()

        # Update the limited curve data
        if newValue == abs(min(graphCurveValues, key=abs)):

            # Limited plot (equal to initial Curve)
            self.limitedCurve.set_data([], [])

        else:

            positiveValuesLimited = [value for value in graphCurveValues if value > 0]
            negativeValuesLimited = [value for value in graphCurveValues if value < 0]

            sortedValuesLimited = sorted(negativeValuesLimited, reverse=True) + sorted(positiveValuesLimited, reverse=True)

            x_coordsLimited = list(range(len(sortedValuesLimited)))
            y_coordsLimited = [abs(value) if abs(value) > newValue - 1 else None for value in sortedValuesLimited]

            self.limitedCurve.set_data(x_coordsLimited, y_coordsLimited)

        # Update the canvas
        self.graph_curve.relim()
        self.graph_curve.autoscale_view()
        self.mainWindow_view.canvas.draw()


    # =========================
    #       Tab Graph
    # =========================
    def UpdateGraph(self):
        print("Loading graph...")
        
        self.PrintAllGraphData_TempFunction()

        # Create graph widget
        self.connGraph_widget = ConnGraphic_Widget(self.connGraph.numberOfNodes, 700, 700)

        # Add it to the graphic_view
        self.mainWindow_view.circularPlot_widget.layout().addWidget(self.connGraph_widget)


    # =========================
    #       Tab Pie
    # =========================

    def _InitPie(self):
        # Init a flow layout to enhance the scroll area
        self.mainWindow_view.region_scroll_layout = FlowLayout(self.mainWindow_view.regionScrollContent)
        self.mainWindow_view.regionScrollContent.setContentsMargins(10, 10, 10, 10)

        # Create context menu for the "add graphic" button
        self.mainWindow_view.region_menu = QMenu(self.mainWindow_view, triggered=self.AddGraphic_PieTab)

    def UpdatePie(self):

        # Build menu with each region name
        for regionName in self.connGraph.GetAllNameWithConnectivity():
            self.mainWindow_view.region_menu.addAction(QAction(regionName, self.mainWindow_view.region_menu))

        self.mainWindow_view.addGraphic_button.setMenu(self.mainWindow_view.region_menu)

    def AddGraphic_PieTab(self, action: QAction):
        print("add graphic")

        connectivities = self.connGraph.GetAllConnectivityWithName(action.text())

        if action is not None and action.text() not in self.displayedPies:
            self.displayedPies.append(action.text())
            graphic_widget = GraphicWidget(action.text(), connectivities)
            self.mainWindow_view.region_scroll_layout.addWidget(graphic_widget)

            #self.on_resize()

    """def on_resize(self):

        layout_size = self.mainWindow_view.regionScrollContent.size()
        for indexWidget in range(self.mainWindow_view.region_scroll_layout.count()):
 
            widget = self.mainWindow_view.region_scroll_layout.itemAt(indexWidget).widget()
            if isinstance(widget, GraphicWidget):
                new_width = int(layout_size.width() / 2) - 20
                new_height = int(layout_size.height() / 2) - 20
                widget.setFixedSize(new_width, new_height)
    """


    # =========================
    #       Tab List
    # =========================

    def _InitList(self):

        # Hide vertical header of the list
        self.mainWindow_view.infoList_tableWidget.verticalHeader().setVisible(False)

        # Disable cell editing and column resizing by user
        self.mainWindow_view.infoList_tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.mainWindow_view.infoList_tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)

        # Set sorting based on the first column
        self.mainWindow_view.infoList_tableWidget.setSortingEnabled(True)
    
    def UpdateList(self):

        # Build a list of edges with each information needed
        edges = np.array(self.connGraph.GetEdgesDetails())

        # Prepare formatting for int/float values in the tableWidget
        intMax = max(np.concatenate((edges[:, 0], edges[:, 1])))
        intFormat = "{:" + str(intMax) + "d}"
        floatFormat = "{:10.2f}"

        # Create each row with edges info
        for edge in edges:

            # Put the cursor on the last row, then insert a new empty row in the tableWidget
            row = self.mainWindow_view.infoList_tableWidget.rowCount()
            self.mainWindow_view.infoList_tableWidget.insertRow(row)

            # Create table item for the row
            # Note : It is important to not convert int values into str() values without .format
            #        otherwise sorting will not work properly for these values
            node1 = QTableWidgetItem(intFormat.format(int(edge[0])))
            node2 = QTableWidgetItem(intFormat.format(int(edge[1])))
            region1 = QTableWidgetItem(str(edge[2]))
            region2 = QTableWidgetItem(str(edge[3]))
            connType = QTableWidgetItem(str(edge[4]))
            value = QTableWidgetItem(floatFormat.format(float(edge[5])))

            # Set each row item
            self.mainWindow_view.infoList_tableWidget.setItem(row, 0, node1)
            self.mainWindow_view.infoList_tableWidget.setItem(row, 1, node2)
            self.mainWindow_view.infoList_tableWidget.setItem(row, 2, region1)
            self.mainWindow_view.infoList_tableWidget.setItem(row, 3, region2)
            self.mainWindow_view.infoList_tableWidget.setItem(row, 4, connType)
            self.mainWindow_view.infoList_tableWidget.setItem(row, 5, value)

        self.mainWindow_view.infoList_tableWidget.resizeColumnsToContents()

    # =========================
    #       Tab GT
    # =========================

    def UpdateGT(self):
        pass







