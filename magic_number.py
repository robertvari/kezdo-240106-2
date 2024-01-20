import os

MAX_NUMBER = 10

# entry point
def main():
    clear_screen()
    intro()


def clear_screen():
    os.system("cls")
    # os.system("clear")

def intro():
    print("*"*50, "MAGIC NUMBER GAME", "*"*50)
    
    # Game rules
    print(f"I have number between 1 and {MAX_NUMBER}. Can you guess it?")
    print("-"*50)

def get_player_name():
    pass


# The Game Loop
def game():
    pass


# Ask for the player if he/she wants a new turn.
def ask_new_game():
    pass



# start game
main()