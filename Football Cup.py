'''
  It is the final day of La Liga. 
  Chef has a certain criteria for assessing football matches.
  In particular, he only likes a match if:
    -> The match ends in a draw, and 
    -> At least one goal has been scored by either team.
Given the goals scored by both the teams as X and Y respectively, determine whether Chef will like the match or not.
'''

# Running Loop For Test Cases
for t in range(int(input())):

  # Taking Input For X & Y = Goal Scored By Each Team
  X,Y = map(int, input().split())

  # If Match Draws And Atleast One Goal Is Scored By Either Team, Chef Will Like The Game Else He Will Not
  FootballCup = "YES" if X==Y and X !=0 and Y !=0 else "NO"

  # Displaying Result
  print(FootballCup)
