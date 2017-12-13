from ui_form import Ui_MainWindow

from PyQt4 import QtGui
from PyQt4 import QtCore
from guiqwt.curve import CurvePlot
from guiqwt.plot import PlotManager
from guiqwt.builder import make
import os
import cv2


class UI(QtGui.QMainWindow):
    def __init__(self,parent = None):
        super(UI, self).__init__(parent)
        self.ui_obj = None
        self.y_position = 0
        self.slider_pos = 0
        self.image_temp = None
        self.image_w = 0
        self.image_h = 0
        self.image_path = None
        self.ui_init()
        self.init_connect()
        self.plot_init()



    def ui_init(self):
        self.ui_obj = Ui_MainWindow()
        self.ui_obj.setupUi(self)

    def init_connect(self):
        self.connect(self.ui_obj.y_verticalSlider, QtCore.SIGNAL('valueChanged(int)'),
                     self.plot_line_gray)
        self.ui_obj.open_image_button.clicked.connect(self.open_image)
        self.ui_obj.save_plot_button.clicked.connect(self.save_image)

    def open_image(self):
        self.file_name = QtGui.QFileDialog.getOpenFileName(self, "open file dialog", "C:\Users\Administrator\Desktop","*.jpg *.png")
        print self.file_name
        if self.file_name != "":
        # if self.ui_obj.image_path_lineEdit.text() != "":
        #     self.image_path = self.ui_obj.image_path_lineEdit.text()
            self.image_path = self.file_name
            if os.path.exists(self.image_path):
                self.display_image()
            else:
                # self.image_clean()
                print "path is not exists!!\n"
        else:
            # self.image_clean()
            print "pls fill imagepath\n"


    def save_image(self):
        pass

    def image_clean(self):
        self.image_temp = None
        self.image_w = 0
        self.image_h = 0

    def display_image(self):
        # print "cv2 imread path :"+str(self.image_path)
        self.image_temp = cv2.imread(str(self.image_path))
        self.image_h = len(self.image_temp)
        self.image_w = len(self.image_temp[0])
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

    def plot_init(self):
        self.manager = PlotManager(self)
        self.plots = []
        self.plot = CurvePlot(xlabel="", ylabel="")
        # self.plot.axisScaleDraw(CurvePlot.Y_LEFT).setMinimumExtent(10)
        self.manager.add_plot(self.plot)
        self.plots.append(self.plot)
        self.plot.plot_id = id(self.plot)
        self.curve = make.curve([0], [0], color="blue", title="gray value")
        self.plot.add_item(self.curve)
        self.plot.add_item(make.legend("TR"))
        self.ui_obj.line_info_display.addWidget(self.plot)

    def plot_line_gray(self):
        self.slider_pos = self.ui_obj.y_verticalSlider.value()
        # print"print line ",self.slider_pos
        # print type(self.slider_pos), len(self.image_temp)
        self.y_position = (100 - self.slider_pos) * (int(self.image_h)/100)
        print"y_position:", self.y_position

        line = [self.image_temp[self.y_position][i][1] for i in range(len(self.image_temp[self.y_position]))]
        print len(line), [i for i in range(len(line))]
        self.plot.set_axis_limits('left', 0, 255)
        self.plot.set_axis_limits('bottom', 0, self.image_w)
        self.curve.set_data([i for i in range(len(line))], line)
        self.plot.replot()


        # print "image :", self.image_temp[3]



    def blur(self,kernel):
        pass


    def nosie(self,method):
        pass