from random import randint
play=True
playtime = "0"
score_player = 0
score_computer = 0
def card_giveaway():
    global playercards
    global computercards
    global playercards_values
    global computercards_values
    playercards=0
    computercards=0
    playercards_values=[]
    computercards_values=[]
    
    playercard1 = randint(1,13)
    if playercard1 == 1:
        answer= input("Ace. Is it 1 or 11: ")
        if answer == "11":
            playercard1 = 11
            playercards_values.append("A(11)")
            print (playercards_values)
        elif answer == "1":
            playercard1 = 1
            playercards_values.append("A(1)")
            print (playercards_values)
        else:
            while answer != "1" or answer != "11":
                answer = input("Enter a valid value: ")
                if answer == "1":
                    playercard1 = 1
                    playercards_values.append("A(1)")
                    print (playercards_values)
                    break
                elif answer == "11":
                    playercard1 = 11
                    playercards_values.append("A(11)")
                    print (playercards_values)
                    break
                
    elif playercard1 == 11:
        playercard1 = "J"
        print ("First card value: ", playercard1)
        playercard1 = 10
        playercards_values.append("J")
        print (playercards_values)
    elif playercard1 == 12:
        playercard1 = "Q"
        print ("First card value: ", playercard1)
        playercard1 = 10
        playercards_values.append("Q")
        print (playercards_values)
    elif playercard1 == 13:
        playercard1 = "K"
        print ("First card value: ", playercard1)
        playercard1 = 10
        playercards_values.append("K")
        print (playercards_values)
    else:
        print ("First card value: ", playercard1)
        playercards_values.append(str(playercard1))
        print (playercards_values)
    
    playercard2 = randint(1,13)
    if playercard2 == 1:
        answer = input("Ace. Is it 1 or 11: ")
        if answer == "11":
            playercard2 = 11
            playercards_values.append("A(11)")
            print (playercards_values)
        elif answer == "1":
            playercard2 = 1
            playercards_values.append("A(1)")
            print (playercards_values)
        else:
            while answer != "1" and answer != "11":
                answer = input("Enter a valid value: ")
                if answer == "1":
                    playercard2 = 1
                    playercards_values.append("A(1)")
                    print (playercards_values)
                    break
                elif answer == "11":
                    playercard2 = 11
                    playercards_values.append("A(11)")
                    print (playercards_values)
                    break
                
    elif playercard2 == 11:
        playercard2 = "J"
        print ("Second card value: ", playercard2)
        playercard2 = 10
        playercards_values.append("J")
        print (playercards_values)
    elif playercard2 == 12:
        playercard2 = "Q"
        print ("Second card value: ", playercard2)
        playercard2 = 10
        playercards_values.append("Q")
        print (playercards_values)
    elif playercard2 == 13:
        playercard2 = "K"
        print ("Second card value: ", playercard2)
        playercard2 = 10
        playercards_values.append("K")
        print (playercards_values)        
    else:
        print ("Second card value: ", playercard2)
        playercards_values.append(str(playercard2))
        print (playercards_values)
        
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
                    print ("Extra card value: A(11)" )
                    playercards_values.append("A(11)")
                    print (playercards_values)
                elif answer == "1":
                    extracard = 1
                    print ("Extra card value: A(1)" )
                    playercards_values.append("A(1)")
                    print (playercards_values)
                else:
                    while answer != "1" and answer != "11":
                        answer = input("Enter a valid value: ")
                        if answer == "1":
                            extracard = 1
                            print ("Extra card value: A(1)" )
                            playercards_values.append("A(1)")
                            print (playercards_values)
                            break
                        elif answer == "11":
                            extracard = 11
                            print ("Extra card value: A(11)" )
                            playercards_values.append("A(11)")
                            print (playercards_values)
                            break
                
            elif extracard == 11:
                extracard = "J"
                print ("Extra card value: ", extracard)
                extracard = 10
                playercards_values.append("J")
                print (playercards_values)
            elif extracard == 12:
                extracard = "Q"
                print ("Extra card value: ", extracard)
                extracard = 10
                playercards_values.append("Q")
                print (playercards_values)
            elif extracard == 13:
                extracard = "K"
                print ("Extra card value: ", extracard)
                extracard = 10
                playercards_values.append("K")
                print (playercards_values)
            else:
                print ("Extra card value: ", extracard)
                playercards_values.append(str(extracard))
                print (playercards_values)
        
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
    global computercards_values, computercards
    computercard1 = randint(1, 13)
    if computercard1 == 1:
        answer = randint(1, 2)
        if answer == 1:
            computercard1 = 1
            computercards_values.append("A(1)")
        else:
            computercard1 = 11
            computercards_values.append("A(11)")
    elif computercard1 == 11:
        computercard1 = 10
        computercards_values.append("J")
    elif computercard1 == 12:
        computercard1 = 10
        computercards_values.append("Q")
    elif computercard1 == 13:
        computercard1 = 10
        computercards_values.append("K")
    else:
        computercards_values.append(str(computercard1))

    computercard2 = randint(1, 13)
    if computercard2 == 1:
        answer = randint(1, 2)
        if answer == 1:
            computercard2 = 1
            computercards_values.append("A(1)")
        else:
            computercard2 = 11
            computercards_values.append("A(11)")
    elif computercard2 == 11:
        computercard2 = 10
        computercards_values.append("J")
    elif computercard2 == 12:
        computercard2 = 10
        computercards_values.append("Q")
    elif computercard2 == 13:
        computercard2 = 10
        computercards_values.append("K")
    else:
        computercards_values.append(str(computercard2))

    computercards = computercard1 + computercard2
    return computercards

def actioncomputer(computercards):
    global computercards_values
    computer = True
    while computer:
        if computercards >= 17:
            computer = False
            break
        compextracard = randint(1, 13)
        if compextracard == 1:
            answer = randint(1, 2)
            if answer == 1:
                compextracard = 1
                computercards_values.append("A(1)")
            else:
                compextracard = 11
                computercards_values.append("A(11)")
        elif compextracard == 11:
            compextracard = 10
            computercards_values.append("J")
        elif compextracard == 12:
            compextracard = 10
            computercards_values.append("Q")
        elif compextracard == 13:
            compextracard = 10
            computercards_values.append("K")
        else:
            computercards_values.append(str(compextracard))

        computercards += compextracard
        if computercards > 21:
            break
    return computercards
        
def ending(playercards_values, computercards_values, computercards, playercards):
    global score_player, score_computer
    if playercards > 21:
        print("Player Busts! Computer Wins!")
        score_computer += 1
    elif computercards > 21:
        print("Computer Busts! Player Wins!")
        score_player += 1
    elif playercards > computercards:
        print("Player Wins!")
        score_player += 1
    elif computercards > playercards:
        print("Computer Wins!")
        score_computer += 1
    else:
        print("It's a Tie!")
    

    print("Your cards: ", computercards_values)
    print("Computer cards: ", playercards_values)
    print("Player: ", playercards)
    print("Computer: ", computercards)
    print("_________________________________")
    print ("Computer Score: ", score_computer)
    print ("Player Score: ", score_player)
    print ("________________________________")
    playtime = "1"



while play==True:
    if playtime == "0":
        card_giveaway()
        playercards = action(playercards)
        computercards = actioncomputer(computercards)
        ending(computercards_values, playercards_values, computercards, playercards)
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
    else:
        score_player = score_player
        score_computer = score_computer
        card_giveaway()
        playercards = action(playercards)
        computercards = actioncomputer(computercards)
        ending(computercards_values, playercards_values, computercards, playercards)
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
