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
        self.figura = 'triangulo'
        self.colores = {'r':[255,0,0], 'g':[0,255,0], 'b':[0,0,255]}
        self.color = 'r' 
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
        glColor3fv(self.colores[self.color])
        if self.figura == 'cuadrado':
            self.cuadrado()
        else:
            self.triangulo()
    #Metodos-figuras
    def triangulo(self):
        glBegin(GL_POLYGON)        
        glVertex2f(0.0, 0.5)
        glVertex2f(0.5, -0.5)
        glVertex2f(-0.5, -0.5)
        glEnd()
    def cuadrado(self):
        glBegin(GL_POLYGON)        
        glVertex2f(-0.5, 0.5)
        glVertex2f(0.5, 0.5)
        glVertex2f(0.5, -0.5)
        glVertex2f(-0.5, -0.5)
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
      self.colores = ['r', 'g', 'b']
      self.figuras = ['triangulo', 'cuadrado']
      #signals
      self.ui.figura.currentIndexChanged.connect(self.cambioFigura)
      self.ui.color.currentIndexChanged.connect(self.cambioColor)      
   #slots
   @pyqtSlot()
   def cambioFigura (self):
       index_figura = self.ui.figura.currentIndex()
       self.viewer3D.figura = self.figuras[index_figura]
       self.viewer3D.updateGL() 
   @pyqtSlot()
   def cambioColor (self):
       index_color = self.ui.color.currentIndex()
       self.viewer3D.color = self.colores[index_color]
       self.viewer3D.updateGL()  
    
if __name__ == "__main__":
   app = QtWidgets.QApplication(sys.argv)
   ventana = Ventana()
   sys.exit(app.exec_())
