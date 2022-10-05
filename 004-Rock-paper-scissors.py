import random

# Options converter - from numeric value to rock, paper or scissor
def converter(choice):
    if choice == 1:
        return "Rock"
    elif choice == 2:
        return "Paper"
    else:
        return "Scissors"

# Rock paper scissors comparator 
def comparator(choice_1, choice_2):
    if choice_1 == 1 and choice_2 == 3:
        return True
    elif choice_1 == 2 and choice_2 == 1:
        return True
    elif choice_1 == 3 and choice_2 == 2:
        return True
    return False

score = 0
play = True

while play:
    
    # We get the user's choice
    user_choice = input("\nRock, paper or scissors? Please type 1 to chose rock, 2 for paper and 3 for scissors. ")

    # We check that their user is either 1, 2 or 3
    while user_choice != "1" and user_choice != "2" and user_choice != "3":
        user_choice = input("Please choose 1, 2 or 3 depending on what your choice is. Please type 1 to chose rock, 2 for paper and 3 for scissors. ")

    # We transform the user's choice (str) into an integer and get the computers choice, which will be either 1, 2, or 3
    user_choice = int(user_choice)
    comp_choice = random.choice(range(1,4))

    # We show the choices to the user
    print(f"\nYour choice is: {converter(user_choice)} \nThe computer's choice is: {converter(comp_choice)}\n")
  
    # We compare the choices to determine who's won
    user_vs_comp = comparator (user_choice, comp_choice)
    comp_vs_user = comparator (comp_choice, user_choice)

    # We show the results and change and show the score 
    if user_vs_comp == True:
        print("You've won")
        score += 1
    elif comp_vs_user == True:
        print ("You've lost")
        score -= 1
    else:
        print("No one wins. Try again")

    print(f"Your score is: {score}")

    # We ask the user if they would like to play again. Every input but "N" o "n" will be taken as 'continue to play'.
    again = input("\nWould you like to play again? (Y/N) ").upper()
    if again == "N":
        play = False
    
