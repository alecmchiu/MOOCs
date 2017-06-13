#!/usr/bin/env python3

print("Please think of a number between 0 and 100!")

response = ""
n_low = 0
n_high = 100
n = int((n_low + n_high) / 2)
while response != "c":
	print("Is your number {}?".format(n))
	response = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
	if response == "l":
		n_low = n
		n = int((n_high + n)/2)
	elif response == "h":
		n_high = n
		n = int((n + n_low)/2)
	elif response == "c":
		break
	else:
		print("Sorry, I did not understand your input.")

print("Game over. Your secret number was: {}".format(n))