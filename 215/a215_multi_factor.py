# a215_multi_factor.py
import tkinter as tk
import multifactorgui as mfg

# create a multi-factor interface to a restircted app
my_auth = mfg.MultiFactorAuth()

username:str
password:str
while True:
	try:
		username = input("Username:")
		password = input("Password:")
		assert username.isalnum() == True
		assert password.isalnum() == True
		assert password.isalpha() == False
		assert password.isdigit() == False
		assert len(password) > 7 and len(password) < 25
		break
	except AssertionError:
		print("Invalid Username or Password.\nUsernames and Passwords must contain alphanumeric characters only.\nPasswords must be 8-24 characters long and contain at least one number.")

my_auth.set_authorization(username, password)
# confirm authorization info
auth_info = my_auth.get_authorization()
print(auth_info)

# set the users authentication information
question = "What is your favorite color?"
answer = "purple"
my_auth.set_authentication(question, answer)

# start the GUI
my_auth.mainloop()