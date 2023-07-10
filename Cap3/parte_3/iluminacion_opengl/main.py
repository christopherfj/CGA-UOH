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
    max_xyz = 2.0
    def __init__(self, parent=None):
        QtOpenGL.QGLWidget.__init__(self, parent)
        self.angx, self.angy, self.angz = 0,0,0
    #Funciones protegidas OpenGL
    def paintGL(self):        
        glMatrixMode( GL_MODELVIEW )
        glLoadIdentity()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        glShadeModel(GL_SMOOTH)
        self.dibujar()
        glFlush()
    def resizeGL(self, widthInPixels, heightInPixels):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        aspectRatio = float(widthInPixels)/heightInPixels
        if aspectRatio > 1.:
            glOrtho(-self.max_xyz*aspectRatio, self.max_xyz*aspectRatio, \
                    -self.max_xyz, self.max_xyz, \
                    -self.max_xyz, self.max_xyz)
        else:
            glOrtho(-self.max_xyz, self.max_xyz, \
                    -self.max_xyz/aspectRatio, self.max_xyz/aspectRatio, \
                    -self.max_xyz, self.max_xyz)
        glViewport(0, 0, widthInPixels, heightInPixels)
    def initializeGL(self):
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClearDepth(1.0)
        ambientLight  = [ 0.3, 0.3, 0.3, 0.5 ]
        diffuseLight  = [ 0.7, 0.7, 0.7, 0.6 ]
        specularLight = [ 1.0, 1.0, 1.0, 1.0 ]
        glLightfv(GL_LIGHT0, GL_AMBIENT,  ambientLight)
        glLightfv(GL_LIGHT0, GL_DIFFUSE,  diffuseLight)
        glLightfv(GL_LIGHT0, GL_SPECULAR, specularLight)
        lightPos = [ 0.0, 0.0, -100.0, 0.0 ]
        glLightfv(GL_LIGHT0, GL_POSITION, lightPos)
    #Metodos-seleccion-figuras
    def dibujar(self):
        glEnable(GL_LIGHT0)
        glEnable(GL_COLOR_MATERIAL)
        glRotatef(self.angx, 1.0, 0.0, 0.0)
        glRotatef(self.angy, 0.0, 1.0, 0.0)
        glRotatef(self.angz, 0.0, 0.0, 1.0)
        cubo()
        glDisable(GL_COLOR_MATERIAL)
        glDisable(GL_LIGHT0)
          
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
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana = Ventana()
    sys.exit(app.exec_())