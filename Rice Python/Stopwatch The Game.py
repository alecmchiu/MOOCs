# importing modules
import simplegui
import time

# define global variables
time_in_sec = 0
number_stops = 0
number_whole_second = 0
stop_ratio = "0/0"

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    
    # copy input time to modify
    time = t
    
    # calculate milliseconds
    ms = time % 10
    time /= 10
    
    # calculate seconds
    seconds = time % 60
    
    # format seconds
    if(seconds < 10):
        str_seconds = "0" + str(seconds)
    else:
        str_seconds = str(seconds)
    
    # calculate minutes
    minutes = time/60
    
    # return formatted string
    string = str(minutes) + ":" + str_seconds + "." + str(ms)
    return string
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()

def stop():
    
    #check if timer is running
    #if so, increment number_stops
    #increment whole_second stops if necessary
    if (timer.is_running()):
        global number_stops
        number_stops += 1
        global time_in_sec
        if (time_in_sec % 10 == 0):
            global number_whole_second
            number_whole_second += 1
    
    #stop the timer
    timer.stop()
    
    #set the stop ratio
    global stop_ratio
    stop_ratio = str(number_whole_second) + "/" + str(number_stops)

# resets everything
def reset():
    
    #if timer is running, stop it
    if (timer.is_running()):
        timer.stop()
    
    #reset all global variables
    global time_in_sec, number_stops, number_whole_second,stop_ratio
    time_in_sec = 0
    number_stops = 0
    number_whole_second = 0
    stop_ratio = "0/0"

# define event handler for timer with 0.1 sec interval
def timer_inc():
    global time_in_sec
    time_in_sec += 1

# define draw handler
def draw(canvas):
    canvas.draw_text(format(time_in_sec),(90,105),50,'White')
    canvas.draw_text(stop_ratio,(205,50),50,'White')

# create frame
frame = simplegui.create_frame("Stopwatch: The Game",300,125)

#create buttons
start_button = frame.add_button("Start",start, 200)
stop_button = frame.add_button("Stop",stop, 200)
reset_button = frame.add_button("Reset",reset, 200)

#set draw handler
frame.set_draw_handler(draw)

# create timer
timer = simplegui.create_timer(100,timer_inc)

# start frame
frame.start()
