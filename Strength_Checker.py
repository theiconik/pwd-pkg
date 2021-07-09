
def printStrongNess(input_string):
	n = len(input_string)

	# Initializing necessary characters with false
	hasLower = False
	hasUpper = False
	hasDigit = False
	hasSpecialChar = False
	normalChars = "abcdefghijklmnopqrstu"
	"vwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 "
	
   # Checking necessary characters in string
	for i in range(n):
		if input_string[i].islower():
			hasLower = True
		if input_string[i].isupper():
			hasUpper = True
		if input_string[i].isdigit():
			hasDigit = True
		if input_string[i] not in normalChars:
			hasSpecialChar = True

	# Strength of password
	print("----------------------------------------------------------------")
	print("Strength of password:- ", end = "")
	if (hasLower and hasUpper and
		hasDigit and hasSpecialChar and n > 8):
		print("Strong")
		print("----------------------------------------------------------------\n")
		
	elif ((hasLower or hasUpper) and
		(hasDigit or hasSpecialChar) and n >= 8):
		print("Moderate")
		print("----------------------------------------------------------------\n")
	else:
		print("Weak")
		print("----------------------------------------------------------------\n")


