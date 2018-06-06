import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QTextEdit, QPushButton, QLabel

import time


class PreviewPanel(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)

        self.parent = parent

        mainLayout = QHBoxLayout()

        label = QLabel("Preview : ",self)

        #-- preview start button
        start = QPushButton("Start", self)
        start.setToolTip('click here to start preview')
        start.clicked.connect(self.previewStart)

        #-- preview stop button
        stop = QPushButton("stop", self)
        stop.setEnabled(False)
        stop.setToolTip('click here to stop preview')
        stop.clicked.connect(self.previewStop)

        #--- setup layout
        for item in (label, start, stop):
            mainLayout.addWidget( item )

        self.setLayout(mainLayout)

        #-- set self
        self.setSelf(start=start, stop=stop)

    def previewStart(self, event):

        #self.parent.logWidget.insertPlainText("preview started. \n")
        self.start.setEnabled(False);self.stop.setEnabled(True)


    def previewStop(self, event):

        #self.parent.logWidget.insertPlainText("preview stopped. \n")
        self.start.setEnabled(True);self.stop.setEnabled(False)

    def setSelf(self, **kwags):
        for key, value in kwags.items():
            setattr(self, key, value)






if __name__=="__main__":
    app = QApplication(sys.argv)
    test = PreviewPanel(parent=None)
    test.show()
    sys.exit(app.exec_())
