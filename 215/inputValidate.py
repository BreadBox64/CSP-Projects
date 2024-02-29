def integer(s:str):
	try:
		assert s.isdigit() == True
		return True, s
	except (ValueError, AssertionError):
		return False, s
# str.alpha() returns True if all characters in the string are alphabetic (a–z or A–Z), and there is at least one character in the string.