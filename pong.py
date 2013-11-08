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
PAD_VEL = 2

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2]
    ball_vel = [0,0]
    ball_vel[1] = random.randrange(60, 180) / 60
    
    if direction: 
        ball_vel[0] = random.randrange(120, 240) / 60
    else:    
        ball_vel[0] = -random.randrange(120, 240) / 60
        
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    
    paddle1_pos = HEIGHT/2 - HALF_PAD_HEIGHT
    paddle2_pos = HEIGHT/2 - HALF_PAD_HEIGHT
    paddle1_vel = 0
    paddle2_vel = 0
    score1 = 0
    score2 = 0
    spawn_ball(RIGHT)
    
def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel

    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    lb = BALL_RADIUS + PAD_WIDTH # left 
    rb = WIDTH - BALL_RADIUS - PAD_WIDTH # right 
    tb = HEIGHT - BALL_RADIUS # top 
    bb = BALL_RADIUS # bottom 
    
    if ball_pos[1] <= bb or ball_pos[1] >= tb:
        ball_vel[1] -= 1        

    if ball_pos[0] <= lb:
        if ball_pos[1] >= paddle1_pos and ball_pos[1] <= paddle1_pos + PAD_HEIGHT:
            ball_vel[0] *= -1
        else:
            spawn_ball(RIGHT)
            score2 += 1
        
    if ball_pos[0] >= rb:
        if ball_pos[1] <= paddle2_pos + PAD_HEIGHT and ball_pos[1] >= paddle2_pos:
            ball_vel[0] *= -1
        else:
            spawn_ball(LEFT)
            score1 += 1          
        
    # draw ball
    c.draw_circle(ball_pos, BALL_RADIUS, 1, "White", "White")    
            
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel  
        
    if paddle1_pos + HALF_PAD_HEIGHT >= HEIGHT:
        paddle1_pos = HEIGHT - HALF_PAD_HEIGHT
    
    if paddle1_pos - HALF_PAD_HEIGHT <= 0:
        paddle1_pos = HALF_PAD_HEIGHT

    if paddle2_pos + HALF_PAD_HEIGHT >= HEIGHT:
        paddle2_pos = HEIGHT - HALF_PAD_HEIGHT
    
    if paddle2_pos - HALF_PAD_HEIGHT <= 0:
        paddle2_pos = HALF_PAD_HEIGHT    
    
    # draw paddles
    x = paddle1_pos - HALF_PAD_HEIGHT 
    y = paddle1_pos + HALF_PAD_HEIGHT
    c.draw_polygon([(0, x),(0, y),(PAD_WIDTH, y),(PAD_WIDTH, x)], 1, "White", "White")

    x = paddle2_pos - HALF_PAD_HEIGHT 
    y = paddle2_pos + HALF_PAD_HEIGHT 
    z = WIDTH - PAD_WIDTH 
    c.draw_polygon([(WIDTH, x),(WIDTH, y),(z, y),(z, x)], 1, "White", "White")    

    # draw scores
    c.draw_text(str(score1),(270, 20), 20, "White")
    c.draw_text(str(score2),(320, 20), 20, "White")
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = -PAD_VEL
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel = PAD_VEL
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel = -PAD_VEL
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel = PAD_VEL   
        
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()