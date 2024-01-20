import os, random

MAX_NUMBER = 10
PLAYER_NAME = None

def main():
    clear_screen()
    
    get_player_name()

    clear_screen()
    
    intro()

    game_loop()

def clear_screen():
    os.system("cls")
    # os.system("clear")

def intro():
    print("*"*50, "MAGIC NUMBER GAME", "*"*50)
    
    # Game rules
    print(f"Hello {PLAYER_NAME}! I have number between 1 and {MAX_NUMBER}. Can you guess it?")
    print("-"*50)

def get_player_name():
    global PLAYER_NAME
    PLAYER_NAME = input("What is your name?")

def game_loop():
    max_tries = 3

    # generate a random number
    magic_number = str(random.randint(1, MAX_NUMBER))
    player_number = input("What is your guess?")

    while magic_number != player_number:
        max_tries -= 1
        if max_tries == 0:
            print("Game Over :(")
            ask_new_game()
        
        print(f"Wrong, try again. You have {max_tries} left.")
        player_number = input("What is my magic number?")

    print(f"You win {PLAYER_NAME}! {magic_number} was my number!!!")
    ask_new_game()

def ask_new_game():
    clear_screen()
    player_input = input("Do you want to play again? (y/n)")

    if player_input == "y":
        clear_screen()
        game_loop()

    print("Maybe next time :)")
    exit()



# start game
main()