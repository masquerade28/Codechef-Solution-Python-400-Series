'''
  You're given an integer N. Write a program to calculate the sum of all the digits of N.
'''

a = int(input(''))

for i in range(a):
  
  b = int(input(''))
  
  c = 0
  
  d = 0
  
  while b != 0:
    
    c = b % 10
    
    d = d + c
    
    b = b // 10
    
  print(d)
