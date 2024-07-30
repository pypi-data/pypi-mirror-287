import math
import random
import sys
from math import comb
from typing import Union

import numpy as np
import pyqtgraph as pg
from PyQt5 import QtWidgets
from PyQt5.QtCore import QPointF, Qt, pyqtSignal
from PyQt5.QtGui import QFont, QColor, QPainter, QTransform, QImage, QPainterPath, QFontMetrics
from PyQt5.QtWidgets import QGraphicsBlurEffect, QWidget, QVBoxLayout
from matplotlib.path import Path


class RegionLabelItem_ConnGraphic(pg.ImageItem):
    textClicked = pyqtSignal(int)

    def __init__(self, text: str, coordinates, color: QColor = QColor(0, 0, 0), **kargs):
        # Init label attributes
        self.text = text
        self.coordinates = coordinates
        self.color = color
        self.distance = 1  # TODO : à voir quel réglage est préférable

        size_min, size_max = 6, 12
        self.size = self.computeTextSize(size_min, size_max)
        self.rotation, self.anchor = self.computeTextRotation()

        np_image = self._initText()
        super().__init__(np_image, **kargs)

        self._initImage()

    def _initText(self):
        # Initialisation de la police pour calculer la taille de la zone de texte
        font = QFont("Arial", self.size, weight=QFont.Bold)
        self.text_width = QFontMetrics(font).width(self.text, len(self.text))
        self.text_height = QFontMetrics(font).height()

        #width, height = self.size * len(self.text), self.size + 6
        image = QImage(self.text_width, self.text_height, QImage.Format_ARGB32)
        image.fill(Qt.transparent)

        # On utilise QPainter et QPainterPath pour afficher le texte
        painter = QPainter(image)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.TextAntialiasing)
        painter.setFont(font)

        path = QPainterPath()
        path.addText(0, self.size + 3, font, self.text)

        painter.fillPath(path, self.color)
        painter.end()

        # On convertit ensuite ce texte en matrice pour initialiser l'ImageItem
        np_image = self.imageToNpArray(image)

        return np_image

    def _initImage(self):
        self.setPos(self.computeTextCoordinates(self.distance))
        self.setTransform(self.computeTextTransform())

        blurEffect = QGraphicsBlurEffect(blurRadius=1.01)
        self.setGraphicsEffect(blurEffect)

    def imageToNpArray(self, image: QImage):
        width, height = image.width(), image.height()

        buffer = image.bits().asstring(width * height * 4)
        np_array = np.frombuffer(buffer, dtype=np.uint8).reshape((height, width, 4))

        return np_array

    def computeTextSize(self, size_min: int, size_max: int):
        size = int(math.dist(self.coordinates[2], self.coordinates[3]))

        # To guarantee that text size is beetween given min and max size
        size = min(size_max, size)
        size = max(size_min, size)

        return size

    def computeTextRotation(self):
        if self.coordinates[2, 1] - self.coordinates[3, 1] < 0:
            x = -np.mean(self.coordinates[:, 0])
            y = -np.mean(self.coordinates[:, 1])
            anchor = (1, 0.5)
        else:
            x = np.mean(self.coordinates[:, 0])
            y = np.mean(self.coordinates[:, 1])
            anchor = (0, 0.5)

        angle = -np.arctan2(x, y)

        return np.degrees(angle), anchor

    def computeTextCoordinates(self, distance):
        p1, p2 = self.coordinates[2], self.coordinates[3]

        # Calculate the normal vector to the longer side
        dx, dy = p2 - p1
        normal_vector = np.array([-dy, dx])
        normal_vector = normal_vector / np.linalg.norm(normal_vector) * distance

        # Determine the direction to place the point outside the region
        midpoint = (p1 + p2) / 2
        point = midpoint + normal_vector

        text_coordinates = QPointF(point[0], point[1])

        # Now the position is defined, we translate the text depending on the anchor settings

        x = text_coordinates.x()
        text_coordinates.setX(x)
        return text_coordinates

    def computeTextTransform(self):
        tr = QTransform()
        tr.scale(0.3, 0.3)
        tr.rotate(self.rotation)

        xt = -self.anchor[1] * self.text_height
        # We use text_len to put the anchor at the end of the text if it is reversed
        yt = -self.anchor[0] * self.text_width + self.distance
        tr.translate(xt, yt)

        return tr

    def mousePressEvent(self, ev, *args, **kwargs):
        self.textClicked.emit(ev.button)


