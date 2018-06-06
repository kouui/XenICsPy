import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QTextEdit, QPushButton

from previewPanel import PreviewPanel


class ControlPanel(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)

        self.parent = parent

        mainLayout = QVBoxLayout()

        # setup layout

        preview = PreviewPanel(self.parent)

        mainLayout.addWidget(preview)

        self.setLayout(mainLayout)



if __name__=="__main__":
    app = QApplication(sys.argv)
    test = ControlPanel(parent=None)
    test.show()
    sys.exit(app.exec_())
