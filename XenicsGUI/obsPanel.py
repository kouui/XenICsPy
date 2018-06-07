import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QFrame
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit, QRadioButton, QButtonGroup
from PyQt5.QtWidgets import QSizePolicy

class ObsPanel(QFrame):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)

        self.parent = parent

        self.setFrameShape(QFrame.Box)
        self.setFrameShadow(QFrame.Sunken)
        mainLayout = QVBoxLayout()

        #-- title
        #title = QLabel(">>>---  Observation  ---<<<", self)
        #title.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        #title.setAlignment(QtCore.Qt.AlignCenter)

        #-- external trigger
        layoutExttrig = self.makeExtrig()
        #-- polarity
        layoutPolarity = self.makePolarity()
        #-- get image
        layoutGetImage = self.makeGetImage()
        #-- observation
        layoutObserve = self.makeObserve()
        #-- outdir
        layoutOutdir = self.makeOutdir()
        #-- filename
        layoutFilename = self.makeFilename()
        #-- load, fitsheader
        layoutLoad = self.makeLoad()

        #-- add layout and widget
        mainLayout.addLayout(layoutExttrig)
        mainLayout.addLayout(layoutPolarity)
        mainLayout.addLayout(layoutGetImage)
        mainLayout.addLayout(layoutObserve)
        mainLayout.addLayout(layoutOutdir)
        mainLayout.addLayout(layoutFilename)
        mainLayout.addLayout(layoutLoad)

        self.setLayout(mainLayout)

    def makeExtrig(self):

        label = QLabel("ExTrig   ->",self)
        nonTrig = QRadioButton("Non",self);nonTrig.setChecked(True)
        extTrig = QRadioButton("Ext",self)
        group = QButtonGroup(self)
        for item in (nonTrig,extTrig): group.addButton(item)

        layout = QHBoxLayout()
        for item in (label,nonTrig,extTrig):
            layout.addWidget(item,alignment=QtCore.Qt.AlignLeft)
            item.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)

        return layout

    def makePolarity(self):

        label = QLabel("Polarity ->",self)
        negPolar = QRadioButton("Neg",self);negPolar.setChecked(True)
        posPolar = QRadioButton("Pos",self)
        group = QButtonGroup(self)
        for item in (negPolar,posPolar): group.addButton(item)

        layout = QHBoxLayout()
        for item in (label,negPolar,posPolar):
            layout.addWidget(item,alignment=QtCore.Qt.AlignLeft)
            item.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)

        return layout

    def makeGetImage(self):

        label = QLabel("nimg",self)
        nimg = QLineEdit("1",self); nimg.setMaxLength(3)
        get = QPushButton("Get",self)
        prof = QPushButton("Prof",self)
        rev = QPushButton("Rev",self)
        save = QPushButton("Save",self)


        layout = QHBoxLayout()
        for item in (label,nimg,get,prof,rev,save):
            layout.addWidget(item,alignment=QtCore.Qt.AlignLeft)
            item.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)

        return layout

    def makeObserve(self):

        label1 = QLabel("Cadence (sec):",self)
        cadence = QLineEdit("1.0",self)
        label2 = QLabel("Observe:",self)
        start = QPushButton("Start", self)
        start.setToolTip('click here to start observation')
        stop= QPushButton("stop", self)
        stop.setToolTip('click here to start observation')

        layout = QHBoxLayout()
        for item in (label1,cadence,label2,start,stop):
            layout.addWidget(item,alignment=QtCore.Qt.AlignLeft)
            item.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)

        return layout

    def makeOutdir(self):

        label1 = QLabel("Outdir:",self)
        outdir = QLineEdit("None",self)
        label2 = QLabel("        prefix:",self)
        prefix = QLineEdit("xeva_",self)

        layout = QHBoxLayout()
        for item in (label1,outdir,label2,prefix):
            layout.addWidget(item,alignment=QtCore.Qt.AlignLeft)
            item.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)

        return layout

    def makeFilename(self):

        label1 = QLabel("Filename:", self)
        filename = QLineEdit("xeva_20180607T150505_194",self)
        label2 = QLabel(".fits",self)

        layout = QHBoxLayout()
        for item in (label1,filename,label2):
            layout.addWidget(item,alignment=QtCore.Qt.AlignLeft)
            item.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)

        return layout

    def makeLoad(self):

        load = QPushButton("Load",self)
        fitsHeader = QPushButton("Fits Header",self)

        layout = QHBoxLayout()
        for item in (load,fitsHeader):
            layout.addWidget(item,alignment=QtCore.Qt.AlignLeft)
            item.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)

        return layout

    def setSelf(self, **kwags):
        for key, value in kwags.items():
            setattr(self, key, value)


if __name__=="__main__":
    app = QApplication(sys.argv)
    test = ObsPanel(parent=None)
    test.show()
    sys.exit(app.exec_())
