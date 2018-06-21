#Imports
import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from math import *
from Shapes import *

def main():
	pygame.init()	#Initialize pygame
	display = (800,600)	#Screen size
	pygame.display.set_mode(display, DOUBLEBUF|OPENGL)	#Tell pygame we're using OpenGL

	gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)	#Point of perspective
	glTranslatef(0, 0, -5)	#Translate cube before drawing
	glRotatef(1, 0, 0, 0)	#Rotate cube before drawing

	running = True	#Game running boolean

	#Running loop
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:	#If quitting
				running = False	#Flip boolean
				pygame.quit()	#Quit pygame
				quit()	#Quit window

		#Code here will continuously run until program is quit
		glRotatef(1, 1, 1, 1)	#Rotate cube 1 degree per loop over XYZ-axes
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)	#Clear buffer bits
		cube = Cube()	#Make cube
		tetrahedron = Tetrahedron()	#Make tetrahedron
		pyramid = Pyramid()	#Make pyramid
		pygame.display.flip()	#Draw
		pygame.time.wait(10)	#Wait 10 milliseconds before drawing again


main()

print("Successful so far!")