'''
  Chef appeared for an exam consisting of 3 sections. 
  Each section is worth 100 marks.
  Chef scored A marks in Section 1, B marks in section 2, and C marks in section 3.
  Chef passes the exam if both of the following conditions satisfy:
    -> Total score of Chef is ≥100;
    -> Score of each section ≥10.
  Determine whether Chef passes the exam or not.
'''

# Taking Input For Number Of Test Cases
T = int(input())

# Making An Empty List For Inputs For Each Test Cases
test = []

# Making An Empty List For Inputs For Each Test Cases 
for t in range(T):
  test.append([int(t) for t in input().split()])

# Displaying Result Of The Test Cases 
for i in test:

  # Checking The Given Conditions To Find Out Whether Chef Is Pass Or Not
  PassTheExam = "PASS" if (i[0]+i[1]+i[2] >= 100) and i[0] >= 10 and i[1] >= 10 and i[2] >= 10 else "FAIL"
  print(PassTheExam)
