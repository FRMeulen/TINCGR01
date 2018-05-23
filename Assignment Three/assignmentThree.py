from grid import *
from random import randint

debug = True

g = Grid(50, 50)	#Grid with tiles

#Booleans for special occasions
straightVertical = False
straightHorizontal = False

#Coordinates of two points
x1 = randint(0, 49)
y1 = randint(0, 49)
x2 = randint(0, 49)
y2 = randint(0, 49)

#Set starting points in red
print("Point 1: X:", x1, "Y:", y1)
print("Point 2: X:", x2, "Y:", y2)

#Methods
def derivative(hor1, ver1, hor2, ver2):
	deltaX = hor2 - hor1	#x2 - x1
	deltaY = ver2 - ver1	#y2 - y1
	
	#If straight vertical line
	if deltaX == 0:
		straightVertical = True
	
	#If not a straight horizontal line
	if deltaY != 0:
		coefficient = deltaX / deltaY
	
	#If straight horizontal line
	else:
		straightHorizontal = True
		coefficient = 0
	
	return coefficient

def addNextPoint(lastX, lastY, coeff):
	g.addPoint(lastX + coeff, lastY + 1)

def verticalLine(x, bottomY, topY):
	for y in range(bottomY, topY):
		g.addPoint(x, y)

def horizontalLine(leftX, rightX, y):
	for x in range(leftX, rightX):
		g.addPoint(x, y)

def diagonalLine(leftX, rightX, topY, bottomY):
	return 0

#Logic
c = derivative(x1, y1, x2, y2)	#Coefficient of line between points

#Determine direction of line
if x1 > x2:
	if y1 > y2:
		#Point 1 is below and to the right of point 2
		#Coefficient is negative, line goes from 2 to 1
		tempX = x2
		tempY = y2

		while tempY < y1:
			addNextPoint(tempX, tempY, c)
			tempX += c
			tempY += 1

		if debug:
			print("Point 1 is below and to the right of point 2")
			print("Coefficient is positive, line goes from 2 to 1")
			print(c)

	elif y2 > y1:
		#Point 1 is above and to the right of point 2
		#Coefficient is negative, line goes from 2 to 1
		tempX = x1
		tempY = y1

		while tempY < y2:
			print("Temp X:", tempX)
			addNextPoint(tempX, tempY, c)
			tempX += c
			tempY += 1

		if debug:
			print("Point 1 is above and to the right of point 2")
			print("Coefficient is negative, line goes from 1 to 2")
			print(c)

	elif y1 == y2:
		#Point 1 is to the right of point 2
		horizontalLine(x2, x1, y1)

		if debug:
			print("Point 1 is to the right of point 2")
			print("Line is straight horizontal")

elif x2 > x1:
	if y1 > y2:
		#Point 1 is below and to the left of point 2
		#Coefficient is negative, line goes from 1 to 2
		tempX = x2
		tempY = y2

		while tempY < y1:
			print("Temp X:", tempX)
			addNextPoint(tempX, tempY, c)
			tempX += c
			tempY += 1

		if debug:
			print("Point 1 is below and to the left of point 2")
			print("Coefficient is negative, line goes from 2 to 1")
			print(c)

	elif y2 > y1:
		#Point 1 is above and to the left of point 2
		#Coefficient is positive, line goes from 1 to 2
		tempX = x1
		tempY = y1

		while tempY < y2:
			print("Temp X:", tempX)
			addNextPoint(tempX, tempY, c)
			tempX += c
			tempY += 1

		if debug:
			print("Point 1 is above and to the left of point 2")
			print("Coefficient is positive, line goes from 1 to 2")
			print(c)

	elif y1 == y2:
		#Point 1 is to the left of point 2
		horizontalLine(x1, x2, y1)

		if debug:
			print("Point 1 is to the left of point 2")
			print("Line is straight horizontal")

elif x1 == x2:
	if y1 > y2:
		#Point 1 is below point 2
		verticalLine(x1, y2, y1)

		if debug:
			print("Point 1 is below point 2")
			print("Line is straight vertical")

	elif y2 > y1:
		#Point 1 is above point 2
		verticalLine(x1, y1, y2)

		if debug:
			print("Point 1 is above point 2")
			print("Line is straight vertical")

	elif y1 == y2:
		#Point 1 is point 2
		g.addPoint(x1, y1, (1, 0, 0))


#Color beginning and end red
g.addPoint(x1, y1, (0, 1, 0))
g.addPoint(x2, y2, (1, 0, 0))

#Draw grid with points
g.draw()