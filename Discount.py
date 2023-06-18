'''
  Alice buys a toy with a selling price of 100 rupees. 
  There is a discount of x percent on the toy. 
  Find the amount Alice needs to pay for it.
'''

# Running Loop For Test Cases
for t in range(int(input())): 
  
  # Taking Input For X = The Discount On The Toy
  X = int(input())
  
  # Final Price = 100 - X
  print(100-X)
