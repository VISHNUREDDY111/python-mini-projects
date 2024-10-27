import random
guess_number=random.randint(1,100)
while True:
    try:
        player_number=int(input("Guess the number between 1 and 100:"))
        if guess_number==player_number:
            print("Congratulations! You guessed the number.")
            break
        elif guess_number>player_number:
            print("too Low!!")
        else:
            print("Too High")
    except ValueError:
        print("please enter a valid number")

 