import random

rock = '''
    _______
---'   ____)
      (_____)  
      (_____) (rock)
      (____)
---.__(___)
'''
paper = '''
    _______
---'    ____)____
           ______)
          _______) (paper)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________) (scissors)
      (____)
---.__(___)
'''
print("Welcome to Rock-Paper-Scissors game.")
print()
user = int(
    input(
        "enter your choice \nenter 1 for ROCK, 2 for PAPER and 3 for SCISSORS :"
    ))

object_list = [rock, paper, scissors]

if user == 1:
    user_choise = rock
elif user == 2:
    user_choise = paper
elif user == 3:
    user_choise = scissors
else:
    print("enter correct command!")

print()
print("Your choice:")
print(user_choise)

computer_choise = random.choice(object_list)
print("Computer choice")
print(computer_choise)
print()

if user_choise == computer_choise:
    print("Match tie 🤝")

if user_choise == rock and computer_choise == scissors:
    print("You're awesome 🤩, You won the game")
elif user_choise == scissors and computer_choise == rock:
    print("You lost! computer won 🤖 ")
elif user_choise == scissors and computer_choise == paper:
    print("You're awesome 🤩, You won the game!")
elif user_choise == paper and computer_choise == scissors:
    print("You lost! computer won 🤖")
elif user_choise == paper and computer_choise == rock:
    print("You're awesome 🤩, You won the game!")
elif user_choise == rock and computer_choise == paper:
    print("You lost! computer won 🤖")