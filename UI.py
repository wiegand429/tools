from ui_form import Ui_MainWindow
from PyQt4 import QtGui
from PyQt4 import QtCore
import os
import cv2

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
                # print "cv2 imread path :"+str(self.image_path)
                # image = cv2.imread(str(self.image_path))
                # #print image.shape[1],image.shape[0]
                # #print self.ui_obj.picture_display.width(),self.ui_obj.picture_display.height()
                # qimage = QtGui.QImage(image, image.shape[1], image.shape[0], QtGui.QImage.Format_RGB888)
                # qimage_resize = qimage.scaled(self.ui_obj.picture_display.width(), self.ui_obj.picture_display.height(), 0, 0)
                # self.ui_obj.picture_display.setPixmap(QtGui.QPixmap.fromImage(qimage_resize))
                # self.ui_obj.picture_display.show()

                pixmap = QtGui.QPixmap()
                pixmap.load(str(self.image_path))
                newpixmap = pixmap.scaled(self.ui_obj.picture_display.width(), self.ui_obj.picture_display.height(), 0, 0)
                self.ui_obj.picture_display.setPixmap(newpixmap)
                self.ui_obj.picture_display.setAlignment(QtCore.Qt.AlignCenter)
                self.ui_obj.picture_display.show()



            else:
                print "path is not exists!!\n"
        else:
            print "pls fill imagepath\n"


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