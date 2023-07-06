'''
  Eikooc loves bread. 
  She has N loaves of bread, all of which expire after exactly M days. 
  She can eat upto K loaves of bread in a day. 
  Can she eat all the loaves of bread before they expire?
'''

# Running Loop For Test Cases
for t in range(int(input())):

  # Taking Input For N = Total Number Of Loaves ; M = Days After Which Bread Expires ; K = Lovaes Of Bread She Can Eat In A Day
  N,M,K = map(int, input().split())

  # Number Of Days Required To Finish All Loaves = Total Number Of Loaves / Lovaes Of Bread She Can Eat In A Day ; Number Of Days Required To Finish All Loaves <= Days After Which Bread Expires, then She Can Eat All The Loaves Before They Expire.
  ExpiringBread = "YES" if (N/K) <= M else "NO"

  # Displaying Result
  print(ExpiringBread)
