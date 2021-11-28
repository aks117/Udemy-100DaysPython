# Calculator Program

from art import logo

def add (n1, n2) :
  """Returns the sum of two numbers."""
  return n1 + n2

def subtract (n1, n2) :
  """Returns the difference of two numbers."""
  return n1 - n2

def multiply (n1, n2) :
  """Returns the product of two numbers."""
  return n1 * n2

def divide (n1, n2) :
  """Returns the division of two numbers."""
  return n1 / n2

def calculatorFn () :
  print (logo)
  should_continue = True
  n1 = float(input("Enter First number : \n"))

  while should_continue :

    operator = input("Enter the opertion you want to perform : (+ or - or * or /)\n")
    n2 = float(input("Enter next number : \n"))
    
    calculator = {
      "+" :  add(n1, n2), 
      "-" : subtract(n1, n2), 
      "*" : multiply(n1, n2), 
      "/" : divide(n1,n2),
      }

    answer = calculator[operator]

    print(f"{n1} {operator} {n2} = {answer}")

    choice = input("Want to continue with this calculation ? ( Yes / No / Close)\n").lower()

    if (choice == "yes") :
      n1 = answer
    elif choice == "close" :
      should_continue = False
    else :
      should_continue = False
      calculatorFn()

if __name__ == "__main__" :
  calculatorFn()
