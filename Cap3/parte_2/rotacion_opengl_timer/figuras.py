from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def cubo():        
    # Cuadrado 1
    glBegin(GL_QUADS)      
    glColor3f(1,0,0)
    glVertex3f(-1,-1, 1)
    glVertex3f( 1,-1, 1)
    glVertex3f( 1, 1, 1)
    glVertex3f(-1, 1, 1)
    glEnd()

    # Cuadrado 2
    glBegin(GL_QUADS) 
    glColor3f(0,1,0)
    glVertex3f(-1,-1,-1)
    glVertex3f( 1,-1,-1)
    glVertex3f( 1, 1,-1)
    glVertex3f(-1, 1,-1)
    glEnd()

    # Cuadrado 3
    glBegin(GL_QUADS)     
    glColor3f(0,0,1)    
    glVertex3f( 1, 1, 1)
    glVertex3f( 1,-1, 1)
    glVertex3f( 1,-1,-1)
    glVertex3f( 1, 1,-1)
    glEnd()

    # Cuadrado 4
    glBegin(GL_QUADS) 
    glColor3f(1,1,0)
    glVertex3f(-1, 1, 1)
    glVertex3f( 1, 1, 1)
    glVertex3f( 1, 1,-1)
    glVertex3f(-1, 1,-1)
    glEnd()

    # Cuadrado 5  
    glBegin(GL_QUADS) 
    glColor3f(0,1,1)
    glVertex3f(-1, 1, 1)
    glVertex3f(-1,-1, 1)
    glVertex3f(-1,-1,-1)
    glVertex3f(-1, 1,-1)
    glEnd()

    # Cuadrado 6
    glBegin(GL_QUADS) 
    glColor3f(1,0,1)
    glVertex3f(-1,-1, 1)
    glVertex3f( 1,-1, 1)
    glVertex3f( 1,-1,-1)
    glVertex3f(-1,-1,-1)
    glEnd()