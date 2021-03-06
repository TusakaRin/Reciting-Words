# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWin.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(796, 425)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.confirmBtn = QtWidgets.QPushButton(self.centralwidget)
        self.confirmBtn.setGeometry(QtCore.QRect(280, 50, 31, 31))
        self.confirmBtn.setObjectName("confirmBtn")
        self.mainText = QtWidgets.QLabel(self.centralwidget)
        self.mainText.setGeometry(QtCore.QRect(40, 110, 391, 111))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.mainText.setFont(font)
        self.mainText.setAlignment(QtCore.Qt.AlignCenter)
        self.mainText.setObjectName("mainText")
        self.meanText = QtWidgets.QLabel(self.centralwidget)
        self.meanText.setGeometry(QtCore.QRect(50, 220, 361, 111))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.meanText.setFont(font)
        self.meanText.setText("")
        self.meanText.setAlignment(QtCore.Qt.AlignCenter)
        self.meanText.setWordWrap(True)
        self.meanText.setObjectName("meanText")
        self.resetBtn = QtWidgets.QPushButton(self.centralwidget)
        self.resetBtn.setGeometry(QtCore.QRect(320, 50, 31, 31))
        self.resetBtn.setObjectName("resetBtn")
        self.showCheck = QtWidgets.QCheckBox(self.centralwidget)
        self.showCheck.setGeometry(QtCore.QRect(290, 90, 101, 16))
        self.showCheck.setChecked(True)
        self.showCheck.setObjectName("showCheck")
        self.pronText = QtWidgets.QLabel(self.centralwidget)
        self.pronText.setGeometry(QtCore.QRect(40, 130, 391, 111))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pronText.setFont(font)
        self.pronText.setText("")
        self.pronText.setAlignment(QtCore.Qt.AlignCenter)
        self.pronText.setObjectName("pronText")
        self.currentlcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.currentlcd.setGeometry(QtCore.QRect(460, 20, 151, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.currentlcd.setFont(font)
        self.currentlcd.setObjectName("currentlcd")
        self.nextlcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.nextlcd.setGeometry(QtCore.QRect(640, 20, 151, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.nextlcd.setFont(font)
        self.nextlcd.setObjectName("nextlcd")
        self.shuffleBtn = QtWidgets.QPushButton(self.centralwidget)
        self.shuffleBtn.setGeometry(QtCore.QRect(360, 50, 31, 31))
        self.shuffleBtn.setObjectName("shuffleBtn")
        self.listlistwidget = QtWidgets.QListWidget(self.centralwidget)
        self.listlistwidget.setGeometry(QtCore.QRect(60, 10, 191, 131))
        self.listlistwidget.setObjectName("listlistwidget")
        self.passbtn = QtWidgets.QPushButton(self.centralwidget)
        self.passbtn.setGeometry(QtCore.QRect(104, 320, 131, 51))
        self.passbtn.setObjectName("passbtn")
        self.remainbtn = QtWidgets.QPushButton(self.centralwidget)
        self.remainbtn.setGeometry(QtCore.QRect(230, 320, 131, 51))
        self.remainbtn.setObjectName("remainbtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 796, 23))
        self.menubar.setObjectName("menubar")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.confirmBtn.setText(_translate("MainWindow", "√"))
        self.mainText.setText(_translate("MainWindow", "Start Reciting Word!"))
        self.resetBtn.setText(_translate("MainWindow", "R"))
        self.showCheck.setText(_translate("MainWindow", "Show Meaning"))
        self.shuffleBtn.setText(_translate("MainWindow", "S"))
        self.passbtn.setText(_translate("MainWindow", "PASS"))
        self.remainbtn.setText(_translate("MainWindow", "REMAIN"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
