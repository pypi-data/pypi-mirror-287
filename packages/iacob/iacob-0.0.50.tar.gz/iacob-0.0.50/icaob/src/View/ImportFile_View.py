import os
from pathlib import Path

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QDesktopWidget

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from src.View.ui.ImportWindow_ui import Ui_ImportWindow
from src.Controller.ImportFile_Controller import ImportFile_Controller


class ImportFile_View(QtWidgets.QMainWindow, Ui_ImportWindow):

    def __init__(self, parent=None):
        super(ImportFile_View, self).__init__(parent=parent)

        self.setupUi(self)

        # Load Controler File
        self.importFile_Controller = ImportFile_Controller(self)

        # Action Configuration
        self._InitAction()

        # Hidden Elements
        self._HiddenElements()

        # Images Loading
        self._InitLoadingImages()

        # Graph Preparation
        self._InitGraphPreparation()

    # =====================================================================
    # Method to associate all actions to each winget when the app is opened
    # =====================================================================
    def _InitAction(self):

        # Resize the Window (80%)
        self.ResizeWindow()

        # Display Full Path when the mouse entered the item
        self.previousDataFiles_List.setMouseTracking(True)
        self.previousFlutFiles_List.setMouseTracking(True)

        # Asssociate Action to ToolButton
        self.importDataFile_Button.setDefaultAction(self.importFile_Controller.OpenDataFile_Qaction)
        self.importNameFile_Button.setDefaultAction(self.importFile_Controller.OpenNameFile_Qaction)
        self.importConfigFile_Button.setDefaultAction(self.importFile_Controller.OpenConfigFile_Qaction)
        self.importProject_Button.setDefaultAction(self.importFile_Controller.OpenProjectFile_Qaction)
        self.validation_Button.setDefaultAction(self.importFile_Controller.Validation_Qaction)

    # ==============================================
    # Method to hide elements when the app is opened
    # ==============================================
    def _HiddenElements(self):

        # Label / Button to import Name File
        self.openedNameFile_Label.hide()
        self.importNameFile_Button.hide()
        self.errorFile_Label.hide()
        #self.ERROR_Label_Validation.hide()

        # Graph Section
        self.graphSection_Widget.hide()

    # =======================================
    # Method to associate image to ToolButton
    # =======================================
    def _InitLoadingImages(self):

        resourcedir = Path(__file__).parent.parent.parent / 'resources'
        imagePath = os.path.join(resourcedir, "images", "folder.png")

        # Load image using the variable path
        pixmap = QPixmap(imagePath)
        pixmap = pixmap.scaled(self.importDataFile_Button.width(), self.importDataFile_Button.height(),
                               Qt.KeepAspectRatioByExpanding)

        # Check if pixmap loaded successfully
        if not pixmap.isNull():

            # Set pixmap as icon for the tool button
            icon_Qicon = QIcon(pixmap)

            self.importDataFile_Button.setIcon(icon_Qicon)
            self.importDataFile_Button.setIconSize(pixmap.size())
            self.importNameFile_Button.setIcon(icon_Qicon)
            self.importNameFile_Button.setIconSize(pixmap.size())
            self.importConfigFile_Button.setIcon(icon_Qicon)
            self.importConfigFile_Button.setIconSize(pixmap.size())
            self.importProject_Button.setIcon(icon_Qicon)
            self.importProject_Button.setIconSize(pixmap.size())

        else:
            pass
            # log

    # =======================================================
    # Method to create Figure and Canvas to display Histogram
    # =======================================================
    def _InitGraphPreparation(self):

        # Create a Matplotlib figure and a canvas to display it
        self.graph = Figure()
        self.canvas = FigureCanvas(self.graph)
        self.graphDisplay_Layout.addWidget(self.canvas)

    # ==================================================
    # Method to resize the window when the app is opened
    # ==================================================
    def ResizeWindow(self):

        # Obtain the Screen Size
        screen = QDesktopWidget().screenGeometry()
        screenWidth = screen.width()
        screenHeight = screen.height()

        # Define the Window Size (80%)
        widthPercentage = 0.8
        heightPercentage = 0.8

        # Compute the new Window Size
        newWidth = int(screenWidth * widthPercentage)
        newHeight = int(screenHeight * heightPercentage)

        # Apply new Value
        self.resize(newWidth, newHeight)

    # =======================================
    # Method called when the window is closed
    # =======================================
    def closeEvent(self, event):
        
        # when the application is closed, called the control to save some data
        if hasattr(self, 'importFile_Controller'):
            self.importFile_Controller.SaveData()
