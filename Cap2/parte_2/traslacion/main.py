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
        self.t = (0,0)
        self.coords = [(0.0, 0.5), (0.5,-0.5), (-0.5,-0.5)]
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
        self.triangulo()
    #Metodos-figuras
    def triangulo(self):
        glBegin(GL_POLYGON)
        for x,y in self.coords:
            glVertex2f( x+self.t[0],y+self.t[1] )
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
      self.ui.arriba.clicked.connect(self.arriba)
      self.ui.abajo.clicked.connect(self.abajo)
      self.ui.izquierda.clicked.connect(self.izquierda)
      self.ui.derecha.clicked.connect(self.derecha)
      self.ui.centro.clicked.connect(self.centro)
   #slots
   @pyqtSlot()
   def arriba(self):
       self.viewer3D.t = (0,0.5)
       self.viewer3D.updateGL() 
   @pyqtSlot()
   def abajo(self):
       self.viewer3D.t = (0,-0.5)
       self.viewer3D.updateGL() 
   @pyqtSlot()
   def izquierda(self):
       self.viewer3D.t = (-0.5,0)
       self.viewer3D.updateGL() 
   @pyqtSlot()
   def derecha(self):
       self.viewer3D.t = (0.5,0)
       self.viewer3D.updateGL() 
   @pyqtSlot()
   def centro(self):
       self.viewer3D.t = (0,0)
       self.viewer3D.updateGL() 
        
if __name__ == "__main__":
   app = QtWidgets.QApplication(sys.argv)
   ventana = Ventana()
   sys.exit(app.exec_())
