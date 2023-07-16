'''
  Most programmers will tell you that one of the ways to improve your performance in competitive programming is to practice a lot of problems.
  Our Chef took the above advice very seriously and decided to set a target for himself.
  Chef decides to solve at least 10 problems every week for 4 weeks.
  Given the number of problems he actually solved in each week over 4 weeks as P1, P2, P3, and P4, output the number of weeks in which Chef met his target.
 '''

P=[]
P = map(int, input().split())

count = 0

for i in P:
  
  if i>=10:
    
    count+=1 
  
print(count)
