'''
  Chef has opened a new airline. 
  Chef has 10 airplanes where each airplane has a capacity of X passengers.
  On the first day itself, Y people are willing to book a seat in any one of Chef's airplanes.
  Given that Chef charges Z rupees for each ticket, find the maximum amount he can earn on the first day.
'''

for i in range(int(input())):
  X,Y,Z = map(int, input().split())
  CodechefAirlines = 10*X*Z if Y>=X*10 else Y*Z
  print(CodechefAirlines)
