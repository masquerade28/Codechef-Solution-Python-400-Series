'''
  Pooja would like to withdraw X $US from an ATM. 
  The cash machine will only accept the transaction if X is a multiple of 5, and Pooja's account balance has enough cash to perform the withdrawal transaction (including bank charges). 
  For each successful withdrawal the bank charges 0.50 $US.
  Calculate Pooja's account balance after an attempted transaction.
'''

# Taking Input For X = Amount Of Money She Wants To Withdraw ; Y = Her Initial Account Balance
X,Y = map(float, input().split())

# If The Money She Wants To Withdraw Is Not A Multiple Of 5 Or She Wants To Withdraw Money Greater Than Her Account's Balance, Then She Will Not Be Able To Withdraw Any
if X % 5 != 0 or X +0.5 > Y:
  print("{:.2f}".format(Y))

# Else After Withdrawing Money Her Balance Will Be = Y - X - 0.5(For Every Succesful Transaction)
else:
  print("{:.2f}".format(Y-X-0.5))
