'''
  Chef recently started selling a special fruit.
  He has been selling the fruit for X rupees (X is a multiple of 100). 
  He earns a profit of Y rupees on selling the fruit currently.
  Chef decided to increase the selling price by 10%. 
  Please help him calculate his new profit after the increase in selling price.
  Note that only the selling price has been increased and the buying price is same.
'''

# Running Loop For Test Cases
for t in range(int(input())):

  # Taking Input For X = Initial Selling Price ; Y = Profit Earned
  X,Y = map(int, input().split())

  # If X Is Multiple Of 100 Then New Profit = (Initial Selling Price + 10% Of Initial Selling Price) - (Selling Price - Profit)
  ProfitIncrement = "Invalid Input" if X%100 != 0 else int((X+0.1*X)-(X-Y))

  # Displaying Result
  print(ProfitIncrement)
