'''
  Chef has invented 1-minute Instant Noodles. As the name suggests, each packet takes exactly 1 minute to cook.
  Chef's restaurant has X stoves and only 1 packet can be cooked in a single stove at any minute.
  How many customers can Chef serve in Y minutes if each customer orders exactly 1 packet of noodles?
'''

# Taking Input For X = Number Of Stoves ; Y = Number Of Minutes
X,Y = map(int, input().split())

# Customers Chef Can Serve = Number Of Stoves * 1 Instant Noodles * Number Of Minutes
print(X*Y)
