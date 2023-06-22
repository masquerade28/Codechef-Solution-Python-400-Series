'''
  Chef is watching TV. 
  The current volume of the TV is X. 
  Pressing the volume up button of the TV remote increases the volume by 1 while pressing the volume down button decreases the volume by 1. 
  Chef wants to change the volume from X to Y. 
  Find the minimum number of button presses required to do so.
'''

for t in range(int(input())):
  
  # Taking Input For X = Initial Volume Of The TV ; Y = Final Volume Of The TV 
  X,Y = map(int, input().split())
  
  # Minimum Number Of Button Presses Required = Absolute of ( Final Volume - Initial Volume )
  print(abs(Y-X))
