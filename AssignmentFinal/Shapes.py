#Imports
import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from math import *
import random

class Cube:
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

		self.vertices = (
			(self.x + 1, self.y - 1, self.z - 1),
			(self.x + 1, self.y + 1, self.z - 1),
			(self.x - 1, self.y + 1, self.z - 1),
			(self.x - 1, self.y - 1, self.z - 1),
			(self.x + 1, self.y - 1, self.z + 1),
			(self.x + 1, self.y + 1, self.z + 1),
			(self.x - 1, self.y - 1, self.z + 1),
			(self.x - 1, self.y + 1, self.z + 1)
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
		glColor3fv((0, 1, 1))
		for face in self.faces:
			for vertex in face:
				glVertex3fv(self.vertices[vertex])
		glEnd()

		glBegin(GL_LINES)
		glColor3fv((0, 0, 1))
		for edge in self.edges:
			for vertex in edge:
				glVertex3fv(self.vertices[vertex])
		glEnd()

class Pyramid:
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

		self.vertices = (
			(self.x - 1, self.y - 1, self.z - 1),
			(self.x - 1, self.y + 1, self.z - 1),
			(self.x + 1, self.y + 1, self.z - 1),
			(self.x + 1, self.y - 1, self.z - 1),
			(self.x, self.y, self.z + 2.0/3.0)
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
			(0, 3, 4),
			(2, 3, 4),
			(2, 1, 4)
		)

		glBegin(GL_QUADS)
		glColor3fv((0, 1, 1))
		for face in self.faces:
			for vertex in face:
				glVertex3fv(self.vertices[vertex])
		glEnd()

		glBegin(GL_LINES)
		glColor3fv((0, 0, 1))
		for edge in self.edges:
			for vertex in edge:
				glVertex3fv(self.vertices[vertex])
		glEnd()

class Walls:
	def __init__(self):
		self.x = 0
		self.y = 0
		self.z = 0

		self.vertices = (
			(self.x - 25, self.y - 25, self.z - 500),
			(self.x - 25, self.y + 25, self.z - 500),
			(self.x + 25, self.y + 25, self.z - 500),
			(self.x + 25, self.y - 25, self.z - 500),
			(self.x - 25, self.y - 25, self.z + 5),
			(self.x - 25, self.y + 25, self.z + 5),
			(self.x + 25, self.y + 25, self.z + 5),
			(self.x + 25, self.y - 25, self.z + 5)
		)

		self.edges = (
			(0, 1),
			(0, 3),
			(0, 4),
			(2, 1),
			(2, 3),
			(2, 6),
			(5, 4),
			(5, 1),
			(5, 6),
			(7, 4),
			(7, 6),
			(7, 3)
		)

		self.faces = (
			(1, 2, 6, 5),
			(0, 1, 5, 4),
			(0, 3, 7, 4),
			(3, 2, 6, 7)
		)

		glBegin(GL_QUADS)
		for face in self.faces:
			for vertex in face:
				glColor3fv((0.5, 0.5, 0.5))
				glVertex3fv(self.vertices[vertex])
		glEnd()

		glBegin(GL_LINES)
		glColor3fv((0, 0, 1))
		for edge in self.edges:
			for vertex in edge:
				glVertex3fv(self.vertices[vertex])
		glEnd()

class Crystal:
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

		self.vertices = (
			(self.x, self.y + 5.0/3.0, self.z),
			(self.x - 1, self.y + 1, self.z - 1),
			(self.x + 1, self.y + 1, self.z - 1),
			(self.x + 1, self.y - 1, self.z - 1),
			(self.x - 1, self.y - 1, self.z - 1),
			(self.x - 1, self.y + 1, self.z + 1),
			(self.x + 1, self.y + 1, self.z + 1),
			(self.x + 1, self.y - 1, self.z + 1),
			(self.x - 1, self.y - 1, self.z + 1),
			(self.x, self.y - 5.0/3.0, self.z)
		)

		self.edges = (
			(0, 1),
			(0, 2),
			(0, 5),
			(0, 6),
			(1, 4),
			(2, 3),
			(5, 8),
			(6, 7),
			(3, 9),
			(4, 9),
			(7, 9),
			(8, 9)
		)

		self.faces = (
			(0, 1, 2),
			(0, 2, 6),
			(0, 5, 6),
			(0, 5, 1),
			(1, 2, 3, 4),
			(2, 3, 6, 7),
			(5, 6, 7, 8),
			(1, 4, 8, 5),
			(4, 3, 9),
			(7, 3, 9),
			(7, 8, 9),
			(8, 4, 9)
		)

		glBegin(GL_QUADS)
		glColor3fv((0, 1, 1))
		for face in self.faces:
			for vertex in face:
				glVertex3fv(self.vertices[vertex])
		glEnd()

		glBegin(GL_LINES)
		glColor3fv((0, 0, 1))
		for edge in self.edges:
			for vertex in edge:
				glVertex3fv(self.vertices[vertex])
		glEnd()