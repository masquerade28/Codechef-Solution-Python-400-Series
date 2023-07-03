'''
  Chef is shopping for masks. 
  In the shop, he encounters 2 types of masks:
    -> Disposable Masks — cost X but last only 1 day.
    -> Cloth Masks — cost Y but last 10 days.
  Chef wants to buy masks to last him 100 days. 
  He will buy the masks which cost him the least. 
  In case there is a tie in terms of cost, Chef will be eco-friendly and choose the cloth masks. 
  Which type of mask will Chef choose?
'''

# Running Loop For Test Cases
for t in range(int(input())):
  
  # Taking Input For X = Cost Of Disposable Mask ; Y = Cost Of Cloth Mask
  X,Y = map(int, input().split())

  # If Total Cost Of Disposable Mask Is Less Than Total Cost Of Cloth Mask The Chef Will Buy Disposable Mask
  if 100*X < 10*Y:
    print("Disposable")

  # If Total Cost Of Disposable Mask Is Equal To The Total Cost Of Cloth Mask The Chef Will Buy Cloth Mask
  elif 100*X == 10*Y:
      print("Cloth")

  # If Total Cost Of Disposable Mask Is Greater Than Total Cost Of Cloth Mask The Chef Will Buy Cloth Mask
  else:
      print("Cloth")
