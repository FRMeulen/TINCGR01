import math
from lines import *

#Points are the corners of the cube
class Point:
	#Creates object of Point
	def __init__(self, x=0, y=0, z=0):
		#Set x, y and z coordinates as floats
		self.x, self.y, self.z = float(x), float(y), float(z)

	#Rotates point around the Y axis with a given angle in degrees
	def rotate(self, angle):
		radial = (angle * math.pi) / 180	#Convert degrees to radial
		cosine = math.cos(radial)	#Calculate cosine of radial
		sine = math.sin(radial)	#Calculate sine of radial
		z = self.z * cosine - self.x * sine	#Calculate new Z coordinate
		x = self.z * sine + self.x * cosine	#Calculate new X coordinate
		return Point(x, self.y, z)	#Return Point with new coordinates

	#Goes from 3D Points to 2D Points using perspective projection
	def to2D(self, windowWidth, windowHeight, fieldOfView, viewerDistance):
		factor = fieldOfView / (viewerDistance + self.z)	#Calculate scale factor
		x = self.x * factor + windowWidth / 2	#Calculate 2D X coordinate
		y = -self.y * factor + windowHeight / 2	#Calculate 2D Y coordinate
		return Point(x, y, 1)	#Return Point with new coordinates

#Window that will show the drawn cube
class CubeDrawer:
	#Creates object of CubeDrawer
	def __init__(self, windowWidth, windowHeight):
		#Set window size
		self.windowWidth = windowWidth
		self.windowHeight = windowHeight

		#Contains the corners of the cube
		self.cubePoints = [
			Point(-1, -1, -1),
            Point(1, -1, -1),
            Point(1, 1, -1),
            Point(-1, 1, -1),
            Point(-1, -1, 1),
            Point(1, -1, 1),
            Point(1, 1, 1),
            Point(-1, 1, 1)
		]

		#Contains points that make all 6 cube faces
		self.faces = [
			(0, 1, 2, 3),
			(1, 5, 6, 2),
			(5, 4, 7, 6),
			(4, 0, 3, 7),
			(0, 4, 5, 1),
			(3, 2, 6, 7)
		]

	def draw(self, rotation):
		#Create object of Lines
		l = Lines(self.windowWidth, self.windowHeight)

		#Holds transformed corners
		t = []

		#For every point...
		for x in self.cubePoints:
			#Rotate around Y axis
			rotated = x.rotate(rotation)

			#Transform from 3D to 2D
			projected = rotated.to2D(self.windowWidth, self.windowHeight, 512, 4)

			#Append to t
			t.append(projected)

		#For every face
		for y in self.faces:
			l.addLine((t[y[0]].x, t[y[0]].y, ), (t[y[1]].x, t[y[1]].y))
			l.addLine((t[y[1]].x, t[y[1]].y, ), (t[y[2]].x, t[y[2]].y))
			l.addLine((t[y[2]].x, t[y[2]].y, ), (t[y[3]].x, t[y[3]].y))
			l.addLine((t[y[3]].x, t[y[3]].y, ), (t[y[0]].x, t[y[0]].y))

		l.draw()

cube = CubeDrawer(640, 480)
cube.draw(30)