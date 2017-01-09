# implementation of card game - Memory

import simplegui
import random

# creates board
l1 = range(8)
l2 = range(8)
board = l1 + l2

# creates an inital array of 16 Falses
exposed = [False] * 16

# some values used for positioning of cards
start = 15
step = 50
center = 60

# counters and indicies for flipped cards
turn_count = 0
cards_turned = 0
first_card = -1
second_card = -1

# helper function to initialize globals
def new_game():
    
    #shuffle board
    random.shuffle(board)
    
    # reset all global variables
    global exposed, cards_turned, first_card, second_card, turn_count
    turn_count = 0
    exposed = [False] * 16
    cards_turned = 0
    first_card = -1
    second_card = -1
    
    #update turn text
    label.set_text("Turns = " + str(turn_count))
     
# define event handlers
def mouseclick(pos):
    global turn_count, cards_turned, first_card, second_card
    
    # get horizontal coordinate of click
    click = list(pos)
    x_pos = pos[0]
    
    # use for loop to determine where position is
    for i in range(len(board)):
        
        #check which card's range the click falls in
        if ((x_pos < step*(i+1)) and (x_pos > 0 +(step*i))):
            
            # if already exposed do nothing
            if exposed[i] == True:
                return
            
            # if less than 2 cards exposed, flip and keep track of cards
            if cards_turned < 2:
                exposed[i] = True
                if cards_turned == 0:
                    first_card = i
                if cards_turned == 1:
                    second_card = i
                    turn_count += 1
                cards_turned += 1
                
            # if two cards turned, check if match, flip new card
            elif cards_turned == 2:
                if board[first_card] != board[second_card]:
                    exposed[first_card] = False
                    exposed[second_card] = False
                    first_card = i
                    second_card = -1
                    cards_turned = 1
                    exposed[i] = True
                else:
                    cards_turned = 1
                    exposed[i] = True
                    first_card = i
                    second_card = -1
    
    # update turn label
    label.set_text("Turns = " + str(turn_count))
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for i in range(len(board)):
        
        # if exposed draw the number
        if (exposed[i] == True):
            canvas.draw_text(str(board[i]),(start+step*i,center), 35, 'White')
        
        # if not exposed, draw green rectangle
        else:
            canvas.draw_polygon([[0+(step*i),0],[step*(i+1),0],[step*(i+1),100],[(step*i),100]],1,'White','Green')

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = " + str(turn_count))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

# Always remember to review the grading rubric