# Tip Calculator
print("Welcome to the tip calculator.")
bill = input("What is the total bill? $")
tips = input("What percentage tip would you like to give? 10, 12 or 15? ")
people = input("how many people to split the bill? ")
percentage = "1." + tips
total_bill = float(bill) * float(percentage)
shares = round(total_bill / int(people), 2)
result = "{:.2f}".format(shares)
message = f"each person should pay: ${result}"
print(message)