class RegionItem_ConnGraphic:
    outside: pg.PlotDataItem  # Outer line of the region
    inside: pg.FillBetweenItem  # Colored part of the region
    textArea: pg.FillBetweenItem  # Temp
    text: RegionLabelItem_ConnGraphic  # Text label
    edgesVisible = True

    #textClicked = pyqtSignal(int)

    def __init__(self, code: int, name: str, coordinates, innerCirclePoints, outerCirclePoints,
                 outerCircleTextPoints, textCoordinates,
                 regionColor=QColor(255, 255, 255, 255), textColor=(0, 0, 0), precision=1,
                 textFont: QFont = QFont("Arial", pointSize=8, weight=QFont.ExtraBold), *args):
        """
        :param coordinates: 4 coordinates points which define the polygon to draw
        """
        self.name = name
        self.coordinates = coordinates
        self.code = code
        self.regionColor = regionColor
        self.precision = precision

        self.innerCoords = self.LineToCircleArc(innerCirclePoints, coordinates[0])
        self.outerCoords = self.LineToCircleArc(outerCirclePoints, coordinates[3])
        self.outerTextCoords = self.LineToCircleArc(outerCircleTextPoints, textCoordinates[3])

        x_coords = np.append(np.append(self.innerCoords[:, 0],
                                       self.outerCoords[::-1, 0]),
                             self.innerCoords[0, 0])
        y_coords = np.append(np.append(self.innerCoords[:, 1],
                                       self.outerCoords[::-1, 1]),
                             self.innerCoords[0, 1])

        # Draw the outline of the polygon
        self.outside = pg.PlotDataItem(x_coords, y_coords, pen=pg.mkPen(color='black', width=1))

        # Color the inside of the polygon
        innerLine = pg.PlotDataItem(self.innerCoords[:, 0], self.innerCoords[:, 1])
        outerLine = pg.PlotDataItem(self.outerCoords[:, 0], self.outerCoords[:, 1])

        self.inside = pg.FillBetweenItem(innerLine, outerLine, brush=pg.mkBrush(regionColor))

        # Add text next to the polygon
        self.text = RegionLabelItem_ConnGraphic(self.name, textCoordinates)
        # Add event listener for text click
        #self.text.textClicked.connect(self.textClicked)

        #TODO : finir de gérer le clic sur le texte
        super().__init__(*args)

    # Function used for rouding region borders
    def LineToCircleArc(self, circlePoints, start):
        # Find the two points on the circle closest to the start and end points
        startDistances = np.linalg.norm(circlePoints - start, axis=1)

        startIndex = np.argmin(startDistances)
        endIndex = startIndex + self.precision

        return circlePoints[startIndex:endIndex + 1]

    #TODO : exemple de commentaire pour la doc ici !!
    def isPointInRegionPolygon(self, x, y):
        """
        Compute if the given point is inside the polygon region

        Parameters
        ----------
        x : int
            x coordinate of the point
        y : int
            y coordinate of the point

        Returns
        -------
        bool
            True if inside else False
        """
        # Create matplotlib Path object
        polygonPoints = np.vstack((self.innerCoords, self.outerCoords[::-1]))
        polygonPath = Path(polygonPoints)

        # Check if the point is inside the polygon
        return polygonPath.contains_point((x, y))

    def regionClickEvent(self, ev=None):
        pass


