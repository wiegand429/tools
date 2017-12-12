from ui_designer import Ui_MainWindow
from PyQt4 import QtGui
from PyQt4 import QtCore

class UI(QtGui.QMainWindow):
    def __init__(self,parent = None):
        super(UI, self).__init__(parent)
        self.ui_obj = None
        self.ui_init()

    def ui_init(self):
        self.ui_obj = Ui_MainWindow()
        self.ui_obj.setupUi(self)
