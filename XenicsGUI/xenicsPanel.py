import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QFrame
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit, QRadioButton, QButtonGroup
from PyQt5.QtWidgets import QSizePolicy

class XenicsPanel(QFrame):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)

        self.parent = parent

        self.setFrameShape(QFrame.Box)
        self.setFrameShadow(QFrame.Sunken)
        mainLayout = QVBoxLayout()

        #-- title
        title = QLabel(">>>---  XenICs  ---<<<", self)
        title.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        title.setAlignment(QtCore.Qt.AlignCenter)
        #title.setStyleSheet("QLabel {background-color: red;}")


        #-- preview part
        layoutPreview = self.makePreview()

        #-- Flip and Cut
        layoutFlipCut = self.makeFlipAndCut()

        #-- scale panel
        layoutScale = self.makeScale()

        #-- add layout and widget
        mainLayout.addWidget(title)
        mainLayout.addLayout(layoutPreview)
        mainLayout.addLayout(layoutFlipCut)
        mainLayout.addLayout(layoutScale)

        #-- set layout
        self.setLayout(mainLayout)

    def makePreview(self):

        layout = QHBoxLayout()

        label1 = QLabel("Exposure (ms):", self)
        label2 = QLabel("Preview :", self)

        #-- exposure
        expLE = QLineEdit("1000")

        #-- start button
        start = QPushButton("Start", self)
        start.setToolTip('click here to start preview')

        #-- stop button
        stop = QPushButton("Stop", self)
        stop.setToolTip('click here to stop preview')

        #-- adding to layout
        for item in (label1, expLE, label2, start, stop):
            layout.addWidget(item)
            label1.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)

        #-- set attributes
        self.setSelf(start=start, stop=stop, expLE=expLE)
        return layout

    def makeScale(self):

        layout = QVBoxLayout()
        layout1 = QHBoxLayout()
        layout2 = QHBoxLayout()

        label1 = QLabel("Scale:", self)

        #-- radiobuttuns
        autoScale = QRadioButton("Auto", self); autoScale.setChecked(True)
        logScale = QRadioButton("Log", self)
        clipScale = QRadioButton("Clip: ", self)

        group=QButtonGroup(self)
        for item in (autoScale,logScale,clipScale):
            group.addButton(item)

        #-- clip value
        label2 = QLabel("Max:", self)
        clipScaleMax = QLineEdit("0")
        label3 = QLabel("Min:", self)
        clipScaleMin = QLineEdit("10000")

        #-- adding to layout
        for item in (label1,autoScale,logScale,clipScale):
            layout1.addWidget(item)
            item.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        for item in (label2,clipScaleMax,label3,clipScaleMin):
            layout2.addWidget(item)
            item.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)

        layout.addLayout(layout1)
        layout.addLayout(layout2)
        return layout

    def makeFlipAndCut(self):

        layout = QVBoxLayout()

        #-- row 1
        layout1 = QHBoxLayout()
        NoFlip = QRadioButton("No Flip", self); NoFlip.setChecked(True)
        FlipX = QRadioButton("Flip-X", self)
        FlipY = QRadioButton("Flip-Y", self)
        group=QButtonGroup(self)
        for item in (NoFlip, FlipX, FlipY):
            group.addButton(item)

        full = QPushButton("Full", self)
        cbox = QPushButton("Cbox", self)

        for item in (NoFlip,FlipX,FlipY,full, cbox):
            layout1.addWidget(item)
            item.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)

        #-- row 2
        layout2 = QHBoxLayout()
        label1 = QLabel("X0:", self)
        X0 = QLineEdit("0")
        label2 = QLabel("Y0:", self)
        Y0 = QLineEdit("0")

        for item in (label1,X0,label2,Y0):
            item.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
            layout2.addWidget(item)

        #-- row 3
        layout3 = QHBoxLayout()
        label3 = QLabel("NX:", self)
        NX = QLineEdit("640")
        label4 = QLabel("NY:", self)
        NY = QLineEdit("512")

        for item in (label3,NX,label4,NY):
            item.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
            layout3.addWidget(item)

        layout.addLayout(layout1)
        layout.addLayout(layout2)
        layout.addLayout(layout3)
        return layout


    def setSelf(self, **kwags):
        for key, value in kwags.items():
            setattr(self, key, value)


if __name__=="__main__":
    app = QApplication(sys.argv)
    test = XenicsPanel(parent=None)
    test.show()
    sys.exit(app.exec_())
