#   a212_rsa_encrypt.py
import rsa as rsa

key:int
modulus:int
while True:
	try:
		key = int(input("Enter the Encryption Key: "))
		assert key >= 0
		modulus = int(input("Enter the Modulus: "))
		assert modulus >= 0
		break
	except (ValueError, AssertionError):
		print("Invalid input, please only input positive, integer values.")
plainText = input("Enter a message to encrypt: ")
print("Encrypted Message:", rsa.encrypt(key, modulus, plainText))