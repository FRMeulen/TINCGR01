class Matrix:
	def __init__(self, height, width):
	#Creates matrix object with variable height and width	
		self.rows = height
		self.columns = width

		#Matrix is list of lists, filled with 0's by default
		self.positions = [[0 for x in range(self.columns)] for y in range(self.rows)]	
		
		#For every row
		for x in range(self.rows):	
			#And every column
			for y in range(self.columns):	
				#Ask input
				print("Number for ", x, ",", y)
				
				#Fill matrix	
				self.positions[x][y] = int(input())	

		#Print empty line to separate in console		
		print()	

	def print(self):
	#Prints out matrix on screen
		#For every row	
		for x in range(self.rows):	
			#And every column
			for y in range(self.columns):	
				#Print stored number and space
				print(self.positions[x][y], end=' ')

			#Next line after every row		
			print()	

	def multRowWithVector(self, row, vector):
	#Multiply one row with a vector 
	#DO NOT CALL ON ITS OWN, COMPATIBILITY CHECK IS IN multWithVector METHOD	

		#Stores result, 0 is default	
		result = 0	

		#For every item in the row
		for x in range(len(row)):	
			#Result increases by row[x] times vector[x]
			result += row[x] * vector[x]	

		return result

	def multWithVector(self, vector):
	#Multiplies a matrix with a vector
		
		#If vector length == amount of matrix rows	
		if(len(vector) == self.rows):	
			#Stores new values
			newValues = []	

			#For every row
			for x in range(self.rows):
				#New value is current row times vector	
				temp = self.multRowWithVector(self.positions[x], vector)	
				#Store new value in list
				newValues.append(temp)

			#After multiplication matrix only has one column	
			self.columns = 1	
			#Re-enter matrix data
			self.positions = [[newValues[y] for x in range(self.columns)] for y in range(self.rows)]

		#If vector length and matrix rows do not match		
		else:	
			#Multiplication impossible
			print("Vector incompatible with matrix")	