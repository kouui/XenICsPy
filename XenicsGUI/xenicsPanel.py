import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QFrame
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit, QRadioButton, QButtonGroup,QCheckBox
from PyQt5.QtWidgets import QSizePolicy

class XenicsPanel(QFrame):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)

        self.parent = parent

        self.setFrameShape(QFrame.Box)
        self.setFrameShadow(QFrame.Sunken)
        mainLayout = QVBoxLayout()

        #-- title
        #title = QLabel(">>>---  XenICs  ---<<<", self)
        #title.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        #title.setAlignment(QtCore.Qt.AlignCenter)
        #title.setStyleSheet("QLabel {background-color: red;}")


        #-- preview
        layoutPreview = self.makePreview()

        #-- Flip and Cut
        layoutFlipCut = self.makeFlipAndCut()

        #-- scale
        layoutScale = self.makeScale()

        #-- temperature
        layoutTemp = self.makeTemperature()

        #-- setting file
        layoutSet = self.makeSettingFile()

        #-- add layout and widget
        for item in (layoutPreview,layoutFlipCut,layoutScale,layoutTemp,layoutSet):
            mainLayout.addLayout(item)

        #-- set layout
        self.setLayout(mainLayout)


    def makePreview(self):

        label1 = QLabel("Exposure (ms):", self)
        label2 = QLabel("Preview :", self)

        #-- exposure
        exposure = QLineEdit("1000");exposure.setMaxLength(4);exposure.setFixedWidth(40)

        #-- preview button
        start = QPushButton("Start", self)
        start.setToolTip('click here to start preview')
        stop= QPushButton("stop", self)
        stop.setToolTip('click here to start preview')

        #-- adding to layout
        layout = QHBoxLayout();layout.setAlignment(QtCore.Qt.AlignLeft)
        for item in (label1, exposure, label2, start, stop):
            layout.addWidget(item,alignment=QtCore.Qt.AlignLeft)
            item.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        #-- set attributes
        self.setSelf(start=start, stop=stop, exposure=exposure)
        return layout

    def makeFlipAndCut(self):

        #-- row 1
        layout1 = QHBoxLayout();layout1.setAlignment(QtCore.Qt.AlignLeft)

        NoFlip = QRadioButton("No Flip", self); NoFlip.setChecked(True)
        FlipX = QRadioButton("Flip-X", self)
        FlipY = QRadioButton("Flip-Y", self)
        group=QButtonGroup(self)
        for item in (NoFlip, FlipX, FlipY):
            group.addButton(item)

        full = QPushButton("Full", self)
        cbox = QPushButton("Cbox", self)

        for item in (NoFlip,FlipX,FlipY,full, cbox):
            layout1.addWidget(item,alignment=QtCore.Qt.AlignLeft)
            item.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        #-- row 2
        layout2 = QHBoxLayout();layout2.setAlignment(QtCore.Qt.AlignLeft)
        label1 = QLabel("X0:", self)
        X0 = QLineEdit("0");X0.setMaxLength(4);X0.setFixedWidth(40)
        label2 = QLabel("Y0:", self)
        Y0 = QLineEdit("0");Y0.setMaxLength(4);Y0.setFixedWidth(40)
        label3 = QLabel("NX:", self)
        NX = QLineEdit("640");NX.setMaxLength(4);NX.setFixedWidth(40)
        label4 = QLabel("NY:", self)
        NY = QLineEdit("512");NY.setMaxLength(4);NY.setFixedWidth(40)

        for item in (label1,X0,label2,Y0, label3,NX,label4,NY):
            item.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            layout2.addWidget(item,alignment=QtCore.Qt.AlignLeft)

        layout = QVBoxLayout()
        for item in (layout1,layout2):
            layout.addLayout(item)
        return layout

    def makeScale(self):

        layout = QHBoxLayout();layout.setAlignment(QtCore.Qt.AlignLeft)

        #label1 = QLabel("Scale:", self)

        #-- radiobuttuns
        autoScale = QRadioButton("Auto", self); autoScale.setChecked(True)
        logScale = QRadioButton("Log", self)
        clipScale = QRadioButton("Clip: ", self)
        #-- clip value
        label2 = QLabel("Max:", self)
        clipScaleMax = QLineEdit("0");clipScaleMax.setMaxLength(5);clipScaleMax.setFixedWidth(50)
        label3 = QLabel("Min:", self)
        clipScaleMin = QLineEdit("10000");clipScaleMin.setMaxLength(5);clipScaleMin.setFixedWidth(50)

        group=QButtonGroup(self)
        for item in (autoScale,logScale,clipScale):
            group.addButton(item)


        #-- adding to layout
        for item in (autoScale,logScale,clipScale, label2,clipScaleMax,label3,clipScaleMin):
            layout.addWidget(item,alignment=QtCore.Qt.AlignLeft)
            item.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        return layout

    def makeTemperature(self):

        #-- row 1
        label1 = QLabel("current Camera Temperature (C)", self)
        readTemp = QLineEdit("24.65", self);readTemp.setMaxLength(6);readTemp.setFixedWidth(60)
        readTemp.setReadOnly(True)
        cooling = QCheckBox("Cooling",self)

        layout1 = QHBoxLayout();layout1.setAlignment(QtCore.Qt.AlignLeft)
        for item in (label1,readTemp,cooling):
            layout1.addWidget(item,alignment=QtCore.Qt.AlignLeft)
            item.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        #-- row 2
        label2 = QLabel("Temperature (C) : Set",self)
        setTemp = QLineEdit("-25.00", self);setTemp.setMaxLength(6);setTemp.setFixedWidth(60)
        label3 = QLabel("Offset",self)
        offsetTemp = QLineEdit("63.50",self);offsetTemp.setMaxLength(6);offsetTemp.setFixedWidth(60)
        empty = QLabel(" ",self)

        layout2 = QHBoxLayout();layout2.setAlignment(QtCore.Qt.AlignLeft)
        for item in (label2,setTemp,label3,offsetTemp):
            layout2.addWidget(item,alignment=QtCore.Qt.AlignLeft)
            item.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        layout = QVBoxLayout()
        layout.addLayout(layout1)
        layout.addLayout(layout2)

        return layout

    def makeSettingFile(self):

        label1 = QLabel("Config:",self)
        config = QLineEdit("None", self)
        loadConfig = QPushButton("Load",self)
        saveConfig = QPushButton("Save as",self)

        layout = QHBoxLayout();layout.setAlignment(QtCore.Qt.AlignLeft)
        for item in (label1,config, loadConfig, saveConfig):
            layout.addWidget(item,alignment=QtCore.Qt.AlignLeft)
            item.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        return layout

    def setSelf(self, **kwags):
        for key, value in kwags.items():
            setattr(self, key, value)


if __name__=="__main__":
    app = QApplication(sys.argv)
    test = XenicsPanel(parent=None)
    test.show()
    sys.exit(app.exec_())
