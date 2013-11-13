# implementation of card game - Memory
import simplegui
import random as r

# helper function to initialize globals
def new_game():
    global cards, turn, solving, solved
    turn = state = 0
    cards = zip(range(8) + range(8),  [False] * 16)
    solved = set()
    solving = set()
    r.shuffle(cards)
    label.set_text("Turns = "+str(turn))
           
# define event handlers
def mouseclick(pos):
    global turn, cards, solving, solved
    # add game state logic here
    idx = pos[0] // 50
    card = cards[idx]
    if not card[1]:
        card = (card[0],True)
        if len(solving) == 2: resolve()
        else: solving.add((idx, card)) 

    show_solved()
    hide_onsolved()
    cards[idx] = card 
    solving.add((idx, card))        
    label.set_text("Turns = "+str(turn))

def resolve():
    global turn, solving, solved
    tupl1 = solving.pop()
    tupl2 = solving.pop()
    idex1 = tupl1[0]
    idex2 = tupl2[0]
    card1 = tupl1[1]
    card2 = tupl2[1]
    
    print (idex1, idex2, card1, card2)
    
    if card1[0] == card2[0]:
        solved.add(idex1)
        solved.add(idex2) 
    
    solving = set()
    turn += 1
    
def show_solved():
    global solved, cards
    for i in solved:
        card = cards[i] 
        cards[i] = (card[0], True)  

def hide_onsolved():
    global solved, cards      
    for i in set(range(16)).difference(solved):
        card = cards[i]
        cards[i] = (card[0], False)  
                        
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