import os
from art import logo

print(logo)
print("Welcome to the secret auction program.")
otherBidders = "YES"
bidDict = dict()
while otherBidders == "YES":
    name = input("What is your name?: ")
    bid = input("What is your bid?: $")
    bidDict[bid] = name
    otherBidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").upper()
    os.system("cls")

winBid = max(bidDict.keys())
print(f"The winner is {bidDict[winBid]} with a bid of ${winBid}.")
input("\nPress any key to exit the program")
