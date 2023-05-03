import sys
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5 import QtOpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

#Ventana clase OpenGL
class Viewer3DWidget(QtOpenGL.QGLWidget):
    def __init__(self, parent=None):
        QtOpenGL.QGLWidget.__init__(self, parent)
        self.color = [255,0,0]
        self.escalamiento = (1.0, 1.0)
        self.coords = [(0.0, 0.5), (0.5,-0.5), (-0.5,-0.5)]
        self.fijo = (0,0)
    #Funciones protegidas OpenGL
    def paintGL(self):
        glLoadIdentity()
        glMatrixMode( GL_MODELVIEW )
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )
        glEnable(GL_DEPTH_TEST)
        self.dibujar()
        glFlush()
    def resizeGL(self, widthInPixels, heightInPixels):
        aspect = widthInPixels / heightInPixels
        print('Razon:', aspect)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        if widthInPixels >= heightInPixels:
            gluOrtho2D(-1.0 * aspect, 1.0 * aspect, -1.0, 1.0)
        else:
            gluOrtho2D(-1.0, 1.0, -1.0 / aspect, 1.0 / aspect)            
        print('Desde clase OpenGL:', widthInPixels, heightInPixels)
        glViewport(0, 0, widthInPixels, heightInPixels)
    def initializeGL(self):
        glClearColor(1.0, 1.0, 1.0, 1.0) #Blanco
        glClearDepth(1.0)
    #Metodos-seleccion
    def dibujar(self):
        glColor3fv(self.color)
        self.triangulo()
    #Metodos-figuras
    def triangulo(self):
        xf,yf = self.fijo
        sx,sy = self.escalamiento
        glScalef(sx,sy,1)
        glBegin(GL_POLYGON)
        for x,y in self.coords:
            glVertex2f( x,y )
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
        self.ui.agrandar.clicked.connect(self.agrandar)
        self.ui.achicar.clicked.connect(self.achicar)
        self.ui.original.clicked.connect(self.original)
    #slots
    @pyqtSlot()
    def agrandar(self):
        self.viewer3D.escalamiento = (2.0, 2.0)
        self.viewer3D.updateGL() 
    @pyqtSlot()
    def achicar(self):
        self.viewer3D.escalamiento = (0.5, 0.5)
        self.viewer3D.updateGL() 
    @pyqtSlot()
    def original(self):
        self.viewer3D.escalamiento = (1.0, 1.0)
        geometry = self.ui.OpenGLLayout.geometry()
        width = geometry.width()
        height = geometry.height()
        print('Desde clase Ventana:', width, height)
        self.viewer3D.updateGL() 
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana = Ventana()
    sys.exit(app.exec_())
