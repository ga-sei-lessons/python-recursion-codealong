def recursive():
  return recursive()

# recursive function rules
# 1. have a base case which stops the recursion form happening
# 2. needs to change state and move towards the base case (recursive case)
# 3. invoke itself recursively

def compliment_machine(count = 0):
  # rule 1: base case
  if count == 4:
    print('ive given enough compliments today!')
    return

  # logic happens after base case
  print('welcome to the compliment machine! 👋')
  print('enter your name for an unsolicited compliment')
  name = input('>>')

  print(f'ive given {count} many  compliments today!')

  print(f'wow! {name}! That is such a beautiful name!')


  # rule 2: invoke itself recursively and move state towards base case
  return compliment_machine(count + 1) # rule 3

# compliment_machine() # first invocation will be zero

# replacing loops with recursion
def print_loop(end_num, current_num = 0):
  # for i in range(end_num):
  #   print(i)

  # base case
  if current_num == end_num: return

  # actual function logic
  print(current_num)

  # advance state towards the base case
  return print_loop(end_num, current_num + 1)

# print_loop(10)

# overried rucrsion limit
import sys
sys.setrecursionlimit(5000)

# print loop but more recursive
def print_loop_easy(end_num):
  # base case
  if end_num == 0: return

  print(end_num)

  return print_loop_easy(end_num - 1)

# print_loop_easy(6000)

# find the factorial of a supplied number recursively
def factorial(num, product = 1):
  # base case
  if num == 0: return product
  # recursive logic
  return factorial(num - 1, product * num)

# print(factorial(5))

# find the sum of all numbers up to supplied number
def sum_to(num):
  # base case
  if num < 0: return 0
  return num + sum_to(num - 1)

print(sum_to(101))