class EdgeItem_ConnGraphic(pg.PlotCurveItem):
    value = 0
    node1: int
    node2: int

    def __init__(self, node1=0, node2=0, value=0, node1_x=0, node1_y=0, node2_x=0, node2_y=0,
                 color=(100, 100, 100, 100), width=1, precision=20, *args,
                 **kargs):
        self.node1 = node1
        self.node2 = node2
        self.node1_x = node1_x
        self.node1_y = node1_y
        self.node2_x = node2_x
        self.node2_y = node2_y
        self.precision = precision
        self.value = value

        x, y = self.computeBezierCurve()

        pen = pg.mkPen(color=color, width=width)

        super().__init__(x=x, y=y, pen=pen, *args, **kargs)

    def computeBezierCurve(self):
        #TODO : ajouter la notion d'intensité de courbure en créant un point de contrôle
        #       entre (0, 0) et mean(p0, p1) selon un certain facteur
        p0 = [self.node1_x, self.node1_y]
        p1 = [self.node2_x, self.node2_y]
        controlPoint = np.array([0, 0])
        controlPoints = np.array([p0, controlPoint, p1])
        n = len(controlPoints) - 1

        values = np.linspace(0, 1, self.precision)
        bezierPoints = np.array(
            [sum(comb(n, i) * (t ** i) * ((1 - t) ** (n - i)) * controlPoints[i]
                 for i in range(n + 1)) for t in values])

        return bezierPoints[:, 0], bezierPoints[:, 1]


