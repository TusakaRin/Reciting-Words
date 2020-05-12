# -*- coding: utf-8 -*-

# @Time : 2020/5/10 15:19
# @Author : yfdai


import sys, random, os
sys.path.append(os.path.dirname(__file__))

from PyQt5.QtWidgets import QApplication, QMainWindow
from ui.MainWin import Ui_MainWindow
from PyQt5.QtCore import pyqtSignal, Qt

import pandas as pd
from config import fd_project
from os.path import join as pjoin


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        self.word_idx = -1
        self.filtered = False
        self.data = pd.read_excel(pjoin(fd_project, 'data/gre3k.xlsx')).rename(columns={'mean': 'meaning'})
        self.current_round = []
        self.next_round = []
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        for idx, li in self.data.list.drop_duplicates().sort_values().iteritems():
            self.listChosenBox.addItem(str(li))
        self.confirmBtn.clicked.connect(self.filter_list)
        self.resetBtn.clicked.connect(self.reset)
        self.showCheck.stateChanged.connect(self.hide_text)
        self.shuffleBtn.clicked.connect(self.shuffle_list)

    def shuffle_list(self):
        remain_list = self.current_round[self.word_idx + 1:]
        random.shuffle(remain_list)
        self.current_round = self.current_round[: self.word_idx + 1] + remain_list

    def filter_list(self):
        if not self.filtered:
            self.current_round = ([
                j for i, j in
                self.data[self.data.list == int(self.listChosenBox.currentText())]
                .reset_index(drop=True)
                .iterrows()
            ])
            self.confirmBtn.setText(self.listChosenBox.currentText())
            self.switch_word(True)
            self.filtered = True

    def reset(self):
        self.filtered = False
        self.word_idx = -1
        self.current_round = []
        self.next_round = []
        self.confirmBtn.setText('√')
        self.pronText.setText('')
        self.mainText.setText('Start Reciting Word!')
        self.meanText.setText('')
        self.nextlcd.display(0)
        self.currentlcd.display(0)

    def switch_word(self, flag):
        self.word_idx += 1
        if not flag:
            self.next_round.append(self.current_round[self.word_idx - 1])
        if self.word_idx >= len(self.current_round):
            self.word_idx = 0
            self.current_round = [i for i in self.next_round]
            self.next_round = []
        if not self.current_round:
            self.mainText.setText('Recite Complete')
            self.reset()
            return
        self.currentlcd.display(len(self.current_round) - self.word_idx)
        self.nextlcd.display(len(self.next_round))
        row = self.current_round[self.word_idx]
        self.mainText.setText(row.word)
        self.pronText.setText(row.usp)
        self.meanText.setText('')
        if self.showCheck.isChecked():
            self.show_text()

    def show_text(self):
        self.meanText.setText(str(self.current_round[self.word_idx].meaning))

    def hide_text(self, state):
        if not state:
            self.meanText.setText('')
        else:
            self.show_text()

    def keyPressEvent(self, event):
        if self.filtered:
            if event.key() == Qt.Key_M:
                self.switch_word(True)
            elif event.key() == Qt.Key_N:
                if not self.meanText.text():
                    self.show_text()
                else:
                    self.switch_word(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyMainWindow()
    win.show()
    sys.exit(app.exec_())
