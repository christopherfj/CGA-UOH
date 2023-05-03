import sys
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5 import QtOpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np

#Ventana clase OpenGL
class Viewer3DWidget(QtOpenGL.QGLWidget):
    def __init__(self, parent=None):
        QtOpenGL.QGLWidget.__init__(self, parent)
        self.color = [255,0,0]
        self.opcion = 'Limpiar'
    #Funciones protegidas OpenGL
    def paintGL(self):
        glLoadIdentity()
        glMatrixMode( GL_MODELVIEW );
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glEnable(GL_DEPTH_TEST)
        self.dibujar()
        glFlush()
    def resizeGL(self, widthInPixels, heightInPixels):
        glViewport(0, 0, widthInPixels, heightInPixels)
    def initializeGL(self):
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClearDepth(1.0)
    #Metodos-seleccion
    def dibujar(self):
        glColor3fv(self.color)
        if self.opcion == 'Circulo':
            self.circulo()
    #Metodos-figuras
    def circulo(self):
        glBegin(GL_LINE_LOOP)
        xr,yr = 0,0
        r = 1.0
        for grados in range(0,360+1):
            theta = np.pi*grados/180
            x = xr+r*np.cos(theta)
            y = yr+r*np.sin(theta)
            glVertex2f( x, y )
        glEnd()  
            
#Ventana principal
class Ventana(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('main.ui')
        self.ui.setWindowIcon(QtGui.QIcon('uoh.jpg'))
        self.ui.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
        self.viewer3D = Viewer3DWidget(self)
        self.ui.OpenGLLayout.addWidget( self.viewer3D  )
        self.ui.show()
        #variables
        #signals
        self.ui.circulo.clicked.connect(self.circulo)
        self.ui.limpiar.clicked.connect(self.limpiar)
    #slots
    @pyqtSlot()
    def circulo(self):
        self.viewer3D.opcion = 'Circulo'
        self.viewer3D.updateGL() 
    @pyqtSlot()
    def limpiar(self):
        self.viewer3D.opcion = 'Limpiar'
        self.viewer3D.updateGL() 
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana = Ventana()
    sys.exit(app.exec_())

