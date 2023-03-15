import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui


class ImageViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Viewer")
        self.resize(600, 400)
        # Image display area
        self.imageLabel = QLabel(self)
        self.setCentralWidget(self.imageLabel)

        # Actions
        self.openImg = QAction("Open", self)
        self.openImg.triggered.connect(self.openImage)

        self.rotateRight = QAction("&Right", self,icon=QIcon("icons\\rotate-right.png"))
        self.rotateRight.triggered.connect(self.rotate_right)

        self.rotateLeft = QAction("&Left", self,icon=QIcon("icons\\rotate-left.png"))
        self.rotateLeft.triggered.connect(self.rotate_left)

        # Menu Bar
        self.menubar = self.menuBar()
        self.menubar.addAction(self.openImg)
        self.rotate = self.menubar.addMenu("&Rotate")
        self.rotate.addAction(self.rotateRight)
        self.rotate.addAction(self.rotateLeft)

        self.rotateLeft.setShortcut("Ctrl+Shift+R")
        self.rotateRight.setShortcut("Ctrl+Shift+L")
        self.openImg.setShortcut("Ctrl+O")

    def openImage(self):
        try:
            file_name, _ = QFileDialog.getOpenFileName(self, 'Select image', '', 'Image files (*.png *.jpg *.bmp)')
            if file_name:
                image = QPixmap(file_name)
                self.imageLabel.setPixmap(image)
                self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)
        except Exception as error:
            print(error)

    def rotate_left(self):
        try:
            transform = QtGui.QTransform().rotate(-90)
            img = self.imageLabel.pixmap()
            rotated_img = img.transformed(transform, QtCore.Qt.SmoothTransformation)
            self.imageLabel.setPixmap(rotated_img)
        except Exception as error:
            print(error)

    def rotate_right(self):
        try:
            transform = QtGui.QTransform().rotate(90)
            img = self.imageLabel.pixmap()
            rotated_img = img.transformed(transform, QtCore.Qt.SmoothTransformation)
            self.imageLabel.setPixmap(rotated_img)
        except Exception as error:
            print(error)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ImageViewer()
    window.show()
    sys.exit(app.exec_())
