'''
  Chef has recently introduced a feature which allows you to open any user’s submitted code (not just your own), and ask an AI to explain that code in English. 
  For example, you can go to https://www.codechef.com/viewsolution/70530506 and click on "Analyse This Code".
  But there is a restriction that the feature works only on codes which are at most 1000 characters long. 
  Given the number of characters, C, in a particular code, output whether the feature is available on this code or not.
'''

# Taking Input For C = Number Of Characters
C = int(input())

# If C Is Less Than Equal To 1000 Character Then Ai Will Be Able To Analyse The Code Else Not
AIAnalysingCode = "YES" if C <= 1000 else "NO"

# Displaying Result
print(AIAnalysingCode)
