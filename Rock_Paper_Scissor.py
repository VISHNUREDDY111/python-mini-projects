import random

print("Welcome to rock paper scissors game🎉🎊")
playing=True
valid_choices=('r','p','s')
d={'r':"Rock🪨",'p':"paper📃",'s':"Scissor✂️"}

while playing:
    your_choice=input("Rock, Paper, Scissors? (r/p/s):").lower()
    if your_choice not in valid_choices:
        print("Invalid choice!")

    else:
        computer_choice=random.choice(valid_choices)

        print(f"your_choice  :{d[your_choice]}\ncomputer choice:{d[computer_choice]}")

        if your_choice==computer_choice:
            print("Tie")
        elif your_choice=='r' and computer_choice=='s':
            print("Congratulations you won")
        elif your_choice=='s' and computer_choice=='p':
            print("Congratulations you won")
        elif your_choice=='p' and computer_choice=='r':
            print("Congratulations you won")
        else:
            print("you loss")
        

        playing=True if input("continue? (y/n)").lower()=='y' else print("Thanks for playing the game.")
            
