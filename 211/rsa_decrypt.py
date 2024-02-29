#   a212_rsa_decrypt.py
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
print("Decrypted Message:", rsa.decrypt(key, modulus, plainText.split(", ")))
