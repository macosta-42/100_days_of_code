# Secret Auctions Program
from tools import clear
from art import logo

clear()
print(logo)
print("Welcome to the secret auction program.")

auctions = {}

def add_auction(name, bid):
  auctions[name] = bid

end_auctions = False
while end_auctions == False:
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: $"))
  
  add_auction(name, bid)

  again = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  clear()
  if again == "no":
    end_auctions = True

winner = max(auctions)
best_bid = auctions[winner]

print(f"The winner is {winner} with a bid of ${best_bid}")
