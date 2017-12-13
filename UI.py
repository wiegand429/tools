from ui_form import Ui_MainWindow
from PyQt4 import QtGui
from PyQt4 import QtCore
import os

class UI(QtGui.QMainWindow):
    def __init__(self,parent = None):
        super(UI, self).__init__(parent)
        self.ui_obj = None
        self.y_position = 0
        self.slider_pos = 0
        self.image_path = None
        self.ui_init()
        self.init_connect()
    def ui_init(self):
        self.ui_obj = Ui_MainWindow()
        self.ui_obj.setupUi(self)

    def init_connect(self):
        self.connect(self.ui_obj.y_verticalSlider, QtCore.SIGNAL('valueChanged(int)'),
                     self.plot_line_gray)
        self.ui_obj.open_image_button.clicked.connect(self.open_image)
        self.ui_obj.save_plot_button.clicked.connect(self.save_image)

    def open_image(self):
        if self.ui_obj.image_path_lineEdit.text() != "":
            self.image_path = self.ui_obj.image_path_lineEdit.text()
            if os.path.exists(self.image_path):
                pass
            else:
                print "path is not exists!!\n"
        else:
            print "请输入图片路径\n"


        pass

    def save_image(self):
        pass

    def display_image(self):

        pass
    def plot_line_gray(self):
        self.slider_pos = self.ui_obj.y_verticalSlider.value()
        print"print line !  ",self.slider_pos

    def blur(self,kernel):
        pass
    def nosie(self,method):
        pass