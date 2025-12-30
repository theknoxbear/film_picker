import random
# Creating different genres for different moods
sci_fi = ["Metropolis", "Things to Come", "Forbidden Planet", "The Day the Earth Stood Still", "The War of the Worlds", "Solaris", "Close Encounters of the Third Kind", "Gattaca", "Contact", "Moon", "Children of Men", "After Yang", "The Vast of Night", "Marcel the Shell with Shoes on"]
mystery = ["Rear Window", "The Third Man", "Vertigo", "Chinatown", "Memento", "Tinker, Tailor, Soilder, Spy", "Prisoners",]
comedy = ["Some like it Hot", "The Apartment", "Hunt for the Wilderpeople", "The Philadelphia Story", "To Be or Not to Be","Young Frankenstein", "Office Space", "His Girl Friday", "Best in Show", "Metropolitan", "The Intern","Julie & Julia", "Modern Times", "PlayTime", "Mr. Hulot's Holiday"]
dramas = ["Manchester by the Sea", "Still Alice", "Ordinary People", "The Straight Story", "Paterson", "Little Women", "The Remains of the Day", "Brooklyn", "CODA","Tokyo Story"]
animated = ["Whisper of the Heart", "The Wind Rises", "The Red Turtle", "Persepolis", "Ernest & Celestine"]
documentary = ["Jiro Dreams of Sushi", "Won't You Be My Neighbor?", "Faces Places", "Rivers and Tides","Stories We Tell"]

#Ask the user for their choice of genre
print("What are you in the mood for? (sci_fi, mystery, comedy, dramas, animated, documentary)")
choice = input("> ").lower() #lower makes this code work even if we use lower case letters

# Logic block - notice how all 'if', 'elif', and 'else' line up vertically
if choice == "sci_fi":
    selection = random.choice(sci_fi)
    print("The film we are watching tonight is: " + selection)

elif choice == "mystery":
    selection = random.choice(mystery)
    print("The film we are watching tonight is: " + selection)

elif choice == "comedy":
    selection = random.choice(comedy)
    print("The film we are watching tonight is: " + selection)

elif choice == "dramas":
    selection = random.choice(dramas)
    print("The film we are watching tonight is: " + selection)

elif choice == "animated":
    selection = random.choice(animated)
    print("The film we are watching tonight is: " + selection)

elif choice == "documentary":
    selection = random.choice(documentary)
    print("The film we are watching tonight is: " + selection)

elif choice == "surprise me" or choice == "surprise":
    # We add all the lists together into one big list
    all_films = sci_fi + mystery + comedy + dramas + animated + documentary
    selection = random.choice(all_films)
    print("The universe has spoken! You are watching: " + selection)

else:
    print("Oops! I didn't recognise that genre. Please check your spelling and try again.")

