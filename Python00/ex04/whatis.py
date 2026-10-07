import sys

if len(sys.argv) < 2:
    sys.exit()
if (len(sys.argv) > 2):
    print("AssertionError: more than one argument is provided")
    sys.exit()

try:
    nbr = int(sys.argv[1])
except ValueError:
    print("AssertionError: argument is not an integer")
    sys.exit()

if (nbr % 2 == 0):
    print("I'm Even.")
elif (nbr % 2 != 0):
    print("I'm Odd.")


# Notes random
'''
import sys = module to access command line arguments 
sys.argv = list arg
sys.agrv[x] = access specific arg
len() = length of list
sys.exit() = exit program
try = attempt to run code that may raise an exception (like C++)
except = handle exception if raised (replace "catch" in C++)
ValueError = exception raised when a function receives an argument of the correct type but an inappropriate value
'''