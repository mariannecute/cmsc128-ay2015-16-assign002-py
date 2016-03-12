string1 = "AACCTT"
string2 = "GGCCTT"
thisString = "AATATATAGG"
subString = "ATA"
validateString = "ACGT"
strAlphabet = "ACGT"
genomeString = "GGCCAC"
n = 2

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

def getSkew(genomeString, n):
	countG = 0
	countC = 0
	if len(genomeString) >= n:
		for i in range(n):
			if genomeString[i] == "G":
				countG += 1
			elif genomeString[i] == "C":
				countC += 1
		skewness = countG - countC

	else:
		skewness = "Error! q should be greater than or equal to n"
	return skewness

skewness = getSkew(genomeString, n)
print("Skewness = " + str(skewness))
