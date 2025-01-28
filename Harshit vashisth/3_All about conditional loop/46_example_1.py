# EXERCISE , NUMBER GUESSING GAME
# Make a variable, like winning_number and assign any number to it.
# Ask user to guess a number.
# if user guessed correctly then print "YOU WIN !!!!"
# if user didn't guessed correctly then :
    # if user guessed lower than actual number then print "too low"
    # if user guessed higher than actual number then print "too high"

# google "how to generate random number in python" to generate random
# winning number

winning_number = 27
user_input = input("Gess the number between 1 and 100: ")
user_input = int(user_input)
if user_input == winning_number:
    print("you wan!!!!")
else:                       #nested if else
    if user_input < winning_number:
        print("to low")
    else:
        print("to high")
        