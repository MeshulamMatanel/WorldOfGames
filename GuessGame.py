import Live

difficulty = Live.dfcltofgame

#This function will generate number between 1 to difficulty and save it to secret_number.
#def generate_number():



#This function will prompt the user for a number between 1 to difficulty and return the number.
def get_guess_from_user():
    global numberfromuser
    numberfromuser = input(f"Please type a number between 1 to {dfcltofgame}")
    print(f"\nYour number is: {numberfromuser}")



#This function will compare the secret generated number to the one prompted by the get_guess_from_user.
def compare_results ():
    if numberfromuser == secret_number:
        print(f"Your choice {numberfromuser} is correct!")
    else:
        print(f"Your choice {numberfromuser} is incorrect..")



#This function will call the functions above and play the game. Will return True / False if the user lost or won.
#def play():

print(difficulty)