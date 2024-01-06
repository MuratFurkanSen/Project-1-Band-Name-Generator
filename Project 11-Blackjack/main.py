from art import logo
import random
import os

while True:
    GameStart = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    os.system("cls")
    if GameStart == 'n':
        break

    Cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    playerHand: list[int] = list()
    computerHand = list()
    player = random.randint
    # Creating Start Hands
    playerEnd = False
    playerHand.append(Cards[random.randint(0, len(Cards) - 1)])
    playerHand.append(Cards[random.randint(0, len(Cards) - 1)])
    computerHand.append(Cards[random.randint(0, len(Cards) - 1)])
    print(logo)
    while not playerEnd:

        print(f"\tYour cards: {playerHand}, current score: {sum(playerHand)}")
        print(f"\tComputer's first card: {computerHand[0]}")

        playerChoice = input("Type 'y' to get another card, type 'n' to pass: ")
        if playerChoice == 'y':
            playerHand.append(Cards[random.randint(0, len(Cards) - 1)])
        else:
            playerEnd = True
            break

        while sum(playerHand) > 21 and 11 in playerHand:
            playerHand[playerHand.index(11)] = 1

        if sum(playerHand) > 21:
            playerEnd = True

    while sum(computerHand) < 16:
        computerHand.append(Cards[random.randint(0, len(Cards) - 1)])
        while sum(computerHand) > 21 and 11 in computerHand:
            computerHand[computerHand.index(11)] = 1

    PlayerScore = sum(playerHand)
    ComputerScore = sum(computerHand)
    print(f"Your final hand: {playerHand}, final score: {PlayerScore}")
    print(f"Computer's final hand: {computerHand}, final score: {ComputerScore}")


    if PlayerScore > 21:
        print("You went over.You lose 😭")
    elif ComputerScore > 21:
        print("Opponent went over.You won")
    elif PlayerScore > ComputerScore:
        print("You won")
    elif PlayerScore < ComputerScore:
        print("Opponent won")
    else:
        print("Draw")