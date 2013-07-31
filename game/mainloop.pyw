import display, map
quit=False
firsttime=True
def MainMenu():
	display.TText("Welcome!")
	print()
	display.CText("[P]lay")
	display.CText("[H]elp")
	display.CText("[Q]uit")
	map.Seed(1)
	
def Update():		
	# eventually handle player.Update() here
	# then map.Update()
	map.Draw()
	
	#now what?
	display.ListInstructions("What is your next move commander sir?", "q - Back")
	inp = input()
	if inp=='q':
		QuitGame()
	# now we handle map commands
		
def QuitGame():
	global quit
	quit=True