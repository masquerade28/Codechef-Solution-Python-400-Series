'''
  Chef needs to park her car while she watches a movie. 
  The parking charges at the theater are as follows:
    -> Rs. X for the first 1 hour
    -> Rs. Y for every extra hour after the first hour
  If Chef parks her car for H hours, what is the total parking charges that she should pay?
'''

# Taking Input For X = Parking Cost For 1st Hour ; Y = Paking Cost For Every Extra Hour ; H = Hours For Chef Parked The Car 
X,Y,H = map(int, input().split())

# Money Chef Needs To Pay = Parking Cost For 1st Hour + Paking Cost For Every Extra Hour * (Hours For Chef Parked The Car - 1)
print(X+Y*(H-1))
