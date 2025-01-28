#dont repeat yourself

winning_number = 43
guess = 1
number = int(input("guess a number between 1 and 100: "))
game_over = False

while True:
    if number == winning_number:
        print(f"you win, and you guessed this number in {guess} times ")
        break
    else:
        if number < winning_number:
            print("too low")

        else:
            print("to high")
            
        guess += 1
        number = int(input("guess again: "))
            
