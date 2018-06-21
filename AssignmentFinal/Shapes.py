#Imports
import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from math import *

colors = (
	(0, 0, 0),
	(0, 0, 1),
	(0, 1, 0),
	(0, 1, 1),
	(1, 0, 0),
	(1, 0, 1),
	(1, 1, 0),
	(1, 1, 1),
	(0.5, 1, 0.5),
	(0.5, 0.5, 1),
	(1, 0.5, 0.5),
	(0.5, 0.4, 0.3)
)

class Cube:
	def __init__(self):

		self.vertices = (
			(1, -1, -1),
			(1, 1, -1),
			(-1, 1, -1),
			(-1, -1, -1),
			(1, -1, 1),
			(1, 1, 1),
			(-1, -1, 1),
			(-1, 1, 1)
		)

		self.edges = (
			(0, 1),
			(0, 3),
			(0, 4),
			(2, 1),
			(2, 3),
			(2, 7),
			(6, 3),
			(6, 4),
			(6, 7),
			(5, 1),
			(5, 4),
			(5, 7)
		)

		self.faces = (
			(0, 1, 2, 3),
			(3, 2, 7, 6),
			(6, 7, 5, 4),
			(4, 5, 1, 0),
			(1, 5, 7, 2),
			(4, 0, 3, 6)
		)

		glBegin(GL_QUADS)
		for face in self.faces:
			x = 0
			for vertex in face:
				x += 2
				glColor3fv(colors[x])
				glVertex3fv(self.vertices[vertex])
		glEnd()

		glBegin(GL_LINES)
		glColor3fv((0, 0, 1))
		for edge in self.edges:
			for vertex in edge:
				glVertex3fv(self.vertices[vertex])
		glEnd()

class Tetrahedron:
	def __init__(self):

		self.vertices = (
			(sqrt(8.0/9.0), 0, -1.0/3.0),
			(-sqrt(2.0/9.0), sqrt(2.0/3.0), -1.0/3.0),
			(-sqrt(2.0/9.0), -sqrt(2.0/3.0), -1.0/3.0),
			(0, 0, 1)
		)

		self.edges = (
			(0, 1),
			(0, 2),
			(0, 3),
			(1, 2),
			(1, 3),
			(2, 3)
		)

		self.faces = (
			(0, 1, 2),
			(0, 1, 3),
			(0, 2, 3),
			(1, 2, 3)
		)

		glBegin(GL_QUADS)
		for face in self.faces:
			x = 0
			for vertex in face:
				x += 2
				glColor3fv(colors[x])
				glVertex3fv(self.vertices[vertex])
		glEnd()

		glBegin(GL_LINES)
		glColor3fv((0, 0, 1))
		for edge in self.edges:
			for vertex in edge:
				glVertex3fv(self.vertices[vertex])
		glEnd()

class Pyramid:
	def __init__(self):

		self.vertices = (
			(-1, -1, -1),
			(-1, 1, -1),
			(1, 1, -1),
			(1, -1, -1),
			(0, 0, 2.0/3.0)
		)

		self.edges = (
			(0, 1),
			(0, 3),
			(0, 4),
			(1, 2),
			(1, 4),
			(2, 3),
			(2, 4),
			(3, 4)
		)

		self.faces = (
			(0, 1, 2, 3),
			(0, 1, 4),
			(0, 2, 4),
			(2, 3, 4),
			(2, 1, 4)
		)

		glBegin(GL_QUADS)
		for face in self.faces:
			x = 0
			for vertex in face:
				x += 2
				glColor3fv(colors[x])
				glVertex3fv(self.vertices[vertex])
		glEnd()

		glBegin(GL_LINES)
		glColor3fv((0, 0, 1))
		for edge in self.edges:
			for vertex in edge:
				glVertex3fv(self.vertices[vertex])
		glEnd()