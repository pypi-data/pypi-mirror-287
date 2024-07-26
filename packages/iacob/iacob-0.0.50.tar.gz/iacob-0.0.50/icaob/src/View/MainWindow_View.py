from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QAction
from PyQt5 import QtWidgets

from src.Controller.MainWindow_Controller import MainWindow_Controller
from src.View.ui.MainWindow_ui import Ui_MainWindow


class MainWindowView(QMainWindow, Ui_MainWindow):

     #resized = pyqtSignal()

    # TODO : Voir quelles variables passer en paramètres (en plus du graphe)
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.mainWindow_controller = MainWindow_Controller(self)

        self._InitView()
        self.InitActions()

    def _InitView(self):
        # Hide the dock widget for the "FileInfo" tab only
        if self.mainTabWidget.currentIndex() == 0:
            self.dockWidget.hide()
        else:
            self.dockWidget.show()

        # Tab1 : File Infos
        self.fileInfosSupport_Frame.hide()
        self.noInfoTab1_Label.show()

        # Tab2 : Graph Circular
        self.circularPlot_widget.hide()
        self.noInfoTab2_Label.show()

        # Tab3 : Pie
        self.pieTabWidget.hide()
        self.noInfoTab3_Label.show()

        # Tab4 : List
        self.infoList_tableWidget.hide()
        self.noInfoTab4_Label.show()

        # Tab5 : GT
        self.noInfoTab5_Label.show()

    def InitActions(self):
        pass

    # Surcharge de la fonction resizeEvent
    """def resizeEvent(self, event):
        self.resized.emit()  # Emit the resized signal
        super().resizeEvent(event)"""