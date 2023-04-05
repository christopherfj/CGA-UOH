import sys
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtCore import pyqtSlot, Qt

class Ventana(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.ui = uic.loadUi('main.ui')
        self.ui.setWindowIcon(QtGui.QIcon('uoh.jpg'))
        self.ui.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
        self.ui.show()
        
        #signals
        self.ui.pushButton.clicked.connect(self.pushButton)     
        self.ui.radioButton.toggled.connect(self.radioButton)     
        self.ui.checkBox.stateChanged.connect(self.checkBox)     
        self.ui.comboBox.currentIndexChanged.connect(self.comboBox)     
        self.ui.spinBox.valueChanged.connect(self.spinBox)     
        self.ui.horizontalSlider.valueChanged.connect(self.horizontalSlider)     
        self.ui.menuBar.triggered.connect(self.menuBar)     

    #slots
    @pyqtSlot()
    def pushButton(self):
        self.ui.lineEdit.setText('lineEdit')
        print( self.ui.lineEdit.text() )
    @pyqtSlot()
    def radioButton(self):
        if self.ui.radioButton.isChecked():
            print('radioButton')
    @pyqtSlot()
    def checkBox(self):
        if self.ui.checkBox.isChecked():
            print('checkBox')
    @pyqtSlot()
    def comboBox(self):
        print(self.ui.comboBox.currentText())
    @pyqtSlot()
    def spinBox(self):
        print(self.ui.spinBox.value())
    @pyqtSlot()
    def horizontalSlider(self):
        self.ui.textLabel.setText( str(self.ui.horizontalSlider.value()) )
        print(self.ui.textLabel.text())
    @pyqtSlot()
    def menuBar(self):
        self.ui.close()
        
app = QtWidgets.QApplication(sys.argv)
ventana = Ventana()
sys.exit(app.exec())
