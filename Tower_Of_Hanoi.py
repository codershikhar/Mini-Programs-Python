def move(sys, m, tar):
	# do the move
	temp = sys[m[0]][-1]
	sys[m[1]].append(temp)
	sys[m[0]] = sys[m[0]].remove(temp)
	
	
	# check
	pole = sys[tar]
	ideal = [3, 2 ,1]
	if pole is ideal:
		return m
	
	# generate moves
	# recurtion
	# retuns
	pass


class Tower:
	pole1 = []
	pole2 = []
	pole3 = []
	target = 0
	system = [pole1, pole2, pole3]
	
	def __init__(self):
		s = str(input("Enter Order in Pole 1, if emplty enter 0 : "))
		if s != '0':
			self.pole1 = [int(x) for x in s.split(" ")]
		
		s = str(input("Enter Order in Pole 2, if emplty enter 0 : "))
		if s != '0':
			self.pole2 = [int(x) for x in s.split(" ")]
			
		s = str(input("Enter Order in Pole 3, if emplty enter 0 : "))
		if s != '0':
			self.pole3 = [int(x) for x in s.split(" ")]
		self.system = [self.pole1, self.pole2, self.pole3]
		
		self.target = int(input("Enter the Target : "))
		
		print("Initial state of Towers", self.system)
		
		self.start(self.system, self.target)
	
	
	def start(self, sys, tar):
		# check
		pole = sys[tar]
		ideal = [3, 2 ,1]
		if pole is ideal:
			print("No moves Required!!!")
			exit(0)
		
		
		# generate moves
		moves = []
		for i in range(3):
			for j in range(3):
				if len(sys[i]) > 0:
					if i != j:
						if len(sys[j]) == 0:
							moves.append((i, j))
						else:
							if sys[j][-1] > sys[i][-1]:
								moves.append((i, j))
		print(moves)
				
		
		# recurtion
		path = []
		for i in moves:
			path.append(move(sys, i, tar))
		
		
		# print path



# MAIN

tObj = Tower()
