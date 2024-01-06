import random
from hangman_words import word_list
from hangman_art import stages, logo

word = list(random.choice(word_list))
display = ['_']*len(word)
gameEnd = False
playerWin = False
lives = 6
print(logo)
print("".join(display))

while not gameEnd:
    guess = input("Enter a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")
    elif guess in word:
        pass
    else:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
    for i in range(len(word)):
        if word[i] == guess:
            display[i] = word[i]
    if display == word:
        gameEnd, playerWin = True, True
    if lives == 0:
        gameEnd = True
    print("".join(display))
    print(stages[lives])


if playerWin:
    print("You won!")
else:
    print("You lost!")
    print("The word was: " + "".join(word))