class ConnGraphicView(pg.ViewBox):
    regions: list[Union[RegionItem_ConnGraphic, None]]  # Can contain both None or RegionItem_ConnGraphic
    colors: list[QColor]
    edges: list[EdgeItem_ConnGraphic]
    edgesVisible: bool

    # TODO : Modifier les paramètres d'initialisation pour passer le graphe complet
    def __init__(self, numPoints, parent=None):
        print("Init graphic_view connectivity graph...")
        super().__init__(parent)

        # Init regions and edges list
        self.regions = [None for i in range(numPoints)]
        self.edges = []
        self.edgesVisible = True

        self.colors = []
        for i in range(numPoints):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            self.colors.append(QColor(r, g, b))

        # Init class attributes
        self.numPoints = numPoints

        self._initViewSettings()
        self._initGraphSettings()
        self._InitGraph_Regions()
        self._InitGraph_Edges()
        print("Connectivity graph loaded.")

    def _initViewSettings(self):
        print("Init graphic_view settings...")

        self.disableAutoRange()
        #self.setMouseEnabled(False, False)  # Disable mouse interactions
        self.setBackgroundColor("w")

        XRange = 100
        YRange = 100
        self.setRange(xRange=(-XRange, XRange), yRange=(-YRange, YRange))

    def _initGraphSettings(self):
        print("Init graph settings...")

        angles = np.linspace(0, 2 * np.pi, self.numPoints, endpoint=False)
        radius = 50
        tickness = 5  # of a region
        textLenght = 20
        self.precision = 20  # nb of lines which compose an edge

        # coordinates of each region
        self.innerPoints = np.vstack((np.cos(angles), np.sin(angles))).T * radius
        self.outerPoints = np.vstack((np.cos(angles), np.sin(angles))).T * (radius + tickness)
        self.textPoints = np.vstack((np.cos(angles), np.sin(angles))).T * (radius + tickness + textLenght)

        # create two circle for the inner and outer line of the donut
        circleAngle = np.linspace(0, 2 * np.pi, self.numPoints * self.precision, endpoint=False)
        circleAngle = np.append(circleAngle, circleAngle[0])

        self.innerCirclePoints = np.vstack((np.cos(circleAngle), np.sin(circleAngle))).T * radius
        self.outerCirclePoints = np.vstack((np.cos(circleAngle), np.sin(circleAngle))).T * (radius + tickness)
        self.outerCircleTextPoints = np.vstack((np.cos(circleAngle), np.sin(circleAngle))).T * (
                radius + tickness + textLenght)

        self.font = QFont("Arial", pointSize=9, weight=QFont.ExtraBold)

    def _InitGraph_Regions(self):
        names = ["lh_G_front_inf-Orbital", "rh_S_circular_insula_ant", "Right-Caudate"]
        for i in range(self.numPoints):
            if i % 9 != 0:
                self.CreateRegionOnGraph(i, random.choice(names), self.colors[i], i)
            PrintProgressBar(i, self.numPoints - 1, "Init graph regions : ", "Complete", length=30)

    def _InitGraph_Edges(self):
        for i in range(len(self.regions)):
            PrintProgressBar(i, len(self.regions) - 1, "Init graph edges : ", "Complete", length=30)
            for j in range(i + 1, len(self.regions)):
                self.CreateEdge(i, j, None)

        i = 0
        for edge in self.edges:
            print(f"Edge {i} : {edge.value}")
            i += 1

    def AddRegion(self, region: RegionItem_ConnGraphic, pos=None):

        # TODO : à revoir une fois le graphe implémenté
        if pos is None:
            self.regions.append(region)
        else:
            self.regions[pos] = region

        # Add polygon to the graphic_view
        self.addItem(region.inside)
        self.addItem(region.outside)

        # Add label to the graphic_view
        self.addItem(region.text)

        #region.text.textClicked.connect(lambda : self.regionClickEvent(..., region))

        #TODO : add signal for text click

    # create a new RegionItem at a given position in RegionList (beetween 1 and numPoints)
    def CreateRegionOnGraph(self, code, name, color, pos):
        pos -= 1

        # Get coordinates on the inner/outer circle of the graph
        coordinates = np.array([
            [self.outerPoints[pos][0], self.outerPoints[pos][1]],
            [self.outerPoints[pos + 1][0], self.outerPoints[pos + 1][1]],
            [self.innerPoints[pos + 1][0], self.innerPoints[pos + 1][1]],
            [self.innerPoints[pos][0], self.innerPoints[pos][1]]
        ])

        textCoordinates = np.array([
            [self.textPoints[pos][0], self.textPoints[pos][1]],
            [self.textPoints[pos + 1][0], self.textPoints[pos + 1][1]],
            [self.outerPoints[pos + 1][0], self.outerPoints[pos + 1][1]],
            [self.outerPoints[pos][0], self.outerPoints[pos][1]]
        ])

        # Create region
        self.regions[pos] = RegionItem_ConnGraphic(code, name, coordinates,
                                                   self.innerCirclePoints, self.outerCirclePoints,
                                                   self.outerCircleTextPoints,
                                                   textCoordinates, regionColor=color, precision=self.precision,
                                                   textFont=self.font)

        self.AddRegion(self.regions[pos], pos)

    # Get a region of the graph with its code
    def GetRegion(self, code):
        for region in self.regions:
            if region is not None:
                if region.code == code:
                    return region
        return None

    def AddEdgeToGraph(self, edge: EdgeItem_ConnGraphic):
        if edge is not None:
            self.edges.append(edge)

            # Add edge to the graphic_view
            self.addItem(edge)

    def CreateEdge(self, node1, node2, value):
        self.testFilter = 100

        # Generate random conn val
        power = 100
        rand = math.pow(random.randint(0, 255), power)
        value = (rand / math.pow(255, power)) * 25500 * random.random()

        if value > self.testFilter:
            region1 = self.GetRegion(node1)
            region2 = self.GetRegion(node2)

            if region1 is not None and region2 is not None:
                # Compute edge ends
                region1Coordinates = region1.coordinates
                region2Coordinates = region2.coordinates

                #TODO : à retravailler (actuellement conçue pour des valeurs aléatoires)
                edgeR = 100
                edgeG = 100
                edgeB = 100

                edgeA = int(value / 100)
                color = QColor(edgeR, edgeG, edgeB, edgeA)
                edgeW = int(value / (2550 * 2))

                # Get coordinate of each region border
                x1 = np.mean([region1Coordinates[2, 0], region1Coordinates[3, 0]])
                y1 = np.mean([region1Coordinates[2, 1], region1Coordinates[3, 1]])
                x2 = np.mean([region2Coordinates[2, 0], region2Coordinates[3, 0]])
                y2 = np.mean([region2Coordinates[2, 1], region2Coordinates[3, 1]])

                # Create the Edge
                edge = EdgeItem_ConnGraphic(node1, node2, int(value), x1, y1, x2, y2, color, edgeW, self.precision)

                self.AddEdgeToGraph(edge)

    # Get an edge of the graph with its two nodes
    def GetEdge(self, node1, node2):
        for edge in self.edges:
            if edge is not None:
                if edge.node1 == node1 and edge.node2 == node2:
                    return edge
        return None

    def GetRegionEdges(self, code):
        edges = []
        for edge in self.edges:
            if edge is not None:
                if edge.node1 == code or edge.node2 == code:
                    edges.append(edge)
        return edges

    def GetSortedEdgeList(self, sorting: bool):
        # TODO : check if edge is not None
        # True mean descending, False mean ascending
        return sorted(self.edges, key=lambda edge: edge.value, reverse=sorting)

    #TODO : modifier ça en keep edges beetween values
    def KeepWeightBeetween(self, inf, sup):
        for edge in self.edges:
            if edge is not None:
                if edge.value < inf or edge.value > sup:
                    edge.hide()
                else:
                    edge.show()

        for region in self.regions:
            if region is not None:
                continue
                # TODO : tout doux

    #TODO : modifier ça en keep edges beetween ranks
    def DiscardEdgeUnderRank(self, rank):
        edges = self.GetSortedEdgeList(True)
        for i in range(rank - 1):
            if edges[i] is not None:
                edges[i].show()
        for i in range(rank, len(edges)):
            if edges[i] is not None:
                edges[i].hide()

    def ToggleAllEdges(self):
        # Toggle edges
        for edge in self.edges:
            if edge is not None:
                edge.hide() if self.edgesVisible else edge.show()

        # Set all region as "hidden edges" state
        for region in self.regions:
            if region is not None:
                region.edgesVisible = not self.edgesVisible

        self.edgesVisible = not self.edgesVisible

    def SetRegionEdgesVisible(self, region, visible):
        if region is not None:
            code = region.code
            edges = self.GetRegionEdges(code)

            # Toggle edges
            for edge in edges:
                edge.show() if visible else edge.hide()

            region.edgesVisible = visible

    def mouseClickEvent(self, ev):
        #super().mouseClickEvent(ev) open context menu with right click, so we need to override it
        # Keep the menu enabled, but with a different button
        if ev.button() == Qt.MouseButton.MiddleButton and self.menuEnabled():
            ev.accept()  # Indicate that the event will be handled so the parent won't receive it
            #self.raiseContextMenu(ev)
            self.DiscardEdgeUnder(20)
        else:
            # Convert pixel position into scene position
            p = self.mapSceneToView(ev.scenePos())  # QPointF

            # Search for a region under clicked point
            for region in self.regions:
                if region is not None and region.isPointInRegionPolygon(p.x(), p.y()):
                    print(f"Region n°{region.code} clicked ! [at ({p.x()}, {p.y()})]")
                    ev.accept()
                    self.RegionClickEvent(ev, region)
                    break

    def RegionClickEvent(self, ev, region):
        if ev.button() == Qt.MouseButton.LeftButton:
            self.SetRegionEdgesVisible(region, True)
        elif ev.button() == Qt.MouseButton.RightButton:
            self.SetRegionEdgesVisible(region, False)
        pass


class ConnGraphic_Widget(QWidget):
    graphic_view: ConnGraphicView

    def __init__(self, region_num, width=100, height=100):
        super().__init__()
        self.graphic_view = ConnGraphicView(region_num)

        self.graphic = pg.GraphicsView()
        self.graphic.setCentralItem(self.graphic_view)

        QVBoxLayout(self)
        self.layout().addWidget(self.graphic)
        self.setMinimumWidth(width)
        self.setMinimumHeight(height)


# Print iterations progress
# (from https://stackoverflow.com/questions/3173320/text-progress-bar-in-terminal-with-block-characters)
def PrintProgressBar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    sys.stdout.write(f'\r{prefix} |{bar}| {percent}% {suffix}')
    # Print New Line on Complete
    if iteration == total:
        print()


#TODO : remove it later
def printCoordinates(coordinates):
    i = 0
    for point in coordinates:
        print(f"Point {i} : ({point[0]}, {point[1]})")
        i += 1
