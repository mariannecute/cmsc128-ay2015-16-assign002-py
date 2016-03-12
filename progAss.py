string1 = "AACCTT"
string2 = "GGCCTT"
thisString = "AATATATAGG"
subString = "ATA"
validateString = "ACGT"
strAlphabet = "ACGT"

def getHammingDistance(string1, string2):
	hammingDistance = 0
	if len(string1) == len(string2):
		for i in range(len(string1)):
			if string1[i] != string2[i]:
				hammingDistance += 1
		return hammingDistance
	else:
		return "Error! Strings are not equal!"

hammingDistance = getHammingDistance(string1, string2)
print ("Hamming Distance = " + str(hammingDistance))

def countSubstrPattern(thisString, subString):
	substrPattern = 0
	substrLen = len(subString)
	for i in range(len(thisString)):
		if thisString[i:(i + substrLen)] == subString:
			substrPattern += 1

	return substrPattern

substrPattern = countSubstrPattern(thisString, subString)
print ("Total Substring Found = " + str(substrPattern))

def isValidString(validateString, strAlphabet):
	valid = 1
	count = 0
	for i in validateString:
		for j in strAlphabet:
			if i == j:
				count += 1

	if count == len(validateString):
		return True
	else:
		return False

isValid = isValidString(validateString, strAlphabet)
print("String valid? " + str(isValid))
