from random import choice
from play import Paper, Rock, Scissors

def run_game():
    """
    Starts the game
    """
    display_game()
    user_play = get_user_play()
    comp_play = random_play()
    winner = get_winner(user_play, comp_play)
    
    if winner == None: # Tie, no one wins
        display_tie(user_play, comp_play)
    else:
        display_victory(winner)

def display_game():
    """
    Shows the game's name
    """
    print("Rock, Paper, Scissors")

def get_user_play():
    """
    Asks the user what their choice is and returns it
    """
    res = get_user_response()
    if res == 1:
        return Rock()
    elif res == 2:
        return Paper()
    else:
        return Scissors()

def get_user_response():
    """
    Asks the user what's their choice (it shows a range of options and asks the user to input their choice). 
    It returns the user's choice (str)
    """
    response = None
    while True:
        print(f"Choose your play:\n1. Rock\n2. PAper\n3. Scissors")
        raw = input("Enter 1, 2, or 3: ")
        raw = raw.strip()
        if raw == "1": # We dont use int() to avoid errors caused by big numbers, chars, etc.
            response = 1
            break
        elif raw == "2":
            response = 2
            break
        elif raw == "3":
            response = 3
            break
        else:
            continue
    return raw

def random_play():
    """
    Selects a random play in order to compete with the user's choice
    """
    return choice([Paper(), Rock(), Scissors()])

def get_winner(play1, play2):
    """
    Returns the winner or None if it's tie
    """
    pass

def display_tie(play1, play2):
    """
    Prints tie
    """
    pass

def display_victory(winner):
    """
    Displays the winnner
    """
    pass