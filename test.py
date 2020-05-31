# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Notes = QtWidgets.QTreeView(self.centralwidget)
        self.Notes.setGeometry(QtCore.QRect(-5, 0, 181, 571))
        self.Notes.setObjectName("Notes")
        self.NoteArea = QtWidgets.QScrollArea(self.centralwidget)
        self.NoteArea.setGeometry(QtCore.QRect(170, 130, 621, 431))
        self.NoteArea.setWidgetResizable(True)
        self.NoteArea.setObjectName("NoteArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 619, 429))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.textEdit = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit.setGeometry(QtCore.QRect(0, 30, 621, 371))
        self.textEdit.setObjectName("textEdit")
        self.NoteArea.setWidget(self.scrollAreaWidgetContents)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(600, 110, 194, 22))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuedit = QtWidgets.QMenu(self.menubar)
        self.menuedit.setObjectName("menuedit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionsave = QtWidgets.QAction(MainWindow)
        self.actionsave.setObjectName("actionsave")
        self.actionsave_as = QtWidgets.QAction(MainWindow)
        self.actionsave_as.setObjectName("actionsave_as")
        self.actionopen = QtWidgets.QAction(MainWindow)
        self.actionopen.setObjectName("actionopen")
        self.actionSome_Edit = QtWidgets.QAction(MainWindow)
        self.actionSome_Edit.setObjectName("actionSome_Edit")
        self.menuFile.addAction(self.actionsave)
        self.menuFile.addAction(self.actionsave_as)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionopen)
        self.menuedit.addAction(self.actionSome_Edit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuedit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuedit.setTitle(_translate("MainWindow", "Edit"))
        self.actionsave.setText(_translate("MainWindow", "save"))
        self.actionsave_as.setText(_translate("MainWindow", "save as"))
        self.actionopen.setText(_translate("MainWindow", "open"))
        self.actionSome_Edit.setText(_translate("MainWindow", "Some Edit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
