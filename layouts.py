from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys

# Subclass QMainWindow to customise your application's main window

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        
        self.setWindowTitle("My Awesome App")


        tabs = QTabWidget()
        tabs.setDocumentMode(True)
        tabs.setTabPosition(QTabWidget.South)
        tabs.setMovable(True)

        for n, color in enumerate(['red','green','blue','yellow']):
            tabs.addTab( Color(color), color)

        self.setCentralWidget(tabs)


class Color(QWidget):

    def __init__(self, color, *args, **kwargs):
        super(Color, self).__init__(*args, **kwargs)
        self.setAutoFillBackground(True)
        
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

# Running app
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
