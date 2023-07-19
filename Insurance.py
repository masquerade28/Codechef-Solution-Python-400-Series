'''
  Chef bought car insurance. The policy of the insurance is:
    -> The maximum rebatable amount for any damage is Rs X lakhs.
    -> If the amount required for repairing the damage is ≤ X lakhs, that amount is rebated in full.
  Chef's car meets an accident and required Rs Y lakhs for repairing.
  Determine the amount that will be rebated by the insurance company.
'''

for t in range(int(input())):
  X,Y = map(int, input().split())
  Insurance = X if Y>=X else Y
  print(Insurance)
