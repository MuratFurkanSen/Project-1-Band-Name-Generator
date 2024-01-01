from art import logo


def Caesar(plain_text, shiftAmount, dir):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    result = ""
    noLetters = len(alphabet)
    shiftAmount %= noLetters
    if dir == 'decode':
        shiftAmount *= -1

    for i in plain_text:
        if i in alphabet:
            result += alphabet[(alphabet.index(i) + shiftAmount + noLetters) % noLetters]
        else:
            result += i
    return result


print(logo)

runAgain = "YES"
while runAgain == "YES":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:")
    text = input("Type your message:").lower()
    shift = int(input("Type the shift number:"))

    cipher = Caesar(text, shift,direction)
    print(cipher)
    runAgain = input("Type 'yes' if you want to go again. Otherwise type 'no'.").upper()