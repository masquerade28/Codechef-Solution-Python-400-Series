'''
  There is a group of N friends who wish to enroll in a course together. 
  The course has a maximum capacity of M students that can register for it. 
  If there are K other students who have already enrolled in the course, determine if it will still be possible for all the N friends to do so or not.
'''

for t in range(int(input())):
  N,M,K = map(int, input().split())
  CourseRegistration = "YES" if M-K >= N else "NO"
  print(CourseRegistration)
