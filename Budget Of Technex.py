'''
The budget of Technex'23 is R thousand rupees. 
Since ICM is their flagship event, they will allocate at least half of their budget to it.
There are 5 other events planned under Technex'23.
The team wants to distribute the remaining amount equally among these.
Find the maximum amount in rupees that could be allocated to each of the other five events.
'''

for i in range(int(input())):
  R = int(input())
  print(int(((R*1000)/2)/5))
