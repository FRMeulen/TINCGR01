#Imports
from grid import *
from random import randint

debug = True	#Boolean for debug mode

g = Grid(50, 50)	#Grid with tiles

#Coordinates of two points
x1 = randint(0, 49)
y1 = randint(0, 49)
x2 = randint(0, 49)
y2 = randint(0, 49)

if debug:
	#Print x's and y's of points
	print("Point 1: X:", x1, "Y:", y1)
	print("Point 2: X:", x2, "Y:", y2)

#Methods
def derivativeY(hor1, ver1, hor2, ver2):
	deltaX = hor2 - hor1	#x2 - x1
	deltaY = ver2 - ver1	#y2 - y1
	
	coefficientY = 0	#Default value

	#If not a straight horizontal line
	if deltaY != 0:
		coefficientY = deltaX / deltaY
	
	return coefficientY

def derivativeX(hor1, ver1, hor2, ver2):
	deltaX = hor2 - hor1	#x2 - x1
	deltaY = ver2 - ver1	#y2 - y1

	coefficientX = 0	#Default value

	#If not a straight vertical line
	if deltaX != 0:
		coefficientX = deltaY / deltaX

	return coefficientX

def verticalLine(x, bottomY, topY):
	for y in range(bottomY, topY):
		g.addPoint(x, y)

def horizontalLine(leftX, rightX, y):
	for x in range(leftX, rightX):
		g.addPoint(x, y)

#Logic
c1 = derivativeY(x1, y1, x2, y2)	#Coefficient around y of line between points
c2 = derivativeX(x1, y1, x2, y2)	#Coefficient around x of line between points

#Determine direction of line
if x1 > x2:
	if y1 > y2:
		#Point 1 is below and to the right of point 2
		#Coefficient is negative, line goes from 2 to 1
		tempX = x2
		tempY = y2

		#Draw line calculated around deltaY
		while tempY < y1:
			tempX += c1
			tempY += 1
			g.addPoint(tempX, tempY)

		#Reset temp values		
		tempX = x2
		tempY = y2

		#Draw line calculated around deltaX
		while tempX < x1:
			tempX += 1
			tempY += c2
			g.addPoint(tempX, tempY)

		if debug:
			print("Point 1 is below and to the right of point 2")
			print("Y coefficient:", c1)
			print("X coefficient:", c2)

	elif y2 > y1:
		#Point 1 is above and to the right of point 2
		#Coefficient is negative, line goes from 2 to 1
		tempX = x1
		tempY = y1

		#Draw line calculated around deltaY
		while tempY < y2:
			tempX += c1
			tempY += 1
			g.addPoint(tempX, tempY)

		#Reset temp values
		tempX = x2
		tempY = y2

		#Draw line calculated around deltaX
		while tempX < x1:
			tempX += 1
			tempY += c2
			g.addPoint(tempX, tempY)

		if debug:
			print("Point 1 is above and to the right of point 2")
			print("Y coefficient:", c1)
			print("X coefficient:", c2)

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

		#Draw line calculated around deltaY
		while tempY < y1:
			tempX += c1
			tempY += 1
			g.addPoint(tempX, tempY)

		#Reset temp values
		tempX = x1
		tempY = y1

		#Draw line calculated around deltaX
		while tempX < x2:
			tempX += 1
			tempY += c2
			g.addPoint(tempX, tempY)

		if debug:
			print("Point 1 is below and to the left of point 2")
			print("Y coefficient:", c1)
			print("X coefficient:", c2)

	elif y2 > y1:
		#Point 1 is above and to the left of point 2
		#Coefficient is positive, line goes from 1 to 2
		tempX = x1
		tempY = y1

		#Draw line calculated around deltaY
		while tempY < y2:
			tempX += c1
			tempY += 1
			g.addPoint(tempX, tempY)

		#Reset temp values
		tempX = x1
		tempY = y1

		#Draw line calculated around deltaX
		while tempX < x2:
			tempX += 1
			tempY += c2
			g.addPoint(tempX, tempY)

		if debug:
			print("Point 1 is above and to the left of point 2")
			print("Y coefficient:", c1)
			print("X coefficient:", c2)

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