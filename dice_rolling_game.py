import random

while True:
    choice=input('Rollthe dice? (y/n):').lower()
    if choice=='y':
        dice1=random.randint(1,6)
        dice2=random.randint(1,6)
        print(f"({dice1},{dice2})")
    elif choice=='n':
        print("Thanks for playing the game!")
        break
    else:
        print("Invalid option!")