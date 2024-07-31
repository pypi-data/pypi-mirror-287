import csv

import numpy as np
import colorsys

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget, QFileDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from src.View.ui.GraphWidget_ui import Ui_GraphWidget


class GraphicWidget(QWidget):

    def __init__(self, mainWindow_Controller, name, data, graphicType):
        super().__init__()

        # Setup widget UI
        self.graphWidget_ui = Ui_GraphWidget()
        self.graphWidget_ui.setupUi(self)

        self.mainWindow_Controller = mainWindow_Controller

        self.name = name
        self.data = data

        self.plot = None
        self.graphWidget_ui.title_label.setText(name)
        
        # Separate each graphic Type
        match graphicType:

            case "Connections":
                self._InitConnectionsPie()

            case "MajorRegions":
                self._InitMajorRegionsPie()

            case "MajorRegionsBar":
                self._InitMajorRegionsBar()

            case "ConnectionType":
                self._InitConnectionTypePie()

            case "ConnectionTypeBar":
                self._InitConnectionTypeBar()

        self.graphWidget_ui.closeButton.clicked.connect(self.CloseWindow)
        self.graphWidget_ui.toCsv_button.clicked.connect(self.ExportToCsv)
        self.graphWidget_ui.toImage_button.clicked.connect(self.ExportToImage)
    
    def _InitConnectionsPie(self, width=5, height=4, dpi=100):

        self.figure = Figure(figsize=(width, height), dpi=dpi)
        self.canvas = FigureCanvas(self.figure)
        
        self.plot = self.figure.add_subplot(111)

        sortedAreas = sorted(list(self.data.items()), key=lambda item: item[1][0], reverse=True)
        sortedAreas_dict = dict(sortedAreas)
        
        sortedAreaValue = []
        sortedAreaRGBA = []
        for areaInfo in sortedAreas_dict.values():
            sortedAreaValue.append(areaInfo[0])
            sortedAreaRGBA.append((areaInfo[1][0] / 255, areaInfo[1][1] / 255, areaInfo[1][2] / 255, 1))

        totalValue_threshold = sum(sortedAreaValue) * 0.05

        # Display the Pie Graph
        wedges, _ = self.plot.pie(sortedAreaValue, startangle=90, colors=sortedAreaRGBA)

        # Recovert threshold label (to print in the legend)
        legendLabels = []
        legendValues = []

        for indexLabel, (label, (value, _)) in enumerate(sortedAreas_dict.items()):

            if value > totalValue_threshold:
                legendLabels.append(label)
                legendValues.append(wedges[indexLabel])

        self.plot.legend(legendValues, legendLabels, loc="upper center", bbox_to_anchor=(0.5, -0.1), ncol=2, fontsize='small')

        self.plot.axis('equal')
        self.figure.subplots_adjust(bottom=0.3)

        # Draw the canvas
        self.graphWidget_ui.plot_widget.layout().addWidget(self.canvas)

    def _InitMajorRegionsPie(self, width=5, height=4, dpi=100):

        self.figure = Figure(figsize=(width, height), dpi=dpi)
        self.canvas = FigureCanvas(self.figure)
        
        self.plot = self.figure.add_subplot(111)

        sortedMajorRegions = sorted(list(self.data.items()), key=lambda item: item[1], reverse=True)
        sortedMajorRegions_dict = dict(sortedMajorRegions)
        
        # Generate Distincs Color
        hues = np.linspace(0, 1, len(sortedMajorRegions_dict), endpoint=False)
        colors = [colorsys.hsv_to_rgb(hue, 0.7, 0.9) for hue in hues]

        # Display the Pie Graph
        wedges, _ = self.plot.pie(sortedMajorRegions_dict.values(), startangle=90, colors=colors)

        self.plot.legend(wedges, sortedMajorRegions_dict.keys(), 
                         loc="upper center", bbox_to_anchor=(0.5, -0.1), ncol=2, fontsize='small')

        self.plot.axis('equal')
        self.figure.subplots_adjust(bottom=0.3)

        # Draw the canvas
        self.graphWidget_ui.plot_widget.layout().addWidget(self.canvas)

    def _InitMajorRegionsBar(self, width=5, height=4, dpi=100):
        
        self.figure = Figure(figsize=(width, height), dpi=dpi)
        self.canvas = FigureCanvas(self.figure)
        
        self.plot = self.figure.add_subplot(111)



        # Draw the canvas
        self.graphWidget_ui.plot_widget.layout().addWidget(self.canvas)

    def _InitConnectionTypePie(self, width=5, height=4, dpi=100):

        self.figure = Figure(figsize=(width, height), dpi=dpi)
        self.canvas = FigureCanvas(self.figure)
        
        self.plot = self.figure.add_subplot(111)

        sortedConnectionsType = sorted(list(self.data.items()), key=lambda item: item[1], reverse=True)
        sortedConnectionsType_dict = dict(sortedConnectionsType)

        # Append color in the right order
        sortedConnectionsTypeColor = []
        for connectionsTypeName in sortedConnectionsType_dict.keys():
            match connectionsTypeName:

                case "Contralateral":
                    sortedConnectionsTypeColor.append("#556B2F") # Dark Olive Green
                case "Homotopic":
                    sortedConnectionsTypeColor.append("darkkhaki")
                case "Ipsilateral":
                    sortedConnectionsTypeColor.append("skyblue")
                case "Other":
                    sortedConnectionsTypeColor.append("lightgray")
            

        # Display the Pie Graph
        wedges, _ = self.plot.pie(sortedConnectionsType_dict.values(), startangle=90, colors=sortedConnectionsTypeColor)

        self.plot.legend(wedges, sortedConnectionsType_dict.keys(), 
                         loc="upper center", bbox_to_anchor=(0.5, -0.1), ncol=2, fontsize='small')

        self.plot.axis('equal')
        self.figure.subplots_adjust(bottom=0.3)

        # Draw the canvas
        self.graphWidget_ui.plot_widget.layout().addWidget(self.canvas)

    def _InitConnectionTypeBar(self, width=5, height=4, dpi=100):
        
        self.figure = Figure(figsize=(width, height), dpi=dpi)
        self.canvas = FigureCanvas(self.figure)
        
        self.plot = self.figure.add_subplot(111)



        # Draw the canvas
        self.graphWidget_ui.plot_widget.layout().addWidget(self.canvas)

    def ExportToCsv(self):
        
        filePath, _ = QFileDialog.getSaveFileName(self, "Save Pie Graph (CSV)", "c:\\", "CSV Files (*.csv)")

        if filePath:

            with open(filePath, 'w', newline='') as file:
                writer = csv.writer(file)
                field = ["Source", "Destination", "Value", "Percentage"]
                
                writer.writerow(field)
                totalValue = sum(self.data.values())

                for destination, value in self.data.items():
                    elements = [self.name, destination, value, value / totalValue * 100]
                    writer.writerow(elements)

    def ExportToImage(self):

        filePath, _ = QFileDialog.getSaveFileName(self, "Save Graph (Image)", "c:\\", "(*.png)")
        
        if filePath:
            high_dpi = 300
            self.plot.figure.savefig(filePath, bbox_inches='tight', dpi=high_dpi)

    def CloseWindow(self):
        
        self.mainWindow_Controller.DeleteGraphics_PieTab(self.name)
        self.close()
        self.deleteLater()  # Automatically deletes the widget from its parent when all ressources have been freed
