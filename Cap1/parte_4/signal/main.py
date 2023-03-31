import sys
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
import numpy as np

class Ventana(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.ui = uic.loadUi('main.ui')
        self.ui.setWindowIcon(QtGui.QIcon('uoh.jpg'))
        self.ui.show()
        
        #data
        Fs = 5e+3
        Ts = 1/Fs
        self.f0 = 50
        t0 = 1/self.f0
        self.t = np.arange(0,t0+Ts,Ts)
        self.color_options = {'Rojo': [255,0,0], 'Verde': [0,255,0], 'Azul':[0,0,255]}
        self.pen = [255, 0, 0]
        self.A = self.ui.amplitud.value()

        #Promoted class name: GraphicsLayoutWidget
        #Header file: pyqtgraph
        self.widget_plot = self.ui.view.addPlot()
        self.widget_plot.setXRange( 0, t0 )
        self.widget_plot.setLabel(axis = 'bottom', text='Tiempo [s]')
        self.widget_plot.setLabel(axis = 'left', text='Amplitud [u]')
        self.curve = self.widget_plot.plot([], pen=self.pen)
        self.ui.value.setText(str(self.ui.amplitud.value()))

        #signals   
        self.ui.sin.toggled.connect(self.sin)     
        self.ui.cos.toggled.connect(self.cos)   
        self.ui.color.currentIndexChanged.connect(self.color)
        self.ui.clear.clicked.connect(self.clear)   
        self.ui.amplitud.valueChanged.connect(self.amplitud)
        
    #slots
    @pyqtSlot()
    def sin(self):
        self.y = self.A*np.sin(2*np.pi*self.f0*self.t)
        self.plot()
    @pyqtSlot()
    def cos(self):
        self.y = self.A*np.cos(2*np.pi*self.f0*self.t)
        self.plot()
    @pyqtSlot()
    def color(self):
        self.pen = self.color_options[self.ui.color.currentText()]
        self.plot()
    @pyqtSlot()
    def clear(self):
        self.curve.setData([], [])
    @pyqtSlot()
    def amplitud(self):
        self.ui.value.setText(str(self.ui.amplitud.value()))
        self.A = self.ui.amplitud.value()
        if self.ui.sin.isChecked():
            self.sin()
        elif self.ui.cos.isChecked():
            self.cos()
        
    #metodos
    def plot(self):
        self.curve.setData(self.t, self.y, pen = self.pen)
        
app = QtWidgets.QApplication(sys.argv)
ventana = Ventana()
sys.exit(app.exec())

