import random
oyuncu_score = 0
computer_score = 0
print ("welcome rock/paper/scissor game")
print("The game ends when either one of them reach 3!\n")

while True:
    
    kullanici_secimi = input("please enter your weapon (rock/paper/scissor) ")
    kullanici_secimi.lower().strip()
    tkm = {1: "rock", 2: "paper", 3 : "scissor"}
    sec = ["rock", "paper", "scissor"]
    com_secimi = random.choice(sec)
    print(f"Player choice: {kullanici_secimi} | Computer choice : {com_secimi}")

    if kullanici_secimi == com_secimi:
        print("tie! no one wins")
    elif (kullanici_secimi == tkm[1]) and (com_secimi == tkm[2]):
        print("paper beats rock - computer wins")
        computer_score += 1
    elif (kullanici_secimi == tkm[2]) and (com_secimi == tkm[1]): 
        print("paper beats rock - user wins")
        oyuncu_score += 1
    elif (kullanici_secimi == tkm[1]) and (com_secimi == tkm[3]):
        print("rock beats scissor - user wins")
        oyuncu_score += 1
    elif (kullanici_secimi == tkm[3]) and (com_secimi == tkm[1]):
        print("rock beats scissor - computer wins")
        computer_score += 1
    elif (kullanici_secimi == tkm[2]) and (com_secimi == tkm[3]):
        print("scissor beats paper- computer wins")
        computer_score += 1
    elif (kullanici_secimi == tkm[3]) and (com_secimi == tkm[2]):
         print("scissor beats paper - user wins")
         oyuncu_score += 1
    
    print(f"\nUser wins {oyuncu_score} time(s) | Computer wins {computer_score} time(s)\n")
    
    
    if oyuncu_score == 3:
        print("\nUser has won the game")
        break
    elif computer_score == 3:
        print("\nComputer has won the game")
        break
        
