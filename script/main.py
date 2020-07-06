import sys, os
from os.path import join as pjoin
sys.path.append(pjoin(os.path.dirname(__file__), '../src'))

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QSignalMapper, QMimeData
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QDrag

from wordmgr.mgr import WordMgr
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QLabel, QCheckBox, QListWidget
from ui.MainWin import Ui_MainWindow


class MyListWidget(QListWidget):
    def __init__(self, mainView, parent=None):
        super().__init__(parent)
        self.mainView = mainView
        self.setAcceptDrops(True)  # 必须有(当然，图标模式的列表控件已默认打开）
        self.map_word_item = {}

    def dragEnterEvent(self, event):  # 拖动开始时，以及刚进入目标控件时调用
        event.accept()

    def dragMoveEvent(self, event):
        event.accept()

    def startDrag(self):  # self是源控件
        item: QListWidgetItem = self.currentItem()
        if item is None:  # 没有选中可拖动项
            return
        mimeData = QMimeData()
        mimeData.setText(self.itemWidget(item).text() + f'@{self.objectName()}')  # 自定义数据的格式名'application/x-阿猫
        drag = QDrag(self)
        drag.setMimeData(mimeData)
        if drag.exec_(Qt.MoveAction) == Qt.MoveAction:  # Qt.CopyAction 复制# Qt.MoveAction 移动
            index = self.row(item)  # 返回拖动项在源列表控件的索引
            self.takeItem(index)

    def dropEvent(self, event):
        # print(event.mimeData() .formats())
        item = QListWidgetItem(self)
        word, from_ = event.mimeData().text().split('@')
        self.mainView.drag(from_, self.objectName(), word)
        self.setItemWidget(item, QLabel(word))
        event.accept()
        self.map_word_item[word] = item

    # 确保startDrag被调用的最简单的方法就是对mouseMoveEvent()重新实现
    def mouseMoveEvent(self, event):
        self.startDrag()


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.mgr = WordMgr(auto_shuffle=False)
        self.setupUi(self)

        self.signal_map_list_checkbox = QSignalMapper()
        self.signal_map_list_checkbox.mapped[int].connect(self.onListCheckboxChanged)
        self.map_li_checkbox = {}

        self.initUI()

    def initUI(self):
        def onConfirmClicked():
            self.confirmBtn.setEnabled(False)
            self.resetBtn.setEnabled(True)
            self.mgr.filter_words()
            for word in self.mgr.current_remain:
                label = QLabel()
                label.setText(word[1])
                item = QListWidgetItem()
                self.currentRemainList.addItem(item)
                self.currentRemainList.setItemWidget(item, label)
                self.currentRemainList.map_word_item[word[1]] = item
            self.uiSwitchWord()
        self.confirmBtn.clicked.connect(onConfirmClicked)

        def onShuffleClicked():
            self.mgr.shuffle()
        self.shuffleBtn.clicked.connect(onShuffleClicked)

        def onResetClicked():
            self.resetBtn.setEnabled(False)
            self.confirmBtn.setEnabled(True)
            self.nextlcd.display(0)
            self.currentlcd.display(0)
            for li in [self.currentRemainList, self.nextRoundList, self.finishedList]:
                li.clear()
                li.map_word_item = {}
            self.mgr.reset()
        self.resetBtn.clicked.connect(onResetClicked)

        def onShowMeaningChanged(state):
            if not state:
                self.meanText.setText('')
            else:
                self.showMeaning()
        self.showCheck.stateChanged.connect(onShowMeaningChanged)

        self.listlistwidget.setDragEnabled(True)
        self.finishedList.setAcceptDrops(True)
        for idx, li in self.mgr.words.list.drop_duplicates().sort_values().iteritems():
            item = QListWidgetItem()
            widget = QCheckBox()
            widget.setText(f'List {li}')
            widget.stateChanged.connect(self.signal_map_list_checkbox.map)
            self.map_li_checkbox[li] = widget
            self.signal_map_list_checkbox.setMapping(widget, li)
            self.listlistwidget.addItem(item)
            self.listlistwidget.setItemWidget(item, widget)

    def onListCheckboxChanged(self, idx):
        if self.map_li_checkbox[idx].isChecked():
            self.mgr.enabled_list.add(idx)
        else:
            self.mgr.enabled_list.remove(idx)

    def onPassClicked(self, event):
        self.uiPassWord(True)
        self.uiSwitchWord()

    def onRemainClicked(self, event):
        if not self.meanText.text():
            self.showMeaning()
        else:
            self.uiPassWord(False)
            self.uiSwitchWord()

    def showMeaning(self):
        if self.mgr.current_word is not None:
            self.meanText.setText(self.mgr.current_word[4])

    def uiSwitchWord(self):
        word, flag = self.mgr.switch_word()
        if word:
            if self.showCheck.isChecked():
                self.showMeaning()
            else:
                self.meanText.setText('')
            self.mainText.setText(word[1])
            self.pronText.setText(word[3])

            if flag:
                self.currentRemainList.clear()
                self.nextRoundList.clear()
                for word in self.mgr.current_remain:
                    item = QListWidgetItem()
                    self.currentRemainList.addItem(item)
                    self.currentRemainList.map_word_item[word[1]] = item
                    self.currentRemainList.setItemWidget(item, QLabel(word[1]))

            item = self.currentRemainList.map_word_item[word[1]]
            self.currentRemainList.removeItemWidget(item)
            self.currentRemainList.takeItem(self.currentRemainList.row(item))

        self.currentlcd.display(len(self.mgr.current_remain))
        self.nextlcd.display(len(self.mgr.next_round))

    def uiPassWord(self, finished):
        word = self.mgr.pass_word(finished)
        if finished:
            item = QListWidgetItem()
            self.finishedList.addItem(item)
            self.finishedList.map_word_item[word[1]] = item
            self.finishedList.setItemWidget(item, QLabel(word[1]))
        else:
            item = QListWidgetItem()
            self.nextRoundList.addItem(item)
            self.nextRoundList.map_word_item[word[1]] = item
            self.nextRoundList.setItemWidget(item, QLabel(word[1]))

    def setupUi(self, MainWindow):
        super(MyMainWindow, self).setupUi(self)
        self.finishedList = MyListWidget(self, self.centralwidget)
        self.finishedList.setGeometry(QtCore.QRect(580, 120, 91, 241))
        self.finishedList.setObjectName("finishedList")
        self.currentRemainList = MyListWidget(self, self.centralwidget)
        self.currentRemainList.setGeometry(QtCore.QRect(460, 120, 91, 241))
        self.currentRemainList.setObjectName("currentRemainList")
        self.nextRoundList = MyListWidget(self, self.centralwidget)
        self.nextRoundList.setGeometry(QtCore.QRect(700, 120, 91, 241))
        self.nextRoundList.setObjectName("nextRoundList")
        self.passbtn.clicked.connect(self.onPassClicked)
        self.remainbtn.clicked.connect(self.onRemainClicked)
        self.list_map = {
            "finishedList": 'finished',
            "currentRemainList": 'current_remain',
            "nextRoundList": 'next_round',
        }

    def drag(self, from_, to, word):
        wordli = self.mgr.words.set_index('word').loc[word].to_list()
        wordli.insert(1, word)
        getattr(self.mgr, self.list_map[from_]).remove(wordli)
        getattr(self.mgr, self.list_map[to]).append(wordli)
        # print(len(self.mgr.current_remain))
        # print(len(self.mgr.finished))
        # print(len(self.mgr.next_round))
        self.currentlcd.display(len(self.mgr.current_remain))
        self.nextlcd.display(len(self.mgr.next_round))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyMainWindow()
    win.show()
    sys.exit(app.exec_())
