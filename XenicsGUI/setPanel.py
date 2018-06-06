import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QTextEdit, QPushButton, QLabel, QLineEdit

class SetPanel(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)

        self.parent = parent
        mainLayout = QHBoxLayout()

        label1 = QLabel("exposure (ms): ")

        #-- exposure
        expLE = QLineEdit("1000")
        expLE.editingFinished.connect(self.onEdit)

        #-- layout
        mainLayout.addWidget(label1, stretch=2)
        mainLayout.addWidget(expLE, stretch=4)

        self.setLayout(mainLayout)

        #-- set self
        self.setSelf(expLE=expLE)

    def onEdit(self):

        exp = int(self.expLE.text())
        self.parent.parent.logWidget.insertPlainText("exposure -> {} ms. \n".format(exp))

    def setSelf(self, **kwags):
        for key, value in kwags.items():
            setattr(self, key, value)


if __name__=="__main__":
    app = QApplication(sys.argv)
    test = SetPanel(parent=None)
    test.show()
    sys.exit(app.exec_())
