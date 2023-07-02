'''
  Given A,B, and C as the sides of a triangle, find whether the triangle is scalene.
  Note:
    -> A triangle is said to be scalene if all three sides of the triangle are distinct.
    -> It is guaranteed that the sides represent a valid triangle.
'''

# Running Loop For Test Cases
for t in range(int(input())):

  # Taking Input For A, B & C i.e; The Three Sides Of The Triangle
  A,B,C = map(int, input().split())

  # If Side A Is Not Equal To Side B And Side B Is Not Equal To Side C And Side c Is Not Equal To Side a, It's A Scalene Triangle
  ScaleneTriangle = 'YES' if A != B and B!=C and C!=A else 'NO'

  # Displaying Result
  print(ScaleneTriangle)
