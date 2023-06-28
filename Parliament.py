'''
  An important resolution is being discussed in the Parliament of Chefland. 
  There are N members present in the Parliament out of which X members voted in favour of the resolution and the remaining voted against it.
  According to the constitution of Chefland, a resolution is passed if and only if half or more than half the members present in the Parliament vote in favour of the resolution.
  Determine if the resolution is passed or not.
'''

# Running Loop For Test Cases
for t in range(int(input())):

  # Taking Input For N = Number Of Members In Parliament ; X = Members Who Voted In Favour Of The Resolution 
  N,X = map(int, input().split())

  # If Members Who Voted In Favour Of The Resolution Is Greater Than Or Equal To Half Of The Number Of Members In Parliament, ThenThe Resolution Will Be Passes Else it Will Not
  Parliament = "YES" if X >= N/2 else "NO"

  # Displaying Result
  print(Parliament)
