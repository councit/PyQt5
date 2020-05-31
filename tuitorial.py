from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class MyWindow(QMainWindow):
	def __init__(self):
		super(MyWindow, self).__init__()
		self.initUI()
		# Setting window size for application
		self.setGeometry(200,200, 300, 300)
		# Writing title to outside title label
		self.setWindowTitle("Taylors App")

	def initUI(self):
		# Creating label or text on the window
		self.label = QtWidgets.QLabel(self)
		self.label.setText("my first label")
		self.label.move(50, 50)
		# Creating button 
		self.b1 = QtWidgets.QPushButton(self)
		self.b1.setText('Click Me')
		self.b1.move(100, 100)
		# b1_clicked pull
		self.b1.clicked.connect(self.b1_clicked)

	# Helper function to give functionality to b1 click
	def b1_clicked(self):
		self.label.setText('You pressed the button')
		self.update()

	def update(self):
		self.label.adjustSize()




def window():
	# Setting up sys variables to run PyQt
	app = QApplication(sys.argv)
	win = MyWindow()
	# Function to exicute code above
	win.show()
	# Function to exit application
	sys.exit(app.exec_())

window()