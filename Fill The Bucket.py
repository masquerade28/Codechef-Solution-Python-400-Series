'''
  Chef has a bucket having a capacity of K liters. 
  It is already filled with X liters of water.
  Find the maximum amount of extra water in liters that Chef can fill in the bucket without overflowing.
'''

# Running Loop For Test Cases
for t in range(int(input())):

  # Taking Input For K = Capacity Of The Bucket ; X = Water In The Bucket
  K,X = map(int, input().split())

  # If Capacity Of The Bucket = Water In The Bucket, No More Water Can Be Added Else K - X Amount Of Water Can Be Added To The Bucket
  FillTheBucket = K-X if K>X else 0

  # Displaying Result
  print(FillTheBucket)
