'''
  Chef considers the climate HOT if the temperature is above 20, otherwise he considers it COLD. 
  You are given the temperature C, find whether the climate is HOT or COLD.
'''

# Running Loop For Test Cases
for t in range(int(input())):
  
  # Taking Input For C = The Temperature
  C = int(input())
  
  # If The Temperature Is Greater Than 20, It's HOT else It's COLD
  IsItHotOrCold = "HOT" if C > 20 else "COLD"
  
  # Displaying Result
  print(IsItHotOrCold)
