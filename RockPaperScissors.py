# Importing libraries for randint
from random import *

# Choose one of these
print('\nPlease select from the options')

# The subjects of the game. Rules are given. (Check README)
ai = ['rock', 'paper', 'scissors']
print(ai)

# User input _+_+_+_+_
choose_input = input('choose one option: ')

# Generate numbers between 0 to 2. 
ai = randint(0,2)

# Assign subjects with numbers.
if ai == 0:
	ai = 'rock'
elif ai == 1:
	ai = 'paper'
else:
	ai = 'scissors'

# Basic algorithm for Rock_Paper_Scissors
while choose_input:
	'''calls init'''
	if choose_input == ai:
		print(choose_input + ' vs ' + ai)
		print("both lost")
	elif choose_input == 'rock' and ai == 'scissors':
		print(choose_input + ' vs ' + ai)
		print("you smash ai's scissor and won")
	elif choose_input == 'scissors' and ai == 'rock':
		print(choose_input + ' vs ' + ai)
		print("ai smashes that scissor and wins",)
	elif choose_input == 'scissors' and ai == 'paper':
		print(choose_input + ' vs ' + ai)
		print("you cut ai's paper and won",)
	elif choose_input == 'paper' and ai == 'scissors':
		print(choose_input + ' vs ' + ai)
		print("ai cuts your paper and wins",)
	elif choose_input == 'paper' and ai == 'rock':
		print(choose_input + ' vs ' + ai)
		print("you wrap ai's rock and won")
	elif choose_input == 'rock' and ai == 'paper':
		print(choose_input + ' vs ' + ai)
		print("ai takes revenge and wins",)

	if choose_input not in ai:
		print('wrong subject')
		exit()
	else:
		exit() 



