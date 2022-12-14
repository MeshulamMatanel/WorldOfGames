
# This program gets the name of the user and displays it with printed text
def welcome():
     name = input("Please enter yor name\n")
     print(f"Hellow {name} and welcome to the World of Games (WoG)"
           "\nHere you can find many cool games to play")


# welcome()


# This program gets the number of the game and displays it with printed text
def load_game():
    print("\nPlease choose a game to play:"
          "\n1. Memory Game - a sequence of numbers will appear for 1 second and you have toguess it back "
          "\n2. Guess Game - guess a number and see if you chose like the computer "
          "\n3. Currency Roulette - try and guess the value of a random amount of USD in ILS")
    global MemoryGame, GuessGame, CurrencyRoulette
    MemoryGame, GuessGame, CurrencyRoulette = "Memory Game", "Guess Game", "Currency Roulette"
    chsngame = input("Type the number of your choice:\n")
    if chsngame == "1":
        print(f"Your choice is {MemoryGame}")
    elif chsngame == "2":
        print(f"Your choice is {GuessGame}")
    elif chsngame == "3":
        print(f"Your choice is {CurrencyRoulette}")
    else:
        print("Wrong choice, try again..")
        load_game()


# This program gets the number of the difficulty and displays it with printed text
dfcltofgame = ""

def choose_diffculty():
    dfcltofgame = input("Please choose game difficulty from 1 to 5:\n")
    if dfcltofgame == "1":
        print(f"Your difficulty choice is {dfcltofgame}")
        return dfcltofgame
    elif dfcltofgame == "2":
        print(f"Your difficulty choice is {dfcltofgame}")
        return dfcltofgame
    elif dfcltofgame == "3":
        print(f"Your difficulty choice is {dfcltofgame}")
        return dfcltofgame
    elif dfcltofgame == "4":
        print(f"Your difficulty choice is {dfcltofgame}")
        return dfcltofgame
    elif dfcltofgame == "5":
        print(f"Your difficulty choice is {dfcltofgame}")
        return dfcltofgame
    else:
        print("Wrong choice, try again..")
        choose_diffculty()


dfcltyofgame = dfcltofgame






# load_game()
# choose_diffculty()
