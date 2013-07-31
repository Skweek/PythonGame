import display, map
quit=False
firsttime=True
def MainMenu():
	display.TText("Welcome!")
	print()
	display.CText("[P]lay")
	display.CText("[H]elp")
	display.CText("[Q]uit")
	map.NewMap(1)
	
def Update():		
	# eventually handle player.Update() here
	# then map.Update()
	display.Clear()
	map.Draw()
	
	#now what?
	display.ListInstructions("What is your next move commander sir?", "q - Back")
	inp = input()
	if inp=='q':
		QuitGame()
	else: 
		pass
	# now we handle map commands
		
def QuitGame():
	global quit
	quit=True