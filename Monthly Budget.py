'''
  Akshat has X rupees to spend in the current month. 
  His daily expenditure is Y rupees, i.e., he spends Y rupees each day.
  Given that the current month has 30 days, find out if Akshat has enough money to meet his daily expenditures for this month.
'''

for t in range(int(input())):
  
  X,Y = map(int, input().split())
  
  MonthlyBudget = "YES" if 30*Y <= X else "NO"
  
  print(MonthlyBudget)
