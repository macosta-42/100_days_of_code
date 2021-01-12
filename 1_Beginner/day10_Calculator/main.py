# Calculator
from art import logo
from tools import clear

clear()
print(logo)

#Add
def add(n1, n2):
  return n1 + n2

#Substract
def substract(n1, n2):
  return n1 - n2

#Multiply
def multiply(n1, n2):
  return n1 * n2

#Divide
def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": substract,
  "*": multiply,
  "/": divide,
}

num1 = float(input("What's the first number?: "))
for symbol in operations:
  print(symbol)

end_game = False
while end_game == False:
  operation_symbol = input("Pick an operation: ")
  num2 = float(input("What's the next number?: "))
  calculation_function = operations[operation_symbol]
  answer = calculation_function(num1, num2)
  
  print(f"{num1} {operation_symbol} {num2} = {answer}")

  again = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ")
  if again == 'n':
    end_game = True
    clear()
  elif again == 'y':
    num1 = answer

