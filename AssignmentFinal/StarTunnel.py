#Imports
import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from math import *
from Shapes import *
import random

def main():
	pygame.init()	#Initialize pygame
	display = (1024,720)	#Screen size
	pygame.display.set_mode(display, DOUBLEBUF|OPENGL)	#Tell pygame we're using OpenGL

	#Initial OpenGL functions to call once
	gluPerspective(45, (display[0]/display[1]), 0.1, 500.0)	#Point of perspective
	glTranslatef(0, 0, -10)	#Translate cube before drawing
	glRotatef(0, 1, 0, 0)

	object_passed = False
	x_speed = 0
	y_speed = 0
	z_speed = 0

	walls = Walls()

	#Running loop
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:	#If quitting
				pygame.quit()
				quit()
	
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_speed = 0.3
				if event.key == pygame.K_RIGHT:
					x_speed = -0.3
				if event.key == pygame.K_UP:
					y_speed = -0.3
				if event.key == pygame.K_DOWN:
					y_speed = 0.3

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_speed = 0
				if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					y_speed = 0

		#Code here will continuously run until program is quit
	
		#Get 'camera' position
		matrix = glGetDoublev(GL_MODELVIEW_MATRIX)
		camera_x = matrix[3][0]
		camera_y = matrix[3][1]
		camera_z = matrix[3][2]

		#Block movement past x walls
		if camera_x >= 25:
			if x_speed > 0:
				x_speed = 0
		if camera_x <= -25:
			if x_speed < 0:
				x_speed = 0

		#Block movement past y walls
		if camera_y >= 25:
			if y_speed > 0:
				y_speed = 0
		if camera_y <= -25:
			if y_speed < 0:
				y_speed = 0

		#If block passed 'camera' trigger flag
		if camera_z < -1:
			object_passed = True

		print("Camera location X:%s Y:%s Z:%s" % (camera_x, camera_y, camera_z))
		glTranslatef(x_speed, y_speed, z_speed)
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)	#Clear buffer bits
		#walls = Walls()
		Crystal(0, 0, 0)
		pygame.display.flip()	#Draw
		pygame.time.wait(10)	#Wait 10 milliseconds before drawing again

main()

pygame.quit()	#Quit pygame
quit()	#Quit window