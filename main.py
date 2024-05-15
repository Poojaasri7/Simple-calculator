from replit import clear

from art import logo


def add(n1 , n2):
  return n1 + n2

def sub(n1, n2):
  return n1 - n2

def mul(n1, n2):
  return n1 * n2

def div(n1, n2):
  return n1 / n2

def exp(n1, n2):
  return n1 ** n2


dic ={
  "+" : add,
  "-" : sub,
  "*" : mul,
  "/" : div,
  "**" : exp
}

class color:
  magenta = "\u001b[35m"
  end = "\u001b[0m"
print(color.magenta + logo + color.end)

def calculator():
  try:
    num1 = float(input("What's the first number: "))
  except ValueError:
    print("Error, number = 0")
    num1 = 0
  for i in dic:
    print(i)
  loop = False
  while not loop:
    op = input("Pick an opertion: ")
    while op not in dic:
      print("Error, Try again!")
      op = input("Pick an operation: ")
      
    try:
      num2 = float(input("What's the next number?: "))
    except ValueError:
      print("Error, number = 0")
      num2 = 0
    if op == "/":
      if num2 == 0:
        print("Infinity")
        user = input(f"Type 'y' to continue calculating with {num1}, or type 'n' to start a new calculation: ")
        if user == "n":
          loop = True
          calculator()
    else:
      function = dic[op]
      result = function(num1, num2)
      print(f"{num1} {op} {num2} = {result}")
      user = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
      if user == "y":
        num1 = result
      else:
        loop = True
        clear()
        calculator()

calculator()


    
    


  
    



