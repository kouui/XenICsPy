import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QVBoxLayout, QTabWidget

from xenicsPanel import XenicsPanel
from observePanel import ObservePanel


class Tab(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.parent = parent

        mainLayout = QVBoxLayout()

        #--- initialize tab screen
        tabs = QTabWidget()
        xenics = XenicsPanel(self)
        observe = ObservePanel(self)

        #--- add tabs
        for tab, name in zip([xenics,observe],
                            ["XenICs","Observation"]):
            tabs.addTab(tab, name)

        #--- add tabs to widget
        mainLayout.addWidget(tabs)
        self.setLayout(mainLayout)

    def setSelf(self, **kwags):
        for key, value in kwags.items():
            setattr(self, key, value)

if __name__=="__main__":
    app = QApplication(sys.argv)
    test = Tab(parent=None)
    test.show()
    sys.exit(app.exec_())
