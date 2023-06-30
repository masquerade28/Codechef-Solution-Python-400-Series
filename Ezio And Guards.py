'''
  Ezio can manipulate at most X number of guards with the apple of eden.
  Given that there are Y number of guards, predict if he can safely manipulate all of them.
'''

# Running Loop For Test Cases
for t in range(int(input())):

  # Taking Input For X = No. Of Guards That Ezio Can Manipulate ; Y = Total No. Of Guards
  X,Y = map(int, input().split())

  # If No. Of Guards That Ezio Can Manipulate >= Total No. Of Guards, Then He Can Safely Manipulate All Of Them Else Not
  EzioAndGuards = 'YES' if X>=Y else 'NO'

  # Displaying Result
  print(EzioAndGuards)
