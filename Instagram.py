'''
  Chef categorises an instagram account as spam, if, the following count of the account is more than 10 times the count of followers.
  Given the following and follower count of an account as X and Y respectively, find whether it is a spam account.
'''

# Running Loop For Test Cases
for t in range(int(input())):
  
  # Taking Input For X = Following Count Of An Account ; Y = Follower Count Of An Account
  X,Y = map(int, input().split())
  
  # If X > 10 Times Of Y, It's A Spam Account
  Instagram = "YES" if X > 10*Y else "NO"
  
  # Displaying Result
  print(Instagram)
