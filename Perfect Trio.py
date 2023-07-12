'''
Chef defines a group of three friends as a perfect group if the age of one person is equal to the sum of the age of remaining two people.
Given that, the ages of three people in a group are A,B, and C respectively, find whether the group is perfect.
'''

for t in range(int(input())):
  A,B,C = map(int, input().split())
  
  if A+B == C:
    print("YES")
    
  elif B+C == A:
    print("YES")
    
  elif A+C == B:
    print("YES")
    
  else:
    print("NO")
