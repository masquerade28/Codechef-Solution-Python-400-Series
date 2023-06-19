'''
  Chef has X 5 rupee coins and Y 10 rupee coins. 
  Chef goes to a shop to buy chocolates for Chefina where each chocolate costs Z rupees. 
  Find the maximum number of chocolates that Chef can buy for Chefina.
'''

# Running Loop For Test Cases
for t in range(int(input())):
  
  # Taking Input For X = Number Of 5 Rupee Coins ; Y = Number Of 10 Rupee Coins ; Z = Cost Of Each Chocolates
  X,Y,Z = map(int, input().split())
  
  # Number Of Chocolates That Chef Can Buy = Total Money // Cost Of Each Chocolate
  print(((X*5)+(Y*10))//Z)
