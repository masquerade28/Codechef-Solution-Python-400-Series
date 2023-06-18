'''
  Chef's current rating is X, and he wants to improve it. 
  It is generally recommended that a person with rating X should solve problems whose difficulty lies in the range [X,X+200], i.e, problems whose difficulty is at least X and at most X+200.
  You find out that Chef is currently solving problems with a difficulty of Y.
  Is Chef following the recommended practice or not ?
'''

# Running Loop For Test Cases
for t in range(int(input())):
  
  # Taking Input For X = Chef's Current Rating ; Y = Difficulty Of Problems Chef Is Solving
  X,Y = map(int, input().split())
  
  # If Y Is Greater Than Or Equal To X And Less Than Equal To X + 200 ; Chef Is Following The Recommended Practice 
  RatingImprovement = "YES" if Y>=X and Y<=X+200 else "NO"
  
  # Displaying Result
  print(RatingImprovement)
