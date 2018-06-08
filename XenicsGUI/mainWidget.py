import sys
from datetime import datetime

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QTextEdit, QPushButton

from tabs import Tab
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
        control = Tab(self)

        #--- log
        log = QTextEdit()
        log.setReadOnly(True)

        # setup layout
        layout_v.addWidget(control)
        layout_v.addWidget(log)

        mainLayout.addLayout(layout_v, stretch=3)
        mainLayout.addWidget(figure,stretch=5)

        self.setLayout(mainLayout)

        #-- set self
        self.setSelf(figure=figure,log=log)
        self.showTextInLog("Software initialized.")

    def setSelf(self, **kwags):
        for key, value in kwags.items():
            setattr(self, key, value)

    def datetime2String(self, t=datetime.now()):
        return t.strftime("%Y-%m-%d %H:%M:%S") + ".{}".format(t.microsecond)


    def showTextInLog(self,text):

        nowStr = self.datetime2String(t=datetime.now())
        self.log.insertPlainText("{} : {} \n".format(nowStr, text))



if __name__=="__main__":
    app = QApplication(sys.argv)
    test = MainWidget(parent=None)
    test.show()
    sys.exit(app.exec_())
