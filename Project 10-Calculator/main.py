import os
from art import logo


def add(a, b):
    return a+b


def subtract(a, b):
    return a-b


def multiply(a, b):
    return a*b


def divide(a, b):
    return a/b


def Calculator(hasAnswer, Answer):
    operations = {'+': add, '-': subtract, '*': multiply, '/': divide}
    if hasAnswer:
        firstNum = Answer
    else:
        print(logo)
        firstNum = float(input("What's the first number?: "))
        print(*operations.keys(), sep="\n")
    operation = input("Pick an operation: ")
    secondNum = float(input("What's the next number?: "))
    result = operations[operation](firstNum, secondNum)
    print(f"{firstNum} {operation} {secondNum} = {result}")
    Choice = input(f"Type 'y' to continue calculating with {result}, "
                   f"'n' to start a new calculation, "
                   f"'quit' to exit the calculator: ")
    if Choice == 'y':
        Calculator(True, result)
    elif Choice == 'n':
        os.system("cls")
        Calculator(False, result)


Calculator(False, 0)



