import os
# from colorama import init
# init()
# from colorama import Fore, Back, Style
"""
This file only contains functions that display things in the 
output screen.
"""	
def Clear():
	os.system('cls')

#TText - Title text ("-------TITLE------") they are 
def TText(text):	
	length = len(text)
	margin = (80-length)/2
	if (margin % 2)==0:
		dashes = '-'*int(margin)
		print(dashes + text + dashes)
		#comment
	else:
		dashes = '-'*int(margin)
		print(dashes + text + dashes + '-')

#CText - Centres text in window("      TEXT       ")
def CText(text):
	length = len(text)
	margin = (80-length)/2
	if (margin % 2)==0:
		dashes = ' '*int(margin)
		print(dashes + text + dashes)
		#comment
	else:
		dashes = ' '*int(margin)
		print(dashes + text + dashes + ' ')
		
def TabbedText(text):
	print(' '*4 + text)
	
def ListInstructions( title, *instructions):
	print("\n" + title + "\n")
	for i in instructions:
		TabbedText(i)