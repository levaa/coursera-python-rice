# template for "Stopwatch: The Game"

import simplegui

# define global variables
tick  = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    a = str(t//600)
    b = str((t%600)//100) 
    c = str((t%100)//10)
    d = str(t%10)    
    return a + ":" + b + c + ":" + d

# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
    
def stop():
    timer.stop()
    
def reset():
    global tick
    tick = 0

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global tick
    tick += 1
    
# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(tick), [100,100], 50, "Red")
    
# create frame
frame = simplegui.create_frame("Stop Watch", 300, 300)

# register event handlers
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)

frame.set_draw_handler(draw_handler)

# start frame
frame.start()

# timer 
timer = simplegui.create_timer(100, timer_handler)

# Please remember to review the grading rubric
