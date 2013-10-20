# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors
 
import random
 
def number_to_name(number):
    if number == 0:
        name = "rock"
    elif number == 1:
        name = "Spock"
    elif number == 2:
        name = "paper"
    elif number == 3:    
        name = "lizard"
    elif number == 4:    
        name = "scissors"
    else:
        name = "Houston we have a problem!"
    
    return name
 
    
def name_to_number(name):
    if name == "rock":
        number = 0
    elif name == "Spock":
        number = 1
    elif name == "paper":
        number = 2
    elif name == "lizard":    
        number = 3
    elif name == "scissors":    
        number = 4
    else:
        number = -1 # error 
    
    return number 
 
 
def rpsls(name): 
    
    player_number = name_to_number(name)
    comp_number = random.randrange(0, 5)    
    diff  = (player_number - comp_number) % 5
    
    if player_number > comp_number:
        winner = "Player wins!"
    elif player_number == comp_number:
        winner = "Player and computer tie!"
    else:
        winner = "Computer wins!"
    
    print ("Player chooses "+name) 
    print ("Computer chooses "+number_to_name(comp_number))
    print (winner)
    print ("")
    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
