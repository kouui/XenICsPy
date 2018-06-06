from __future__ import unicode_literals

import matplotlib
# Make sure that we are using QT5
matplotlib.use('Qt5Agg')

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from PyQt5 import QtCore, QtWidgets

class MyMplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""

    def __init__(self, parent=None, width=6, height=6, dpi=100, isAxis=False):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        self.setPadding(fig)

        if not isAxis:
            self.axes.set_axis_off()

        self.compute_initial_figure()

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)



    def compute_initial_figure(self):
        pass

    def setPadding(self, fig):

        tight = {
            "pad": 0.2,     # default
            #"w_pad":0.2, # decreasing the horizontal padding between axes
        }
        fig.set_tight_layout(tight)
