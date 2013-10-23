# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui, random

# initialize global variables used in your code
high = 0
low = 0
answer = 0
attemps = 0

# helper function to start and restart the game
def new_game():
    global answer, attemps  
    answer = random.randint(0, high)
    print (" ")    
    if high == 0: 
       print("Please pick a range first or will default to [0, 100)")
       range100()         
        
    if attemps != 10 or attemps != 7:
        if high == 1000: attemps = 10
        if high == 100: attemps = 7    
        
# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global high, low, attemps
    print ("Setting Range to [0,100)")    
    high = 100
    low = 0
    new_game()
    
def range1000():
    # button that changes range to range [0,1000) and restarts
    global high, low, attemps
    print ("Setting Range to [0,1000)")
    high = 1000
    low = 0

    new_game()
    
def input_guess(guess):
    # main game logic goes here 
    global answer, attemps
    
    # not going to validate it since material does not cover that yet
    guess_num = int(guess) 
    attemps = attemps - 1
    
    print (" ") 
    print ("Your Guess is "+guess)
    
    won = False
    
    if attemps < 0: 
        print("You Lost!. The number was: "+str(answer)+"... Let's go again!")  
        new_game() 
    else:
        if guess_num == answer:
            print("You Win!!! ... Let's go again!")
            won = True 
            new_game()
        else:    
            if guess_num > answer:
                print ("Go Lower!")
            elif guess_num < answer:
                print ("Go Higher!")
                
    if attemps >= 0 and not won:
        print ("Number of guesses left: "+str(attemps))
    
# create frame
frame = simplegui.create_frame('guess game', 500, 500, 350)

# register event handlers for control elements
frame.add_button('Range: 0 - 100', range100, 200)
frame.add_button('Range: 0 - 1000', range1000, 200)
frame.add_input('Take a Guess', input_guess, 200)


# call new_game and start frame
new_game()
frame.start()