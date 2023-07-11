'''
  There are N bikes and M cars on the road.
    -> Each bike has 2 tyres.
    -> Each car has 4 tyres.
  Find the total number of tyres on the road.
'''

# Running Loop For Test Cases
for t in range(int(input())):

  # Taking Input For N = Number Of Bikes ; M = Number Of Cars
  N,M = map(int, input().split())

  # Total Number Of Tyres = 2 * Number Of Bikes + 4 * Number Of Cars
  print(2*N + 4*M)
