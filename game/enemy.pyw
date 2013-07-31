import roomobject

class Enemy(roomobject.RoomObject):
	# simple enemy class
	# has health, damage and dropped item
	
	health=0
	damage=0
	droppeditem=''
	
	def __init__(self):
		# acts as a constructor
		self.health=100
		self.damage=10
		self.droppeditem="none"
		
	def Getname():
		pass