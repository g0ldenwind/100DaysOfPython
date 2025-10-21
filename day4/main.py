import random
rock=("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper=("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissors=("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")


while True:
    player_input=input('What do you choose? Type 0 for "rock", 1 for "paper", 2 for "scissors", or 3 to quit.\n')
    
    if player_input=="3":
        print("Thanks for playing! Goodbye!")
        break
    
    player=int(player_input)
    comp=random.randint(0,2)
    if player==0:
        print(rock)
        if comp==0:
            print("Computer chose:")
            print(rock)
            print("It's a draw")
        elif comp==1:
            print("Computer chose:")
            print(paper)
            print("You lose")
        else:
            print("Computer chose:")
            print(scissors)
            print("You win")
    elif player==1:
        print(paper)
        if comp==0:
            print("Computer chose:")
            print(rock)
            print("You win")
        elif comp==1:
            print("Computer chose:")
            print(paper)
            print("It's a draw")
        else:
            print("Computer chose:")
            print(scissors)
            print("You lose")
    elif player==2:
        print(scissors)
        if comp==0:
            print("Computer chose:")
            print(rock)
            print("You lose")
        elif comp==1:
            print("Computer chose:")
            print(paper)
            print("You win")
        else:
            print("Computer chose:")
            print(scissors)
            print("It's a draw")
    else:
        print("Invalid input! You lose.")
    
    print("\n" + "="*40 + "\n")
