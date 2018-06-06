import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QTextEdit, QPushButton

from controlPanel import ControlPanel
from figurePanel import MyMplCanvas


class MainWidget(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)

        self.parent = parent

        mainLayout = QHBoxLayout()
        layout_v = QVBoxLayout()

        #--- figure
        figure = MyMplCanvas(parent=self, width=6, height=6, isAxis=False)
        self.figure = figure

        #---control panel
        control = ControlPanel(self)

        #--- log
        self.logWidget = QTextEdit()
        self.logWidget.setReadOnly(True)
        self.logWidget.insertPlainText("software initialized. \n")

        # setup layout
        layout_v.addWidget(control, stretch=5)
        layout_v.addWidget(self.logWidget, stretch=3)

        mainLayout.addLayout(layout_v, stretch=3)
        mainLayout.addWidget(figure,stretch=5)

        self.setLayout(mainLayout)



if __name__=="__main__":
    app = QApplication(sys.argv)
    test = MainWidget(parent=None)
    test.show()
    sys.exit(app.exec_())