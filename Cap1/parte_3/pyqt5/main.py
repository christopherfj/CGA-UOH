import sys
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot

class Ventana(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Hola mundo')
        self.resize(320,320)
        self.setWindowIcon(QtGui.QIcon('uoh.jpg'))
        
        w = self.frameGeometry().width()
        h = self.frameGeometry().height()
        
        self.l_name = QtWidgets.QLineEdit('Ingrese nombre', self)
        self.l_name.setGeometry( int(w/2-(200)/2), int(h/2-(20+20+20)/2), 200, 20 )
        
        b_quit = QtWidgets.QPushButton('Saludar', self)
        b_quit.setGeometry( int(w/2-(100)/2), int(h/2+(20+20+20)/2), 100, 20 )
        b_quit.clicked.connect(self.click)     
        
    @pyqtSlot()
    def click(self):
        value = self.l_name.text()
        self.l_name.setText( f'Hola {value}' )

app = QtWidgets.QApplication(sys.argv)
ventana = Ventana()
ventana.show()
sys.exit(app.exec())

