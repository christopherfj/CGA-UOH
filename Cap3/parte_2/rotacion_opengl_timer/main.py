import sys
from PyQt5 import QtGui, QtWidgets, uic, QtCore
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
        self.angx = 0
        self.angy = 0
        self.angz = 0
    #Funciones protegidas OpenGL
    def paintGL(self):
        glMatrixMode( GL_MODELVIEW )
        glLoadIdentity()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glEnable(GL_DEPTH_TEST)
        self.dibujar()
        glFlush()
    def resizeGL(self, widthInPixels, heightInPixels):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-self.max_xyz, self.max_xyz, \
                -self.max_xyz, self.max_xyz, \
                -self.max_xyz, self.max_xyz)
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
        self.angx = 0
        self.angy = 0
        self.angz = 0
        self.timerx = QtCore.QTimer()
        self.timery = QtCore.QTimer()
        self.timerz = QtCore.QTimer()
        #signals
        self.ui.rotarx.valueChanged.connect(self.rotarx)
        self.ui.rotary.valueChanged.connect(self.rotary)
        self.ui.rotarz.valueChanged.connect(self.rotarz)
        
        self.ui.reiniciar.clicked.connect(self.reiniciar)

        self.ui.rotarx_t.clicked.connect(self.rotarx_t) #inicio timer x
        self.ui.rotary_t.clicked.connect(self.rotary_t) #inicio timer y
        self.ui.rotarz_t.clicked.connect(self.rotarz_t) #inicio timer z
        
        self.timerx.timeout.connect(self.timer_x)
        self.timery.timeout.connect(self.timer_y)
        self.timerz.timeout.connect(self.timer_z)
        
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
    def rotarx_t(self):
        self.timerx.start(50) #cada 50ms
    @pyqtSlot()       
    def rotary_t(self):
        self.timery.start(50) #cada 50ms
    @pyqtSlot()       
    def rotarz_t(self):
        self.timerz.start(50) #cada 50ms
        
    @pyqtSlot()
    def reiniciar(self):
        self.timerx.stop()
        self.timery.stop()
        self.timerz.stop()
        self.viewer3D.angx = 0
        self.viewer3D.angy = 0
        self.viewer3D.angz = 0
        self.viewer3D.updateGL() 
        
    @pyqtSlot()
    def timer_x(self):
        self.angx+=10
        if self.angx>360:
            self.angx = 0
        self.viewer3D.angx = self.angx
        self.viewer3D.updateGL() 
    @pyqtSlot()
    def timer_y(self):
        self.angy+=10
        if self.angy>360:
            self.angy = 0
        self.viewer3D.angy = self.angy
        self.viewer3D.updateGL() 
    @pyqtSlot()
    def timer_z(self):
        self.angz+=10
        if self.angz>360:
            self.angz = 0
        self.viewer3D.angz = self.angz
        self.viewer3D.updateGL() 
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana = Ventana()
    sys.exit(app.exec_())

