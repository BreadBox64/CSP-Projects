# a213_pw_analyzer.py
import time
import pwalgorithms as pwa

password = input("Enter password:")

print("Analyzing a two-word password ...")
timeStart = time.time()

# attempt to find password
found, numGuesses = pwa.twoWord(password)
timeEnd = time.time()

# report results
if (found):
	print(password, "found in", numGuesses, "guesses")
else: 
	print(password, "NOT found in", numGuesses, "guesses!")
print("Time:", format((timeEnd-timeStart), ".8f"))