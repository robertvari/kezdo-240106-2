import os, random

MAX_NUMBER = 10
PLAYER_NAME = None
CREDITS = 10

def main():
    clear_screen()
    
    intro()

    game_loop()

def clear_screen():
    os.system("cls")
    # os.system("clear")

def intro():
    print("*"*50, "MAGIC NUMBER GAME", "*"*50)

    get_player_name()

    # Game rules
    print(f"Hello {PLAYER_NAME}! You have {CREDITS} credits to play.")
    print("If you can guess my number you win 10 credits, otherwise you loose 10 credits")
    print("I you have no more credits the game is over.")
    print(f"I have number between 1 and {MAX_NUMBER}. Can you guess it?")
    print("-"*50)

def get_player_name():
    global PLAYER_NAME
    PLAYER_NAME = input("What is your name?")

def game_loop():
    global CREDITS

    max_tries = 3

    # generate a random number
    magic_number = str(random.randint(1, MAX_NUMBER))
    print(f"DEBUG: {magic_number}")

    player_number = input("What is your guess?")

    while magic_number != player_number:
        max_tries -= 1
        if max_tries == 0:
            clear_screen()
            print("You have no more tries :(")

            CREDITS -= 10
            print(f"You lose 10 credits. You have {CREDITS} credits left")

            ask_new_game()
        
        print(f"Wrong, try again. You have {max_tries} left.")
        player_number = input("What is my magic number?")

    clear_screen()
    print(f"You win {PLAYER_NAME}! {magic_number} was my number!!!")

    CREDITS += 10
    print(f"You get 10 credits. Now you have {CREDITS} credits")
    ask_new_game()

def ask_new_game():
    if CREDITS > 0:
        player_input = input("Do you want to play again? (y/n)")
        if player_input == "y":
            clear_screen()
            game_loop()
    else:
        clear_screen()
        print("You loose all your credits")
    
    print("Maybe next time :)")
    exit()

# start game
main()