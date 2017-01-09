# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

# ball spawn function
def spawn_ball(direction):
    
    # global variables to store ball's position and velocity
    global ball_pos, ball_vel
    
    # initialize ball in center with 0 initial velocity
    ball_pos = [300,200]
    ball_vel = [0,0]
    
    # if the ball will move left, spawn x & y vel < 0
    # if the ball will spawn right, spawn x_vel > 0 and y_vel < 0
    # note that draw handler will run ~60x/sec
    # it will update at (60*vel) pixels/sec
    if (direction == LEFT):
        ball_vel[0] = -(random.randrange(2,4))
        ball_vel[1] = -(random.randrange(1,3))
    if (direction == RIGHT):
        ball_vel[0] = random.randrange(2,4)
        ball_vel[1] = -(random.randrange(1,3))

# new_game function that resets the game
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel
    
    # roughly centered and not moving paddles
    paddle1_pos = HEIGHT/2 - PAD_HEIGHT/2
    paddle2_pos = HEIGHT/2 - PAD_HEIGHT/2
    paddle1_vel = 0
    paddle2_vel = 0
    
    global score1, score2
    
    # initialized scores of 0
    score1 = 0
    score2 = 0
    
    # random initial ball spawn direction
    start = random.randrange(0,2)
    if (start == 0):
        spawn_ball(LEFT)
    else:
        spawn_ball(RIGHT)

# draw handler
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # if ball hits wall, change y direction
    if(ball_pos[1] >= HEIGHT - BALL_RADIUS):
        ball_vel[1] *= -1
    if(ball_pos[1] <= BALL_RADIUS):
        ball_vel[1] *= -1
    
    # update ball position
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
            
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, 'White', 'White')
    
    # update paddle's vertical position, keep paddle on the screen
    if ((paddle1_pos + paddle1_vel > 0) and (paddle1_pos + PAD_HEIGHT + paddle1_vel < HEIGHT)):
        paddle1_pos += paddle1_vel
    if ((paddle2_pos + paddle2_vel > 0) and (paddle2_pos + PAD_HEIGHT + paddle2_vel < HEIGHT)):
        paddle2_pos += paddle2_vel
    
    # draw paddles
    canvas.draw_polygon([(0,paddle1_pos),(PAD_WIDTH,paddle1_pos),(PAD_WIDTH,paddle1_pos+PAD_HEIGHT),(0,paddle1_pos + PAD_HEIGHT)],1,"White", "White")
    canvas.draw_polygon([(WIDTH-PAD_WIDTH,paddle2_pos),(WIDTH,paddle2_pos),(WIDTH,paddle2_pos + PAD_HEIGHT),(WIDTH-PAD_WIDTH,paddle2_pos + PAD_HEIGHT)],1,"White","White")
    
    # determine whether paddle and ball collide
    # if so, update ball velocity
    # if ball did not collide, a player scored and ball will be respawned
    if (ball_pos[0] <= PAD_WIDTH + BALL_RADIUS):
        if (ball_pos[1] > paddle1_pos and ball_pos[1] < paddle1_pos + PAD_HEIGHT):
            ball_vel[0] *= -1.1
        else:
            spawn_ball(RIGHT)
            score2 += 1
    if (ball_pos[0] >= ((WIDTH- PAD_WIDTH) - BALL_RADIUS)):
        if (ball_pos[1] > paddle2_pos and ball_pos[1] < paddle2_pos + PAD_HEIGHT):
            ball_vel[0] *= -1.1
        else:    
            spawn_ball(LEFT)
            score1 += 1
    
    # draw scores
    canvas.draw_text(str(score1),(0.25*WIDTH,75),50,"White")
    canvas.draw_text(str(score2),(0.75*WIDTH,75),50,"White")

# keydown event handler
def keydown(key):
    global paddle1_vel, paddle2_vel
    
    # left paddle controls
    if (key == ord('W')):
        paddle1_vel = -4
    if (key == ord('S')):
        paddle1_vel = 4
        
    # right paddle controls
    if (key == simplegui.KEY_MAP['up']):
        paddle2_vel = -4
    if (key == simplegui.KEY_MAP['down']):
        paddle2_vel = 4
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    
    #left paddle stop
    if (key == ord('W') or key == ord('S')):
        paddle1_vel = 0
        
    #right paddle stop
    if (key == simplegui.KEY_MAP['up'] or key == simplegui.KEY_MAP['down']):
        paddle2_vel = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)

# event handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

# reset button
frame.add_button("Restart",new_game)

# start game and frame
new_game()
frame.start()