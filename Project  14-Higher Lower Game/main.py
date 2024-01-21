from art import logo, vs
from game_data import data
from random import randint
from time import sleep
from os import system


def play_game(A, B, score, isFirst):
    if A['follower_count'] > B['follower_count']: Answer = "A"
    else: Answer = "B"
    print(logo)
    if not isFirst: print(f"You're right! Current score is {score}.")
    print(f"Compare A: {A['name']} a {A['description']}, from {A['country']}.")
    print(vs)
    print(f"Compare B: {B['name']} a {B['description']}, from {B['country']}.")
    userAnswer = input("Who has more followers? Type 'A' or 'B': ").upper()
    system("cls")
    if userAnswer == Answer:
        score += 1
        if Answer == "A":
            play_game(A, data[randint(0, len(data))], score, False)
        else:
            play_game(B, data[randint(0, len(data))], score,False)
    else:
        print(f"Sorry, that's wrong. Final score {score}.")


play_game(data[randint(0, len(data))], data[randint(0, len(data))], 0, True)
input()
