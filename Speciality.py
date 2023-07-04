'''
  On every CodeChef user's profile page, the list of problems that they have set, tested, and written editorials for, is listed at the bottom.
  Given the number of problems in each of these 3 categories as X,Y, and Z respectively (where all three integers are distinct), find if the user has been most active as a Setter, Tester, or Editorialist.
'''

# Running Loop For Test Cases
for t in range(int(input())):

  # Taking  Input For X = No. Of Problems In Setter ; Y = No. Of Problems In Tester ; Z = No. Of Problems In Editorials
  X,Y,Z = map(int, input().split())

  # If No. Of Problems In Setter Is Greater Than No. Of Problems In Tester And No. Of Problems In Editorials, User Is Setter
  if X > Y and X > Z:
    print("Setter")

  # If No. Of Problems In Tester Is Greater Than No. Of Problems In Setter And No. Of Problems In Editorials, User Is Tester
  elif Y > X and Y > Z:
    print("Tester")

  # Else The User Is Editorialist
  else:
    print("Editorialist")
