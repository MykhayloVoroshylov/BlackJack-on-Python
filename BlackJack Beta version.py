from random import randint
import time

# Global variables
score = 0
dishonorable = False  # Track dishonorable status
reason = "nothing"
deserts = 0

def computer_turn(deadly_number, count):
    global score, dishonorable, reason, deserts
    print("Computer's turn...")
    print("Putting muzzle to head...")
    time.sleep(2)
    print("Taking risks...")
    time.sleep(1)
    print("Pulling trigger...\n")
    count += 1

    if count == deadly_number:
        print("BANG! Computer is eliminated.")
        score += 1  # Add score when the player wins the round
        print("Your current score: ", score)
        return "computer", count, False
    else:
        print("CLICK! Your turn.")
        if deadly_number == 6 and count == 5:
            # Final chamber scenario
            print("You had a chance to desert, yet the drum reached the last chamber, and it has a bullet.")
            print("Make your choice:")
            print("1. Shoot the computer (Dishonorable, but you survive).")
            print("2. Take the shot yourself (Honorable, but you are dead).")
            
            choice = input("Enter 1 to shoot the computer, or 2 to take the shot yourself: ")

            if choice == "1":
                final_bullet = randint(1,100)
                if final_bullet in range (1,5):
                    print("You chose dishonor by shooting computer.")
                    time.sleep(1)
                    print("Click! Uh oh, computer was testing you and your conscience. You failed!")
                    time.sleep(1)
                    print("Computer takes out his gun, and shoots at you. You are eliminated!")
                    print(f"Game Over! Your final score: {score}")
                    score = 0
                    deserts = 0
                    return "player", count, False  # Player loses
                else:
                    print("You chose dishonor by shooting the computer.")
                    time.sleep(1)
                    print("BANG! Computer is eliminated")
                    print("You survive, but you are marked as Dishonorable. Redemption will be required.")
                    reason = "murder"
                    score += 1
                    dishonorable = True
                    return "player", count, False  # End the round
            elif choice == "2":
                print("You chose to take the honorable path. Prepare for the final shot...")
                print("Rolling the drum...")
                time.sleep(2)
                final_bullet = randint (1,100)
                if final_bullet in range (1,5):
                    print ("Click! You miraculously survived. The computer is laughing and saying that he will not kill someone who is so entertaining and has a funny face when facing death.\n You receive an extra point for score")
                    score += 2
                else:
                    print("BANG! You are eliminated. An honorable end.")
                    print(f"Game Over! Your final score: {score}")
                    deserts = 0
                    return "player", count, False  # Player loses
            else:
                print("Invalid choice. You hesitated, and the computer shoots you out of impatience!")
                return "player", count, False  # Player loses due to invalid choice
        else:
            # Default choice for normal gameplay
            choice = input("Perhaps you don't want to lose. Do you want to stay alive and desert? (Yes/No): ").lower()
            if choice == "yes":
                print("You deserted and are alive! However, for unsportsmanlike behavior, your score is set to 0.")
                desert()  # Track desertions
                return "player", count, False  # End the round
            elif choice == "no":
                return "player", count, True
            else:
                print("Invalid choice. The computer doesn't understand gibberish and eliminates you.")
                print(f"Game Over! your final score is: {score}")
                return "player", count, False

                
def desert():
    global deserts, dishonorable, reason, score
    deserts += 1  # Increment desert count
    if deserts == 3:
        print("You have deserted 3 times! You are now dishonored!")
        reason = "desertion"
        dishonorable = True  # Mark as dishonorable after 3 desertions
        print("You are now dishonorable for desertion. Redemption will be required.")
    else:
        print(f"You have deserted {deserts} time(s). You better stop it before it's too late.")
    score = 0  # Reset score when the player deserts


def player_turn(deadly_number, count):
    global score, deserts
    print("Your turn...")
    print("Putting muzzle to head...")
    time.sleep(2)
    print("Taking risks...")
    time.sleep(1)
    print("Pulling trigger...\n")
    count += 1
    if count == deadly_number:
        print("BANG! You are eliminated.")
        print(f"Game Over! Your final score: {score}")  # Show score at the end if the player loses
        deserts = 0
        score = 0  # Reset score when the player dies
        return "player", count, False
    else:
        print("CLICK! Computer's turn.")  # <-- This can be the only place the "Computer's turn" message is printed.
        return "computer", count, True


def dishonorable_round(deadly_number, count):
    print("It's time to play again player, I mean Bastard. This time, it would be harder to survive than usually.")
    response2 = input(("Unlike you, coward, I have conscience and honesty, without saying anything about honor.\nTherefore I give you the chance, before the round begins.\n Do you want to redeem yourself, and have a fair game? (Yes/No)")).lower()
    if response2 == "yes":
        print("Ok, it's a wise choice.")
        seek_forgiveness(dishonorable, score, deserts)
    elif response2 == "no":
        print("I know there are dumb people, but you... you weren't even in line when God was giving out brains. Your choice...")
        # Pass deadly_number and count to dishonorable_game_loop
        dishonorable_game_loop(deadly_number, count)


