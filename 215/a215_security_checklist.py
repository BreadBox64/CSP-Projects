##############################################################################
# a215_security_checklist.py
##############################################################################

print("Let's check your security. Answer y or n to each of the questions.")

yesOptions = ('y', 'Y', 'yes', 'Yes', 'YES')
noOptions = ('n', 'N', 'no', 'No', 'NO')

"""phish = input("Can you recognize phishing emails? ") in yesOptions
pw = input("Is your passord strong? ") in yesOptions
auth = input("Do you use multi-factor authentication? ") in yesOptions
enc = input("Do you know how to encrypt sensitive information? ") in yesOptions

if (phish and pw and auth and enc):
  print("You have good security habits.")
else:
  print("You can improve your security habits.")"""

phish = input("Can you recognize phishing emails? ") in noOptions
pw = input("Is your passord strong? ") in noOptions
auth = input("Do you use multi-factor authentication? ") in noOptions
enc = input("Do you know how to encrypt sensitive information? ") in noOptions

if (phish or pw or auth or enc):
	print("You can improve your security habits.")
else:
	print("You have good security habits.")