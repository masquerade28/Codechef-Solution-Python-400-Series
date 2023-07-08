'''
  Chef is looking to buy a TV and has shortlisted two models. 
  The first one costs A rupees, while the second one costs B rupees.
  Since there is a huge sale coming up on Chefzon, Chef can get a flat discount of C rupees on the first TV, and a flat discount of D rupees on the second one.
  Help Chef determine which of the two TVs would be cheaper to buy during the sale.
'''

# Running Loop For Test Cases
for t in range(int(input())):

  # Taking Input For A = Marked Price Of First TV ; B = Marked Price Of Second TV ; A = Discount On First TV ; A = Discount On Second TV ;
  A,B,C,D = map(int, input().split())

  # If Final Price Of First TV Is Less Than Final Price Of Second TV, Then Chef Will Buy First TV
  if A-C < B-D:
    print("First")
  
  # If Final Price Of First TV Is Equal To Final Price Of Second TV, Then Chef Will Buy Any TV
  elif A-C == B-D:
    print("Any")

  # If Final Price Of First TV Is Greater Than Final Price Of Second TV, Then Chef Will Buy Second TV
  else:
    print("Second")
