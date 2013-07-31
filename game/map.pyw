import display, room
from random import randint, seed
# map size variables
mapx=20
mapy=10
# ensures map fits on screen
if mapx > 80:
	mapx=77
if mapy > 15:
	mapy=15
	
maprooms=[]


def Seed(seednum):
	global map, maprooms
	seed()
		
	for y in range(mapy):
		for x in range(mapx):
			ran=randint(0,3)
			# randomly assign each room
			if ran==0:
				maprooms.append(room.MapRoom("enemy"))
			elif ran==1:
				maprooms.append(room.MapRoom("item"))
			elif ran==2:
				maprooms.append(room.MapRoom("empty"))
			elif ran==3:			
				maprooms.append(room.MapRoom())
				
def Draw():	
	display.Clear()
	display.TText("Map!")
		
	print( '-' * (mapx+2))
	while len(maprooms)>1:
		for y in range(mapy):
			total = '|'
			for x in range(mapx):	
				total += maprooms.pop().GetSymbol()
			total += '|'
			print(total)
	print( '-' * (mapx+2))
	display.ListInstructions("Legend:", "@ - Enemy room", "# - Item room", "0 - Empty room")
		