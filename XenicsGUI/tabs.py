import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QVBoxLayout, QTabWidget

from xenicsPanel import XenicsPanel
from obsPanel import ObsPanel


class Tab(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.parent = parent

        mainLayout = QVBoxLayout()

        #--- initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = XenicsPanel(self.parent)
        self.tab2 = ObsPanel(self.parent)

        #--- add tabs
        for tab, name in zip([self.tab1,self.tab2],
                            ["XenICs","Observation"]):
            self.tabs.addTab(tab, name)

        #--- add tabs to widget
        mainLayout.addWidget(self.tabs)
        self.setLayout(mainLayout)

if __name__=="__main__":
    app = QApplication(sys.argv)
    test = TabWidget(parent=None)
    test.show()
    sys.exit(app.exec_())
