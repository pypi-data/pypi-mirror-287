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

        # Recovert Data from ConnGraph Object
        labels = []
        values = []
        totalValue_threshold = sum(self.data.values()) * 0.05
    
        # Display name with value superior to 5% of the values sum
        for name, value in self.data.items():

            if value > totalValue_threshold:
                labels.append(name)
            else:
                labels.append("")

            values.append(value)

        # Display the Pie Graph
        wedges, _ = self.plot.pie(values)

        # Recovert threshold label (to print in the legend)
        legendLabels = [label for label in labels if label]
        legendValues = [wedges[i] for i, label in enumerate(labels) if label]

        self.plot.legend(legendValues, legendLabels, loc="upper center", bbox_to_anchor=(0.5, -0.1), ncol=2, fontsize='small')

        self.plot.axis('equal')
        self.figure.subplots_adjust(bottom=0.3)

        # Draw the canvas
        self.canvas.draw()
        self.graphWidget_ui.plot_widget.layout().addWidget(self.canvas)

    def ExportToCsv(self):
        print("export to csv")

    def ExportToImage(self):
        print("export to image")
        filePath, _ = QFileDialog.getSaveFileName(self, "Save file", "c:\\", "(*.png)")
        
        if filePath:
            self.plot.figure.savefig(filePath, bbox_inches='tight')

    def CloseWindow(self):

        self.close()
        self.deleteLater()  # Automatically deletes the widget from its parent when all ressources have been freed
