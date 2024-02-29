# Module pwalgorithms

# get words from password dictionary file
def getDictionary():
	words = []
	dictionaryFile = open("213/dictionary.txt")
	for line in dictionaryFile:
		# store word, omitting trailing new-line
		words.append(line[:-1])
	dictionaryFile.close()
	return words

# analyze a one-word password
def oneWord(password):
	words = getDictionary()
	guesses = 0
	# get each word from the dictionary file
	for w in words:
		guesses += 1
		if (w == password):
			return True, guesses
	return False, guesses

def twoWord(password):
	words = getDictionary()
	guesses = 0
	for firstWord in words:
		for secondWord in words:
			guesses += 1
			if(password == (firstWord + secondWord)):
				return True, guesses
	return False, guesses