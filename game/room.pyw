import display
from random import randint, seed

# this module just creates a room from a random list of 
# possible items
# rooms can be empty, have an enemy or have an item
# for now, better variation will be later
class MapRoom:
	hidden = True
	type = ""
	seed()
	
	def __init__(self, roomtype="random"):
		# init code
		if roomtype=="random":
			ran=randint(0,3)
			if ran==0:
				roomtype="enemy"
			elif ran==1:
				roomtype="item"
			elif ran==2:
				roomtype="empty"
			# random number generator
			
			
		if roomtype=="enemy":
			# spawn a monster
			self.type=roomtype
		elif roomtype=="item":
			# spawn an item
			self.type=roomtype
		elif roomtype=="empty":
			#empty room
			self.type=roomtype
		else:
			#empty room
			self.type="empty"
		
		# Set the room to hidden
		self.hidden = True
		#
	def GetSymbol(self):
		if self.type=="enemy":
			return "@"
		elif self.type=="item":
			return "#"
		elif self.type=="empty":
			return "0"
		else:
			return "0"