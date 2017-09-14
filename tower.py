def generateMoves(sys):
	moves = []
	for i in range(3):
		for j in range(3):
			if sys[i] != None:
				if len(sys[i]) > 0:
					if i != j:
						if sys[j] == []:
							moves.append((i, j))
						else:
							if sys[j] == None:
								moves.append((i, j))
							else:
								if sys[j][-1] > sys[i][-1]:
									moves.append((i, j))
	return moves

dict = {}
def move(sys, m, tar):
	# do the move
	print(sys, m)
	temp = sys[m[0]][-1]
	if sys[m[1]] == None:
		sys[m[1]] = [temp]
	else:
		sys[m[1]].append(temp)
	sys[m[0]] = sys[m[0]].remove(temp)
	
	# check
	pole = sys[tar]
	ideal = [3, 2 ,1]
	if pole is ideal:
		return m
	
	if str(sys) in dict:
		return -1
	else:
		dict[str(sys)] = 0
	
	# generate moves
	moves = generateMoves(sys)
	
	# recurtion
	path = []
	for i in moves:
		path.append(move(sys, i, tar))
	
	
	# retuns
	path.sort()
	return path[0]


class Tower:
	pole1 = []
	pole2 = []
	pole3 = []
	target = 0
	system = [pole1, pole2, pole3]
	
	def __init__(self):
		s = str(raw_input("Enter Order in Pole 1, if emplty enter 0 : "))
		if s != '0':
			self.pole1 = [int(x) for x in s.split(" ")]
		
		s = str(raw_input("Enter Order in Pole 2, if emplty enter 0 : "))
		if s != '0':
			self.pole2 = [int(x) for x in s.split(" ")]
			
		s = str(raw_input("Enter Order in Pole 3, if emplty enter 0 : "))
		if s != '0':
			self.pole3 = [int(x) for x in s.split(" ")]
		self.system = [self.pole1, self.pole2, self.pole3]
		
		self.target = int(raw_input("Enter the Target : "))
		
		print "Initial state of Towers", self.system 	
		
		self.start(self.system, self.target)
	
	
	def start(self, sys, tar):
		# check
		pole = sys[tar]
		ideal = [3, 2 ,1]
		if pole is ideal:
			print("No moves Required!!!")
			exit(0)
		
		
		# generate moves
		moves = generateMoves(sys)
		print(moves)
				
		
		# recurtion
		path = []
		for i in moves:
			path.append(move(sys, i, tar))
		
		
		print(path)



# MAIN

tObj = Tower()
