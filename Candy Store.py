'''
  Chef has started working at the candy store. 
  The store has 100 chocolates in total.
  Chef’s daily goal is to sell X chocolates. 
  For each chocolate sold, he will get 1 rupee. 
  However, if Chef exceeds his daily goal, he gets 2 rupees per chocolate for each extra chocolate.
  If Chef sells Y chocolates in a day, find the total amount he made.
'''

# Running Loop For Test Cases
for t in range(int(input())):

  # Taking Input For X = The Daily Goal Of Chef ; Y = The Number Of Chocolates He Actually Sells 
  X,Y = map(int, input().split())

  # Total Candy Sold = (1 Rupee * The Daily Goal Of Chef + 2 Rupee * For Extra Chocolates He Sell) If The Number Of Chocolates He Actually Sells Is Greater Than Equal To The Daily Goal Of Chef,  
    # Else No. Of Chocolate Sold = (1 * Y)
  CandyStore = (X+2*abs(X-Y)) if Y>=X else Y

  # Displaying Result
  print(CandyStore)
