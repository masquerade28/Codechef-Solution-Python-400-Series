'''
  Uttu broke his phone. 
  He can get it repaired by spending X rupees or he can buy a new phone by spending Y rupees. 
  Uttu wants to spend as little money as possible. 
  Find out if it is better to get the phone repaired or to buy a new phone.
'''

for i in range(int(input())):
  X,Y = map(int, input().split())
  
  if X>Y:
    print("NEW PHONE")
    
  elif X==Y:
    print("ANY")
    
  else:
    print("REPAIR")        
