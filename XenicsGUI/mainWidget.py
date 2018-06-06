import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QTextEdit, QPushButton

from xenicsPanel import XenicsPanel
from figurePanel import MyMplCanvas


class MainWidget(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)

        self.parent = parent

        mainLayout = QHBoxLayout()
        layout_v = QVBoxLayout()

        #--- figure
        figure = MyMplCanvas(parent=self, width=6, height=6, isAxis=False)

        #---control panel
        xenics = XenicsPanel(self)

        #--- log
        self.logWidget = QTextEdit()
        self.logWidget.setReadOnly(True)
        self.logWidget.insertPlainText("software initialized. \n")

        # setup layout
        layout_v.addWidget(xenics)
        layout_v.addWidget(self.logWidget)

        mainLayout.addLayout(layout_v, stretch=3)
        mainLayout.addWidget(figure,stretch=5)

        self.setLayout(mainLayout)

        #-- set self
        self.setSelf(figure=figure)

    def setSelf(self, **kwags):
        for key, value in kwags.items():
            setattr(self, key, value)



if __name__=="__main__":
    app = QApplication(sys.argv)
    test = MainWidget(parent=None)
    test.show()
    sys.exit(app.exec_())
