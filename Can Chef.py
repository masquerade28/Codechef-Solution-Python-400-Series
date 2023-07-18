'''
  Chef owns a car that can run 15 kilometers using 1 liter of petrol.
  He wants to attend a programming camp at DAIICT.
  X liters of petrol is present in Chef's car. 
  The distance between his house and DAIICT is Y kilometers.
  Determine whether Chef can attend the event and return to his home with the given amount of petrol.
'''

for t in range(int(input())):
  X,Y = map(int, input().split())
  CanChef = "YES"  if 2*Y <= X*15 else "NO"
  print(CanChef)
