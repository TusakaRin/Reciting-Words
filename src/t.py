import sys, random, os
sys.path.append(os.path.dirname(__file__))

from PyQt5.QtWidgets import QApplication, QMainWindow
from ui.table_test import Ui_MainWindow
from PyQt5.QtCore import pyqtSignal, Qt

import pandas as pd
from config import fd_project
from os.path import join as pjoin


class MyTable(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyTable, self).__init__(parent)
        self.setupUi(self)
        self.init_UI()
    
    def init_UI(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyTable()
    win.show()
    sys.exit(app.exec_())
