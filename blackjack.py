# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
dealer_fist_card_pos = [80, 100]
player_fist_card_pos = [80, 340] 

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print ("Invalid card: ", suit, rank)

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        print self.rank
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        # create Hand object
        self.cards = []

    def __str__(self):
        # return a string representation of a hand
        result = ""
        for card in self.cards: 
            result += str(card) + " " 
        return result               

    def add_card(self, card):
        # add a card object to a hand
        self.cards.append(card)
        
    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        result = 0 
        for card in self.cards:
            rank = card.get_rank()
            print ("rank", rank)
            cval = VALUES[rank]
            result += cval
            if rank == 'A' and result < 12: result += 10
            
        return result                
    
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        i = 0 
        while i < len(self.cards):
            p = pos
            if i > 0: p = [pos[0]+(75 * i), pos[1]]
            self.cards[i].draw(canvas, p)
            i += 1    

# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
               self.cards.append(Card(suit, rank))
        self.shuffle()

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.cards)

    def deal_card(self):
        # deal a card object from the deck
        return self.cards.pop()
        
    def __str__(self):
        result = ""
        for card in self.cards:
            result += str(card) + " "
        return result     
    
#define event handlers for buttons
def deal():
    global outcome, in_play, score, player, dealer, dealer_cards_pos, player_cards_pos 

    # your code goes here
    if in_play: score -=1 

    deck = Deck()
    player = Hand()
    dealer = Hand()   
    for i in range(2): # deal two cards each
        dealer.add_card(deck.deal_card())
        player.add_card(deck.deal_card())

    outcome = "New Hand!"
    in_play = True

def hit():
    # replace with your code below
    global in_play, score, outcome, deck, player, dealer    
    # if the hand is in play, hit the player
    print (in_play, score, outcome, "Dealer " + str(dealer), "Player " + str(player))
    if in_play:
        player.add_card(deck.deal_card())
        outcome = "Hit or stand? "

    # if busted, assign a message to outcome, update in_play and score
    if player.get_value() > 21:
        outcome = "Payer Busted! "
        score -= 1
    
    outcome += "Player:" +str(player.get_value())+" Dealer: "+str(dealer.get_value())       

def stand():
    # replace with your code below
    global in_play, score, message, outcome, player, dealer, deck
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play:
        while dealer.get_value() < 18:
            dealer.add_card(deck.deal_card())

    else: outcome = "Game Over" 
       
    # assign a message to outcome, update in_play and score
    if in_play:
        outcome = "Player: " +str(player.get_value())+" Dealer: "+str(dealer.get_value())
        in_play = False 
        if dealer.get_value > 21:  
            outcome += " Player Wins!"
            score += 1 
        elif player.get_value() > dealer.get_value():
            outcome += " Player Wins!"
            score += 1             
        else:
            outcome += " Dealer Wins!"
            score -= 1    
            
# draw handler    
def draw(canvas):
    global player, dealer, score, outcome
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text("Blackjack", [250, 50], 40, "White")
    canvas.draw_text("Score: " + str(score), [500,75], 24, "White")
    canvas.draw_text("Dealer: ", [20,100], 24, "White")
    dealer.draw(canvas, dealer_fist_card_pos)   
    canvas.draw_text(outcome, [30,250], 18, "White")
    canvas.draw_text("Player: ", [20,340], 24, "White")
    player.draw(canvas, player_fist_card_pos)

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback 
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deck = Deck()
player = Hand() 
dealer = Hand()
deal()
frame.start()


# remember to review the gradic rubric 