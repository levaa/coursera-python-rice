# implementation of card game - Memory
import simplegui
import random as r

# helper function to initialize globals
def new_game():
    global cards, turn, solving, solved
    turn = state = 0
    cards = zip(range(8) + range(8),  [False] * 16)
    solved = set()
    solving = []
    r.shuffle(cards)
    label.set_text("Turns = "+str(turn))
           
# define event handlers
def mouseclick(pos):
    global turn, cards, solving, solved
    # add game state logic here
    solving.append(pos[0] // 50) 
    if len(solving) == 3: resolve()
        
    hide_onsolved()        
    show_solving_solved()
    label.set_text("Turns = "+str(turn))

def resolve():
    global turn, solving, solved
    idex1 = solving[0]
    idex2 = solving[1]
    idex3 = solving[2]
    card1 = cards[idex1]
    card2 = cards[idex2]
    
    if card1[0] == card2[0]:
        solved.add(idex1)
        solved.add(idex2) 
     
    solving = [idex3]    
    turn += 1
    
def show_solving_solved():
    global solved, cards, solving
    for i in solved.union(solving):
        card = cards[i] 
        cards[i] = (card[0], True)  

def hide_onsolved():
    global solved, cards      
    for i in set(range(16)).difference(solved.union(solving)):
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