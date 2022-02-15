"""
write a function to find the squares of numbers in a list?
      conditions: Ask user input how many numbers of squares are required
 ex : 
input: 5
output: 0, 1, 4, 9, 16

input: 2
output: 0, 1

1) You need to handle the exceptions
   To display helpful messages while exiting the programme

"""


def square_numbers(num):
    for x in range(num):
        i = x * x
        print(i)
"""
var = "0"
while var != "exit":
   var = input("Enter Value to display squares: ")

   if "sree" in number:
       break
   else:
       square_numbers(int(number))
   
   try:
      print("entered value "+ int(var))
      square_numbers(int(var))
   # except ValueError as ve:
   #    print("Guys you entered string {} where integer is required. My programme is not capable of conerting strings into integers.If you want to exit please type 'exit' ".format(var))

   except:
      print("You Entered {}. If you want to exit please type 'exit' ".format(var))
      pass
    """
try:
      var = input("Enter Value to display squares: ")
      print("entered value "+ var)
      square_numbers(int(var))
   # except ValueError:
   #   print("You entered {}. Please type 'exit' to exit the programme".format(var))
   #except TypeError:
   #   print("Got Type Error. You are trying to concatenate string with integer")
except Exception as exe:
       print("Error encountered. Error: {}".format(exe))
       # exit()
else: 
       print("I am happy. Bye Bye")
finally:
       print("I am happy with my code")
