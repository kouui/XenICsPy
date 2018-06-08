"""
author : kouui
date : 2018-06
"""

import sys
from datetime import datetime

from PyQt5.QtWidgets import QApplication, QMainWindow, QAction

from mainWidget import MainWidget


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.title = "Observation"
        self.left = 100
        self.top = 100
        self.width = 1100
        self.height = 700

        self.initUI()

    def initUI(self):

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setFixedSize(self.width,self.height)

        #--- add statusbar
        self.statusBar().showMessage("No message from statusbar!")

        #--- add menuBar
        self.addMenuBar()


        #--- layout
        self.mainWidget = MainWidget(self)
        self.setCentralWidget(self.mainWidget)

        self.show()

    def addMenuBar(self):

        mainMenu = self.menuBar()

        """
        if is macOS then turn off the native menubar
        otherwise it will be covered by the systems menubar
        """
        if sys.platform=="darwin":
            mainMenu.setNativeMenuBar(False)

        #--- add menu into menubar
        fileMenu = mainMenu.addMenu("File")

        #--- add action into menu "File"
        exitAction = QAction("Exit", self)
        exitAction.setStatusTip("Exit Application")
        for action in [exitAction]:
            fileMenu.addAction(action)

        #--- define functionality of each action
        exitAction.triggered.connect(self.close)

    def datetime2String(self, t=datetime.now()):
        return t.strftime("%Y-%m-%d %H:%M:%S") + ".{}".format(t.microsecond)


    def showTextInLog(self,text):

        nowStr = self.datetime2String(t=datetime.now())
        self.mainWidget.log.insertPlainText("{} : {} \n".format(nowStr, text))




if __name__=="__main__":
    app = QApplication(sys.argv)
    m = MainWindow()
    sys.exit(app.exec_())
