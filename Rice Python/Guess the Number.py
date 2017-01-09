# import needed modules
import simplegui
import random

"""
initialize global variable number_range to 100

initializing here prevents a new variable being created
every time new_game() is called

"""
number_range = 100

# helper function to start and restart the game
def new_game():
    
    # initialize secret_number as global to store number
    global secret_number
    
    #initialize number_guesses remaining as global
    global number_guesses
    
    # start game based on number_range
    if (number_range == 100):
        range100()
    else:
        range1000()
    
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game
    
    # use global versions of variables
    global secret_number, number_guesses, number_range
    
    # assign random number between 0-99
    secret_number = random.randrange(0,100)
    
    # assign number of guesses
    number_guesses = 7
    
    # set the number range to 100
    number_range = 100
    
    # print messages and new line
    print "New game. Range is [0,100)"
    print "Number of remaining guesses is", number_guesses
    print

def range1000():
    # button that changes the range to [0,1000) and starts a new game  
    
    # use global versions of variables
    global secret_number, number_guesses, number_range
    
    # assign random number between 0-999
    secret_number = random.randrange(0,1000)
    
    # assign number of guesses
    number_guesses = 10
    
    # set the number range to 1000
    number_range = 1000
    
    # print messages and new line
    print "New game. Range is [0,1000)"
    print "Number of remaining guesses is", number_guesses
    print
    
def input_guess(guess):
    # main game logic goes here	
    
    # use global number_guesses
    global number_guesses
    
    # decrement by 1 for each guess/function call
    number_guesses -= 1
    
    # cast inputted guess from string to integer
    guess = int(guess)
    
    #print guess
    print "Guess was", guess
    
    # print number of guesses remaining
    print "Number of remaining guesses is", number_guesses
    
    # if guess is correct, start new game
    if guess == secret_number:
        print "Correct!"
        print
        new_game()
        return
    
    # if 0 guesses left, print number, start new game
    if (number_guesses == 0):
        print "You ran out of guesses. The number was", secret_number
        print
        new_game()
        return
    
    # tell whether the number is higher or lower than guess
    if guess > secret_number:
        print "Lower!"
    else:
        print "Higher!"
        
    # new line for readability in ouputs
    print
    
# create frame
frame = simplegui.create_frame("Guess the Number", 200, 200)

# register event handlers for control elements and start frame
button1 = frame.add_button("Range is [0,100)",range100,100)
button2 = frame.add_button("Range is [0,1000)",range1000,100)
inp = frame.add_input("Guess:",input_guess,100)
frame.start()

# call new_game 
new_game()