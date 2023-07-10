from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def cubo(texture):  
    
    glEnable(GL_TEXTURE_2D) 
    glBindTexture(GL_TEXTURE_2D, texture[0])
    
    # Cuadrado 1
    glBegin(GL_QUADS)      
    glColor3f(1,0,0)
    glTexCoord2f(0.0,1.0)
    glVertex3f(-1,-1, 1)
    glTexCoord2f(1.0,1.0)
    glVertex3f( 1,-1, 1)
    glTexCoord2f(1.0,0.0)
    glVertex3f( 1, 1, 1)
    glTexCoord2f(0.0,0.0)
    glVertex3f(-1, 1, 1)
    glEnd()

    # Cuadrado 2
    glBegin(GL_QUADS) 
    glColor3f(0,1,0)
    glTexCoord2f(0.0,1.0)
    glVertex3f(-1,-1,-1)
    glTexCoord2f(1.0,1.0)
    glVertex3f( 1,-1,-1)
    glTexCoord2f(1.0,0.0)
    glVertex3f( 1, 1,-1)
    glTexCoord2f(0.0,0.0)
    glVertex3f(-1, 1,-1)
    glEnd()

    # Cuadrado 3
    glBegin(GL_QUADS)     
    glColor3f(0,0,1)    
    glTexCoord2f(0.0,1.0)
    glVertex3f( 1, 1, 1)
    glTexCoord2f(1.0,1.0)
    glVertex3f( 1,-1, 1)
    glTexCoord2f(1.0,0.0)
    glVertex3f( 1,-1,-1)
    glTexCoord2f(0.0,0.0)
    glVertex3f( 1, 1,-1)
    glEnd()

    # Cuadrado 4
    glBegin(GL_QUADS) 
    glColor3f(1,1,0)
    glTexCoord2f(0.0,1.0)
    glVertex3f(-1, 1, 1)
    glTexCoord2f(1.0,1.0)
    glVertex3f( 1, 1, 1)
    glTexCoord2f(1.0,0.0)
    glVertex3f( 1, 1,-1)
    glTexCoord2f(0.0,0.0)
    glVertex3f(-1, 1,-1)
    glEnd()

    # Cuadrado 5  
    glBegin(GL_QUADS) 
    glColor3f(0,1,1)
    glTexCoord2f(0.0,1.0)
    glVertex3f(-1, 1, 1)
    glTexCoord2f(1.0,1.0)
    glVertex3f(-1,-1, 1)
    glTexCoord2f(1.0,0.0)
    glVertex3f(-1,-1,-1)
    glTexCoord2f(0.0,0.0)
    glVertex3f(-1, 1,-1)
    glEnd()

    # Cuadrado 6
    glBegin(GL_QUADS) 
    glColor3f(1,0,1)
    glTexCoord2f(0.0,1.0)
    glVertex3f(-1,-1, 1)
    glTexCoord2f(1.0,1.0)
    glVertex3f( 1,-1, 1)
    glTexCoord2f(1.0,0.0)
    glVertex3f( 1,-1,-1)
    glTexCoord2f(0.0,0.0)
    glVertex3f(-1,-1,-1)
    glEnd()