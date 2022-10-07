from functions import add_bid

bids = {}

# We give the option to add more one or more bid participants
more_bids = "Y"
while more_bids == "Y":
    add_bid(bids)
    more_bids= input("Are there more bids? (Y/N) ").upper()

# We gather data from the bids dictionary, creating one list for bidders and another for bifs
bids_list = list(bids.values())
bidders_list = list(bids.keys())

# We calculate the biggest bid
win_bid = max(bids_list)

# Based on the biggest bid's index, we compare bids and bidders lists and get the bid's winner
print(f"The winner is: {bidders_list[bids_list.index(win_bid)]}")

