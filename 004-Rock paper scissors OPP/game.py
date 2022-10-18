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
    pass

def get_user_play():
    """
    Asks the user what's their choice. It returns the user's choice
    """
    pass

def random_play():
    """
    Selects a random play in order to compete with the user's choice
    """
    pass

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