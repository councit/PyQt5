import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QToolBar, QAction, QStatusBar, QCheckBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon


# Subclass QMainWindow to customise your application's main window
class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        
        self.setWindowTitle("My Awesome App")
        
        label = QLabel("THIS IS AWESOME!!!")
        label.setAlignment(Qt.AlignCenter)
        
        self.setCentralWidget(label)
        
        toolbar = QToolBar("My main toolbar")
        self.addToolBar(toolbar)

        # Andriod Button
        button_action = QAction(QIcon("android.png"), "Your button", self)
        button_action.setStatusTip('This is your button')
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        toolbar.addSeparator()
        #Second Button
        button_action2 = QAction(QIcon('android.png'), 'Your button2', self)
        button_action2.setStatusTip('This is your button 2')
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)

        #CheckBox
        toolbar.addWidget(QLabel('Hello'))
        toolbar.addWidget(QCheckBox())

        self.setStatusBar(QStatusBar(self))
        
        
    def onMyToolBarButtonClick(self, s):
        print("click", s)

# Running App
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
