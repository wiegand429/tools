import os
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from  UI import UI
import cv2



if __name__ == '__main__':
   app = QtGui.QApplication(sys.argv)
   window = UI()
   window.show()
   sys.exit(app.exec_())


