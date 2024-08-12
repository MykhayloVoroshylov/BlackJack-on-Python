from random import randint
play=True
def card_giveaway():
    global playercards
    global computercards
    playercards=0
    computercards=0
    playercard1 = randint(1,13)
    if playercard1 == 1:
        answer= input("Ace. Is it 1 or 11: ")
        if answer == "11":
            playercard1 = 11
        elif answer == "1":
            playercard1 = 1
        else:
            while answer != "1" or answer != "11":
                answer = input("Enter a valid value: ")
                if answer == "1":
                    playercard1 = 1
                    break
                elif answer == "11":
                    playercard1 = 11
                    break
                
    elif playercard1 == 11:
        playercard1 = "J"
        print ("First card value: ", playercard1)
        playercard1 = 10
    elif playercard1 == 12:
        playercard1 = "Q"
        print ("First card value: ", playercard1)
        playercard1 = 10
    elif playercard1 == 13:
        playercard1 = "K"
        print ("First card value: ", playercard1)
        playercard1 = 10
    else:
        print ("First card value: ", playercard1)   
    
    playercard2 = randint(1,13)
    if playercard2 == 1:
        answer = input("Ace. Is it 1 or 11: ")
        if answer == "11":
            playercard2 = 11
        elif answer == "1":
            playercard2 = 1
        else:
            while answer != "1" and answer != "11":
                answer = input("Enter a valid value: ")
                if answer == "1":
                    playercard2 = 1
                    break
                elif answer == "11":
                    playercard2 = 11
                    break
                
    elif playercard2 == 11:
        playercard2 = "J"
        print ("Second card value: ", playercard2)
        playercard2 = 10
    elif playercard2 == 12:
        playercard2 = "Q"
        print ("Second card value: ", playercard2)
        playercard2 = 10
    elif playercard2 == 13:
        playercard2 = "K"
        print ("Second card value: ", playercard2)
        playercard2 = 10
    else:
        print ("Second card value: ", playercard2)
        
    playercards=playercard1+playercard2
    print ("You have: ", playercards)
    print ("________________________")
    return playercards
    
def action(playercards):
    player = True
    while player==True:
        action = input ("Hit(1) or Stay(2): ")
        if action == "1":
            extracard = randint(1,13)
            if extracard == 1:
                answer = input("Ace. Is it 1 or 11: ")
                if answer == "11":
                    extracard = 11
                elif answer == "1":
                    extracard = 1
                else:
                    while answer != "1" and answer != "11":
                        answer = input("Enter a valid value: ")
                        if answer == "1":
                            extracard = 1
                            break
                        elif answer == "11":
                            extracard = 11
                            break
                
            elif extracard == 11:
                extracard = "J"
                print ("Extra card value: ", extracard)
                extracard = 10
            elif extracard == 12:
                extracard = "Q"
                print ("Extra card value: ", extracard)
                extracard = 10
            elif extracard == 13:
                extracard = "K"
                print ("Extra card value: ", extracard)
                extracard = 10
            else:
                print ("Extra card value: ", extracard)
        
            playercards = playercards+extracard
            print ("Total: ", playercards)
            print("________________________")
        if action == "2":
            player = False
            print ("Total: ", playercards)
            print("________________________")
            break
        if playercards>21:
            break
    return playercards

def computer_cards():
    computercard1 = randint(1,13)
    if computercard1 == 1:
        answer= randint (1,2)
        if answer == 1:
            computercard1 = 1
        elif answer == 2:
            computercard1 = 11

    elif computercard1 == 11:
        computercard1 = 10
    elif computercard1 == 12:
        computercard1 = 10
    elif computercard1 == 13:
        computercard1 = 10
    
    computercard2 = randint(1,13)
    if computercard2 == 1:
        answer = randint(1,2)
        if answer == 1:
            computercard2 = 1
        elif answer == 2:
            computercard2 = 11
    elif computercard2 == 11:
        computercard2 = 10
    elif computercard2 == 12:
        computercard2 = 10
    elif computercard2 == 13:
        computercard2 = 10
        
    computercards=computercard2+computercard1
    return computercards
    
def actioncomputer(computercards):
    computer = True
    if computercards >= 19:
        computer = False
    while computer==True:
        action = randint(1,2)
        if action == 1:
            compextracard = randint(1,13)
            if compextracard == 1:
                answer = randint(1,2)
                if answer == 1:
                    compextracard = 1
                elif answer == 2:
                    compextracard = 11
                
            elif compextracard == 11:
                compextracard = 10
            elif compextracard == 12:
                compextracard = 10
            elif compextracard == 13:
                compextracard = 10
        
            computercards = computercards+compextracard
            if computercards >= 19:
                computer = False
            break
        if action == "2":
            computer = False
            break
        if computercards>21:
            break
    return computercards
        
def ending(playercards, computercards):
    print("Player: ", playercards)
    print("Computer: ", computercards)
    if playercards > computercards:
        if playercards>21:
            print("Computer Wins!")
        else:
            print("Player Wins!")
    elif computercards > playercards:
        if computercards>21:
            print("Player Wins!")
        else:
            print("Computer Wins!")
    elif computercards == playercards:
        print("Dealer(Computer) Wins!")

while play==True:
    card_giveaway()
    playercards = action(playercards)
    computercards = computer_cards()
    computercards = actioncomputer(computercards)
    ending(playercards, computercards)
    playagain = input ("Would you like to play again? (yes/no): ")
    if playagain == "yes":
        print("________________________")
        play=True
    elif playagain == "no":
        play=False
    else:
        while playagain != "yes" and playagain != "no":
            playagain = input("Would you like to play again? (yes/no): ")
            if playagain == "yes":
                print("________________________")                
                play=True
            elif playagain == "no":
                play=False
                break