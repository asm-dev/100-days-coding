from ASCII import whale

print(whale)

opt_1 = input("\n\n\nYou're coming back from the port, but you doubt whether to head northwest or northeast. (NW/NE) ").lower()
if opt_1 == "no":
  opt_2 = input("\nAs you're coming back from the port, you realise that the sky colours are changing. It's a beautifl sunset. Would you like to stay a little longer? (Y/N) ").lower()
  if opt_2 == "s":
    opt_3 = input("\nIt is a warm summer night, and almost reaching the port, calm after a wonderful sunset, from the bow, you consider the idea of ​​taking a bath. You have three options, ignore your wishes and return to port, impulsively take your clothes off and jump into the water without giving it much thought, or finish watching the sunset a little longer and jump into the water. Which option do you choose? (1/2/3/another) ").lower()
    if opt_3 == "1":
      print("\nGrumbling, you return to port, without having sighted any whales. Try again.")
    elif opt_3 == "2":
      print("\nYou jump into the water and enjoy being in the water so much, you are so amused swimming that you don't even realize that a whale is passing behind your boat. You come home without having seen the whale. Try again.")
    elif opt_3 == "3":
      print("\nWhile you watch the sun on the horizon, calmly, to the rhythm of the sun, you take your clothes off and get into the water. Already in the water, you realize that there are some strange waves around you. You swim and follow the waves, and as you go around the boat, suddenly, you see a gigantic jet of water, followed by a huge tail that, like the sun, goes into the water. It's a whale!")
    else:
      print("\nUnfortunately, you don't see any whales. However, you come back home happily. Try again to find the whale.")
  else:
    print("\nYou come back home safe and sound, after a marvellous sunset. However, you've missed the whale this time. Please try again.")
else:
  print("\nYou come back home safe and sound. Sadly, you've missed the whale. Please try again.")