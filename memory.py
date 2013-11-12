# implementation of card game - Memory
# http://www.codeskulptor.org/#user24_jNBgElYVYR_7.py
import simplegui
import random as r

# helper function to initialize globals
def new_game():
    global cards, width, turn, fst, prev, idex  
    faces = [False] * 16
    turn = 0
    prev = -1
    idex = -1
    cards = zip(range(8) + range(8), [False] * 16)
    r.shuffle(cards)
    label.set_text("Turns = "+str(turn))
           
# define event handlers
def mouseclick(pos):
    global turn, cards, idex, prev
    # add game state logic here
    idex = pos[0] // 50
    card_new = cards[idex]
    card_old = cards[prev] 

    if card_new == card_old:
        card_new = (card_new[0], True)
        card_old = (card_old[0], True)
    else:
        card_new = (card_new[0], False)
        card_old = (card_old[0], False)
        
    turn += 1      
    cards[idex] = card_new
    cards[prev] = card_old
    label.set_text("Turns = "+str(turn))
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    i = 1
    offset = 0
    for card in cards:
        if(card[1]):
            canvas.draw_text(str(card[0]), (offset + 17, 70), 40, "White")  
        else: 
            canvas.draw_polygon([(offset, 0), 
                                 (offset, 100), 
                                 (offset + 50, 100),
                                 (offset + 50, 0)], 
                                 1, "Black", "Green")               
        i += 1    
        offset += 50 


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric 