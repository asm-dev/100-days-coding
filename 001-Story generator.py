import random

full_name = input("What's your name? ") + " " + input("and what's your last name? ")

print(f"\nHi there {full_name}, we're going to create a random name for your article. Your article's name is: ")

opt_start = ["Cuantitative analysis of", "Very important study about", "Synergies between"]
opt_middle = ["the surreal", "wild", "all the"]
opt_end = ["flowers", "tomatoes", "mitochondrial processes"]

def story_maker(start_list, middle_list, end_list, author):
    story = '"' + "\x1B[3m" + random.choice(start_list) + " " + random.choice(middle_list) + " " + random.choice(end_list) + "\x1B[0m" + '"'
    return print(f"\n{story} {author}")

again = True
while again:
    story_maker(opt_start, opt_middle, opt_end, full_name)
    if input("\nWould you want a new suggestion? (Y/N) ") != "Y":
        again = False