import sys
from datetime import datetime

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
        exposure = QLineEdit("1000");exposure.setMaxLength(4);exposure.setFixedWidth(40);exposure.name="exposure (ms)"
        exposure.editingFinished.connect(self.setIntValue)

        #-- preview button
        start = QPushButton("Start", self)
        start.setToolTip('click here to start preview')
        start.clicked.connect(self.buttonPress)
        stop = QPushButton("Stop", self);stop.setEnabled(False)
        stop.setToolTip('click here to start preview')
        stop.clicked.connect(self.buttonPress)

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
            item.toggled.connect(self.setFlip)
            group.addButton(item)

        full = QPushButton("Full", self)
        full.clicked.connect(self.buttonPress)
        cbox = QPushButton("Cbox", self)
        cbox.clicked.connect(self.buttonPress)

        for item in (NoFlip,FlipX,FlipY,full, cbox):
            layout1.addWidget(item,alignment=QtCore.Qt.AlignLeft)
            item.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        #-- row 2
        layout2 = QHBoxLayout();layout2.setAlignment(QtCore.Qt.AlignLeft)
        label1 = QLabel("X0:", self)
        X0 = QLineEdit("0");X0.setMaxLength(4);X0.setFixedWidth(40);X0.name="X0"
        label2 = QLabel("Y0:", self)
        Y0 = QLineEdit("0");Y0.setMaxLength(4);Y0.setFixedWidth(40);Y0.name="Y0"
        label3 = QLabel("NX:", self)
        NX = QLineEdit("640");NX.setMaxLength(4);NX.setFixedWidth(40);NX.name="NX"
        label4 = QLabel("NY:", self)
        NY = QLineEdit("512");NY.setMaxLength(4);NY.setFixedWidth(40);NY.name="NY"
        for item in (X0,Y0,NX,NY):
            item.editingFinished.connect(self.setIntValue)

        for item in (label1,X0,label2,Y0, label3,NX,label4,NY):
            item.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            layout2.addWidget(item,alignment=QtCore.Qt.AlignLeft)

        layout = QVBoxLayout()
        for item in (layout1,layout2):
            layout.addLayout(item)

        self.setSelf(X0=X0,Y0=Y0,NX=NX,NY=NY,full=full,cbox=cbox)
        for item in (X0,Y0,NX,NY, full):
            item.setEnabled(False)

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
        clipScaleMax = QLineEdit("10000");clipScaleMax.setMaxLength(5);clipScaleMax.setFixedWidth(50)
        label3 = QLabel("Min:", self)
        clipScaleMin = QLineEdit("0");clipScaleMin.setMaxLength(5);clipScaleMin.setFixedWidth(50)
        for item in (clipScaleMin,clipScaleMax):
            item.setEnabled(False)

        group=QButtonGroup(self)
        for item in (autoScale,logScale,clipScale):
            group.addButton(item)


        #-- adding to layout
        for item in (autoScale,logScale,clipScale, label3,clipScaleMin,label2,clipScaleMax):
            layout.addWidget(item,alignment=QtCore.Qt.AlignLeft)
            item.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        return layout

    def makeTemperature(self):

        #-- row 1
        label1 = QLabel("current Camera Temperature (C)", self)
        currentTemp = QLineEdit("24.65", self);currentTemp.setMaxLength(6);currentTemp.setFixedWidth(60)
        currentTemp.setReadOnly(True)
        cooling = QCheckBox("Cooling",self)

        layout1 = QHBoxLayout();layout1.setAlignment(QtCore.Qt.AlignLeft)
        for item in (label1,currentTemp,cooling):
            layout1.addWidget(item,alignment=QtCore.Qt.AlignLeft)
            item.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        #-- row 2
        label2 = QLabel("Temperature (C) : Set",self)
        setTemp = QLineEdit("-25.00", self);setTemp.setMaxLength(6);setTemp.setFixedWidth(60)
        label3 = QLabel("Offset",self)
        offsetTemp = QLineEdit("63.50",self);offsetTemp.setMaxLength(6);offsetTemp.setFixedWidth(60)

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


    def setIntValue(self):

        try:
            value = int(self.sender().text()) # ms
        except ValueError:
            self.showTextInLog("Input value must be an integer")
            return None

        self.showTextInLog("{} -->> {}".format(self.sender().name,value))

    def setFloatValue(self):

        pass

    def setStrValue(self):

        pass

    def buttonPress(self):

        sender = self.sender()

        if sender.text() == "Start":
            self.showTextInLog("Preview started.")
            self.start.setEnabled(False);self.stop.setEnabled(True)

        elif sender.text() == "Stop":
            self.showTextInLog("Preview stopped.")
            self.start.setEnabled(True);self.stop.setEnabled(False)

        elif sender.text() == "Full":

            self.cbox.setEnabled(True);self.full.setEnabled(False)
            for item in (self.X0,self.Y0,self.NX,self.NY):
                item.setEnabled(False)

            self.showTextInLog("View -->> {}".format(self.sender().text()))

        elif sender.text() == "Cbox":

            self.full.setEnabled(True);self.cbox.setEnabled(False)
            for item in (self.X0,self.Y0,self.NX,self.NY):
                item.setEnabled(True)

            self.showTextInLog("View -->> {}".format(self.sender().text()))

        else:
            return None

    def setFlip(self, event):

        if event == True:
            self.showTextInLog("Flip -->> {}".format(self.sender().text()))
        else :
            return None

    def setSelf(self, **kwags):
        for key, value in kwags.items():
            setattr(self, key, value)

    def datetime2String(self, t=datetime.now()):
        return t.strftime("%Y-%m-%d %H:%M:%S") + ".{}".format(t.microsecond)


    def showTextInLog(self,text):
        nowStr = self.datetime2String(t=datetime.now())
        self.parent.parent.log.insertPlainText("{} : {} \n".format(nowStr, text))




if __name__=="__main__":
    app = QApplication(sys.argv)
    test = XenicsPanel(parent=None)
    test.show()
    sys.exit(app.exec_())
