'''
  Write a program to find the remainder when an integer A is divided by an integer B.
'''
# Taking Input For Number Of Test Cases
T = int(input())

# Making An Empty List For Inputs For Each Test Cases  
tests = []

# Running Loop To Append The Inputs Of Each Test Cases
for i in range(T):
  tests.append([int(i) for i in input().split()])

# Displaying Result Of The Test Cases 
for i in tests:

  # Remainder = Numerator % Denominator
  print(i[0]%i[1])
