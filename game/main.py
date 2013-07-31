import mainloop, display
functions = {'p': mainloop.Update, 'h': mainloop.Update, 'q': mainloop.QuitGame }
mainloop.MainMenu()
inp = input()
if inp in functions:
	functions[inp]()

while not mainloop.quit:
	display.Clear()	
	mainloop.Update()

display.CText("Thanks for playing you lovely human!")