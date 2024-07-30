import os
import csv

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget, QFileDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from src.View.ui.GraphWidget_ui import Ui_GraphWidget


class GraphicWidget(QWidget):

    def __init__(self, name, data):
        super().__init__()

        # Setup widget UI
        self.graphWidget_ui = Ui_GraphWidget()
        self.graphWidget_ui.setupUi(self)

        self.name = name
        self.data = data

        self.plot = None
        self.graphWidget_ui.title_label.setText(name)
        self._InitMatplotlibFigure()

        self.graphWidget_ui.closeButton.clicked.connect(self.CloseWindow)
        self.graphWidget_ui.toCsv_button.clicked.connect(self.ExportToCsv)
        self.graphWidget_ui.toImage_button.clicked.connect(self.ExportToImage)
    
    def _InitMatplotlibFigure(self, width=5, height=4, dpi=100):

        self.figure = Figure(figsize=(width, height), dpi=dpi)
        self.canvas = FigureCanvas(self.figure)
        
        self.plot = self.figure.add_subplot(111)

        sortedAreas = sorted(list(self.data.items()), key=lambda x: x[1], reverse=True)
        sortedAreas_dict = dict(sortedAreas)

        totalValue_threshold = sum(sortedAreas_dict.values()) * 0.05

        # Display the Pie Graph
        wedges, _ = self.plot.pie(sortedAreas_dict.values(), startangle=90)

        # Recovert threshold label (to print in the legend)
        legendLabels = []
        legendValues = []

        for indexLabel, (label, value) in enumerate(sortedAreas_dict.items()):

            if value > totalValue_threshold:
                legendLabels.append(label)
                legendValues.append(wedges[indexLabel])

        self.plot.legend(legendValues, legendLabels, loc="upper center", bbox_to_anchor=(0.5, -0.1), ncol=2, fontsize='small')

        self.plot.axis('equal')
        self.figure.subplots_adjust(bottom=0.3)

        # Draw the canvas
        self.canvas.draw()
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

        filePath, _ = QFileDialog.getSaveFileName(self, "Save Pie Graph (Image)", "c:\\", "(*.png)")
        
        if filePath:
            high_dpi = 300
            self.plot.figure.savefig(filePath, bbox_inches='tight', dpi=high_dpi)

    def CloseWindow(self):

        self.close()
        self.deleteLater()  # Automatically deletes the widget from its parent when all ressources have been freed
