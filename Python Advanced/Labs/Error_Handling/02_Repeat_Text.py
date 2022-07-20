import sys
from io import StringIO

test_input1 = '''Hello
Bye
'''

test_input2 = '''Hello
2
'''

# sys.stdin = StringIO(test_input1)
sys.stdin = StringIO(test_input2)

text = input()

try:
    times = int(input())
    print(text * times)
except ValueError:
    print('Variable times must be an integer')







# try:
#  text = input()
#  times = int(input())
#  print(text * times)
# except ValueError:
#  print("Variable times must be an integer")




# try:
#  x = int("Peter")
# except ValueError:
#  print("Cannot convert str to int")
# finally:
#  print("Finally block")




# while True:
#  try:
#   x = int(input("Please enter a number: "))
#   break
#  except ValueError:
#   print("Oops! That was no valid number. Try again...")