import sys
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
import numpy as np
import cv2

class Ventana(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.ui = uic.loadUi('mainWindow.ui')
        self.ui.setWindowIcon(QtGui.QIcon('uoh.jpg'))
        self.ui.show()
        
        #signals   
        self.ui.abrir.triggered.connect(self.abrir)
        self.ui.cerrar.triggered.connect(self.cerrar) 
        self.ui.draw.clicked.connect(self.mostrar)
   
    #slots
    @pyqtSlot()
    def abrir(self):
        path, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Abrir archivo', '.') 
        img = cv2.imread(path)
        img = cv2.resize( img, (301,301) )
        self.rgb =  cv2.cvtColor( img, cv2.COLOR_BGR2RGB ) 
        self.gray = cv2.cvtColor(self.rgb, cv2.COLOR_RGB2GRAY)
        th = 100
        ret, self.bw = cv2.threshold(self.gray, th, 255, cv2.THRESH_BINARY)
        self.height, self.width, self.channel = self.rgb.shape
    @pyqtSlot()
    def cerrar(self):
        self.ui.close()
    @pyqtSlot()
    def mostrar(self):
        if self.ui.color.currentText() == 'RGB': 
            qim = QtGui.QImage(self.rgb.data, self.width, self.height, 3*self.width, QtGui.QImage.Format_RGB888)
        elif self.ui.color.currentText() == 'Gris': 
            qim = QtGui.QImage(self.gray.data, self.width, self.height, 1*self.width, QtGui.QImage.Format_Indexed8)
        else:
            qim = QtGui.QImage(self.bw.data, self.width, self.height, 1*self.width, QtGui.QImage.Format_Indexed8) 
        pix = QtGui.QPixmap.fromImage(qim)
        self.ui.view.setPixmap(pix)

app = QtWidgets.QApplication(sys.argv)
ventana = Ventana()
sys.exit(app.exec())