def seek_forgiveness(dishonorable, score, deserts):
    if dishonorable:
        print("You are marked as Dishonorable. Redemption is possible, but it will not be easy.")
        print("You must complete a forgiveness task to erase your dishonor.")
        
        while True:
            print("Choose your path to forgiveness:")
            print("1. Survive 5 honorable turns.")
            print("2. Take the Forgiveness Challenge.")
            print("3. Face execution.")
            choice = input("Enter 1, 2, or 3: ")

            if choice == "1":
                print("Survive 5 turns honorably. Each turn, the drum is rolled.")
                honor_turns = 0
                deadly_number = randint(1, 6)

                while honor_turns < 5:
                    print("Rolling Drum")
                    turn, count, game_on = player_turn(deadly_number, 0)

                    if not game_on:
                        print("You failed to meet the forgiveness criteria. Try again later.")
                        print(f"Game Over! Your final score: {score}")
                        return dishonorable
                    
                    honor_turns += 1  # Increment after player's turn
                    
                    if honor_turns < 5:  # Only proceed to computer's turn if player survived
                        print("Rolling Drum")
                        turn, count, game_on = computer_turn(deadly_number, 0)

                        if not game_on:
                            print("You failed to meet the forgiveness criteria. Try again later.")
                            print(f"Game Over! Your final score: {score}")
                            return dishonorable

                print("Your bravery has redeemed you. You are forgiven!")
                deserts = 0
                return False

            elif choice == "2":
                print("You must face the Forgiveness Challenge.")
                print("Spin the drum and take two shots in one turn. Or desert and be executed immediately.")
                response = input("What is your choice? Execution/Challenge: ").lower()
                if response == "challenge":
                    for i in range(2):  # Two shots
                        print("Drum rolling...")
                        time.sleep(2)
                        deadly_number = randint(1, 6)
                        print("Pulling trigger...")
                        time.sleep(2)
                        count = randint(1, 6)

                        if count == deadly_number:
                            print("BANG! You lost during the Forgiveness Challenge.")
                            print(f"Game Over! Your final score: {score}")
                            return dishonorable
                        else:
                            print(f"CLICK! You survived shot {i + 1}")

                    # After the loop ends, the player has survived both shots
                    print("Incredible bravery! You are forgiven!")
                    deserts = 0
                    return False
                else:
                    print("Execution it is... Goodbye, dishonorable one!")
                    return dishonorable
            
            else:
                print("Execution it is...")
                time.sleep(3)
                print("SQUAD!!!")
                time.sleep(1)
                print("AIM!!!")
                time.sleep(1)
                print("FIRE!!!!")
                print("You were executed for the unsportsmanlike behaviour of", reason)
                print(f"Your final score is: {score}")
                deserts = 0
                score = 0  # Reset score after execution
                return False


    print("You are not marked as Dishonorable. Play honorably!")
    return dishonorable


def dishonorable_game_loop(deadly_number, count):
    global score, dishonorable, deserts
    bullets_in_chamber = 2  # Player has 2 bullets in the chamber when dishonorable
    while True:
        print(f"\nYou have {bullets_in_chamber} bullets left.")
        print("Rolling the drum...")

        # Increment count and check for a bullet in the chamber
        count += 1
        if count == deadly_number:
            print("BANG! You are eliminated. Perhaps it would have been better to not be such a weak coward.")
            print(f"Game Over! Your final score: {score}")
            deserts = 0
            score = 0  # Reset score after death
            return "player", count, False  # End game if the player is eliminated
        else:
            print("CLICK! You survived this shot. Wonder how you did it.")
            bullets_in_chamber -= 1  # Reduce bullets left

            if bullets_in_chamber == 0:  # After 2 shots, the player must choose to desert or proceed
                print("You have 0 bullets left!")
                choice = input("Do you want to seek redemption or continue playing dishonorably? (Redeem/Continue): ").lower()

                if choice == "redeem":
                    print("Wise choice")
                    seek_forgiveness()
                elif choice == "continue":
                    print("You continue dishonorably... Be careful!")
                    bullets_in_chamber = 2  # Refill bullets
                else:
                    print("Invalid choice. No one survives when they hesitate.")
                    print(f"Game Over! Your final score: {score}")
                    score = 0
                    deserts = 0
                    return "player", count, False



def game():
    global score, dishonorable, deserts
    while True:
        answer = input("Would you like to play? (Yes/No): ").lower()
        if answer == "yes":
            score = 0  # Reset score for a new game
            deserts = 0
            game_on = True
            deadly_number = randint(1, 6)
            count = 0
            turn = "player" if randint(1, 2) == 1 else "computer"

            print("Inserting bullet...")
            time.sleep(2)
            print("Rolling the drum...")
            time.sleep(2)
            print("Spinning the gun...")
            time.sleep(2)

            while game_on:
                if turn == "player":
                    if dishonorable:  # Trigger dishonorable round if player is dishonorable
                        dishonorable_round(deadly_number, count)
                        game_on = False
                    else:
                        turn, count, game_on = player_turn(deadly_number, count)
                elif turn == "computer":
                    turn, count, game_on = computer_turn(deadly_number, count)

                # Handle the case where the player wins
                if not game_on and turn == "computer":
                    print("\nCongratulations! You won this round.")
                    play_again = input("Would you like to play another round? (Yes/No): ").lower()
                    if play_again == "yes":
                        deadly_number = randint(1, 6)  # Reset deadly_number for the new round
                        count = 0
                        print("Inserting bullet...")
                        time.sleep(2)
                        print("Rolling the drum...")
                        time.sleep(2)
                        print("Spinning the gun...")
                        time.sleep(2)
                        game_on = True
                    else:
                        print("Thanks for playing! Your final score is:", score)
                        break

            #if not game_on and turn == "player":  # Player loses
             #   print(f"Game over. Your final score is: {score}")
        elif answer == "no":
            print("Thanks for playing! Goodbye!")
            time.sleep(2)
            break
        else:
            print("Invalid input. Please type 'Yes' or 'No'.")



print("Let's play Russian roulette!")
print("There are 6 slots for a bullet, 1 is loaded. Try not to be shot by the bullet. Good Luck!")
game()
