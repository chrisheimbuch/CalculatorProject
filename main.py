from art import logo
print(logo)

#Addition Function
def add(n1, n2):
  return n1 + n2
  
#Subtraction Function
def subtract(n1, n2):
  return n1 - n2

#Multiplication Function
def multiply(n1, n2):
  return n1 * n2
  
#Division Function
def divide(n1, n2):
  return n1 / n2
  
operations = {
  "+":add, 
  "-":subtract, 
  "*":multiply, 
  "/":divide
}

def calculator():
  
  first_number = float(input("What's the first number?: "))
  
  for symbol in operations:
    print(symbol)
  should_continue = True
  
  while should_continue:
      operation_symbol = input("Pick another operation: ")
      second_number = float(input("What's the next number?: "))
      calculation_function = operations[operation_symbol]
      answer = calculation_function(first_number, second_number)
      
      print(f"{first_number} {operation_symbol} {second_number} = {answer}") 
  
      if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ") == "y":
        first_number = answer
      else:
        should_continue = False
        calculator()
        
calculator()