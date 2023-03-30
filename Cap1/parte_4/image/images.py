import cv2
from matplotlib import pylab
import numpy as np

pylab.rcParams.update({'font.size': 25})

img = cv2.imread('uoh.jpg')
rgb =  cv2.cvtColor( img, cv2.COLOR_BGR2RGB ) 
x,y,z = rgb.shape
r = np.zeros((x,y,z), dtype=np.uint8)
r[:,:,0] = rgb[:,:,0]
g = np.zeros((x,y,z), dtype=np.uint8)
g[:,:,1] = rgb[:,:,1]
b = np.zeros((x,y,z), dtype=np.uint8)
b[:,:,2] = rgb[:,:,2]
gray = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
th = 100
ret, bw = cv2.threshold(gray, th, 255, cv2.THRESH_BINARY)

fig = pylab.figure(1)
pylab.subplot(3,1,1)
pylab.imshow(r)
pylab.axis(False)
pylab.subplot(3,1,2)
pylab.imshow(g)
pylab.axis(False)
pylab.subplot(3,1,3)
pylab.imshow(b)
pylab.axis(False)
pylab.show()

fig = pylab.figure(2)
pylab.imshow(rgb)
pylab.axis(False)
pylab.show()

fig = pylab.figure(3)
pylab.subplot(1,2,1)
pylab.imshow(gray, cmap='gray')
pylab.axis(False)
pylab.subplot(1,2,2)
pylab.hist(gray.ravel(), bins=256 )
pylab.xlabel('Intensidad')
pylab.ylabel('Frecuencia')
pylab.show()

fig = pylab.figure(4)
pylab.subplot(1,2,1)
pylab.imshow(bw, cmap='gray')
pylab.axis(False)
pylab.subplot(1,2,2)
pylab.hist(bw.ravel(), bins=256 )
pylab.xlabel('Intensidad')
pylab.ylabel('Frecuencia')
pylab.show()
