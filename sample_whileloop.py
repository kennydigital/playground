
# Let's create some variables, string, some numbers, and a boolean
secret_word="fishy"
guess=""
guess_count=0
guess_limit=3
out_of_guesses= False

# Now let's create some repeating conditions to loop until conditions are met
while guess != secret_word and not(out_of_guesses):
    if(guess_count < guess_limit):
        guess=input("Enter secret word: ")
        guess_count+=1
    else:
        out_of_guesses=True

# Based on the result of the variables initialized within loop let's print a response
if out_of_guesses:
    print("You lose")
else:
    print("You win")
