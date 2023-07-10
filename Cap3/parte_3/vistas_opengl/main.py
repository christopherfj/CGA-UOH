import sys
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5 import QtOpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from figuras import *

#Ventana clase OpenGL
class Viewer3DWidget(QtOpenGL.QGLWidget):
    def __init__(self, parent=None):
        QtOpenGL.QGLWidget.__init__(self, parent)
        self.angx = 0
        self.angy = 0
        self.angz = 0
        self.anguloz = 45
        self.eyez = 10
    #Funciones protegidas OpenGL
    def paintGL(self):
        glMatrixMode( GL_MODELVIEW )
        glLoadIdentity()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glEnable(GL_DEPTH_TEST)
        self.dibujar()
        glFlush()
    def resizeGL(self, widthInPixels, heightInPixels):
        self.setResize(widthInPixels, heightInPixels)
    def setResize(self, widthInPixels, heightInPixels):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        aspectRatio = float(widthInPixels)/heightInPixels
        gluPerspective(self.anguloz, aspectRatio, 0.1, 100.0)                    
        gluLookAt(0.0, 0.0, self.eyez, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
        glViewport(0, 0, widthInPixels, heightInPixels)
    def initializeGL(self):
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClearDepth(1.0)
    #Metodos-seleccion-figuras
    def dibujar(self):
        glRotatef(self.angx, 1.0, 0.0, 0.0)
        glRotatef(self.angy, 0.0, 1.0, 0.0)
        glRotatef(self.angz, 0.0, 0.0, 1.0)
        cubo()
          
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
        self.ui.rotarx.valueChanged.connect(self.rotarx)
        self.ui.rotary.valueChanged.connect(self.rotary)
        self.ui.rotarz.valueChanged.connect(self.rotarz)
        self.ui.ejez.valueChanged.connect(self.ejez)
        self.ui.angz.valueChanged.connect(self.angz)
    #slots
    @pyqtSlot()
    def rotarx(self):
        ang = int(self.ui.rotarx.value())
        self.viewer3D.angx = ang
        self.ui.labelx.setText(str(ang))
        self.viewer3D.updateGL() 
    @pyqtSlot()
    def rotary(self):
        ang = int(self.ui.rotary.value())
        self.viewer3D.angy = ang
        self.ui.labely.setText(str(ang))
        self.viewer3D.updateGL() 
    @pyqtSlot()
    def rotarz(self):
        ang = int(self.ui.rotarz.value())
        self.viewer3D.angz = ang
        self.ui.labelz.setText(str(ang))
        self.viewer3D.updateGL() 
    @pyqtSlot()
    def ejez(self):
        z = float(self.ui.ejez.value()/10)
        self.viewer3D.eyez = z
        self.ui.labelejez.setText(str(z))
        self.viewer3D.setResize(self.viewer3D.width(), self.viewer3D.height())
        self.viewer3D.updateGL() 
    @pyqtSlot()
    def angz(self):
        ang = int(self.ui.angz.value())
        self.viewer3D.anguloz = ang
        self.ui.labelangz.setText(str(ang))
        self.viewer3D.setResize(self.viewer3D.width(), self.viewer3D.height())
        self.viewer3D.updateGL() 
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana = Ventana()
    sys.exit(app.exec_())