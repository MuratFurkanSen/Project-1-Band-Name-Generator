print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tipPercent = float(input("What percentage tip would you like to give? 10,12 or 15?"))
people = int(input("How many people to split the bill ?"))

pay = (bill + (bill *tipPercent/100))/people
print(f"Each person should pay ${pay:.2f}")