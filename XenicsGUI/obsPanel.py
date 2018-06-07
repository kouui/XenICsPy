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
        title = QLabel(">>>---  Observation  ---<<<", self)
        title.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        title.setAlignment(QtCore.Qt.AlignCenter)

        #-- external trigger
        layoutExttrig = self.makeExtrig()
        #-- polarity
        layoutPolarity = self.makePolarity()
        #-- get image
        layoutGetImage = self.makeGetImage()

        #-- add layout and widget
        mainLayout.addWidget(title)
        mainLayout.addLayout(layoutExttrig)
        mainLayout.addLayout(layoutPolarity)
        mainLayout.addLayout(layoutGetImage)

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

        layout = QHBoxLayout()
        for item in (label,nimg):
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
