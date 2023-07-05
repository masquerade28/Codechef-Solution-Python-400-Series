'''
  A participant can make 1 submission every 30 seconds. 
  If a contest lasts for X minutes, what is the maximum number of submissions that the participant can make during it?
  It is also given that the participant cannot make any submission in the last 5 seconds of the contest.
'''

# Running Loop For Test Cases
for t in range(int(input())):

  # Taking Input For X = Number Of MinutesFor Which Contest Lasts
  X = int(input())

  # Maximum Number Of Submissions = X In Seconds / 30 
  print(int((X*60)/30))
