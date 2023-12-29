rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

Images = [rock, paper, scissors]
userChoice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
computerChoice = random.randint(0, 2)

print(Images[userChoice])
print("Computer chose:")
print(Images[computerChoice])
if not 0 <= userChoice <= 2:
    print('You typed an invalid number, you lose!.')
elif userChoice == computerChoice:
    print("It's a draw")
elif userChoice == 0 and computerChoice == 2:
    print("You win!")
elif userChoice > computerChoice:
    print("You win!")
else:
    print("You lose!")
