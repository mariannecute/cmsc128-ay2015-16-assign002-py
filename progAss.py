"""
	Author: Marianne Louise L. Rivera
	Date Created: March 12, 2016
"""

#initialize values for test cases
string1 = "AACCTT"
string2 = "GGCCTT"
thisString = "AATATATAGG"
subString = "ATA"
validateString = "ACGT"
strAlphabet = "ACGT"
genomeString = "GGCCAC"
n = 2

#get Hamming Distance
def getHammingDistance(string1, string2):
	hammingDistance = 0
	if len(string1) == len(string2):	#if their length is equal
		for i in range(len(string1)):		#traverse string1
			if string1[i] != string2[i]:	#if the characters are not equal
				hammingDistance += 1
		return hammingDistance
	else:								#if their lngth is not equal
		return "Error! Strings are not equal!"

hammingDistance = getHammingDistance(string1, string2)
print ("Hamming Distance = " + str(hammingDistance))

#count Substring Pattern in a String
def countSubstrPattern(thisString, subString):
	substrPattern = 0
	substrLen = len(subString)
	for i in range(len(thisString)):		#traverse string
		if thisString[i:(i + substrLen)] == subString: #if the substring matches
			substrPattern += 1

	return substrPattern

substrPattern = countSubstrPattern(thisString, subString)
print ("Total Substring Found = " + str(substrPattern))

#checks if a string is valid given a string alphabet
def isValidString(validateString, strAlphabet):
	valid = 1
	count = 0
	for i in validateString:	#traverse string
		for j in strAlphabet:	#traverse string alphabet
			if i == j:			#if the character is found on the string alphabet
				count += 1

	if count == len(validateString):	#if all the characters are in the string alphabet
		return True
	else:
		return False

isValid = isValidString(validateString, strAlphabet)
print("String valid? " + str(isValid))

#get skewness (Gs - Cs)
def getSkew(genomeString, n):
	countG = 0
	countC = 0
	if len(genomeString) >= n:		#if q >= n
		for i in range(n):			#traverse substring
			if genomeString[i] == "G":		#if it encountered G
				countG += 1
			elif genomeString[i] == "C":	#if it encountered C
				countC += 1
		skewness = countG - countC

	else:			#if q < n
		skewness = "Error! q should be greater than or equal to n"
	return skewness

skewness = getSkew(genomeString, n)
print("Skewness = " + str(skewness))

#get maximum skewness
def getMaxSkew(genomeString, n):
	countG = 0
	countC = 0
	maxSkew = 0
	if len(genomeString) >= n:	#if q >= n
		for i in range(n):		#traverse substring
			if genomeString[i] == "G":	#if it encountered G
				countG += 1
			elif genomeString[i] == "C":	#if it encountered C
				countC += 1
			skewness = countG - countC	#compute skewness

			if skewness > maxSkew:		#if skewness > current max
				maxSkew = skewness

		return maxSkew

	else:		#if q < n
		skewness = "Error! q >= n"
	return skewness

maxSkew = getMaxSkew(genomeString, n)
print("Max Skewness = " + str(maxSkew))

#get minimum skewness
def getMinSkew(genomeString, n):
	countG = 0
	countC = 0
	minSkew = len(genomeString)
	if len(genomeString) >= n:	#if q >= n
		for i in range(n):
			if genomeString[i] == "G":	#if it encountered G
				countG += 1
			elif genomeString[i] == "C":	#if it encountered C
				countC += 1
			skewness = countG - countC	#compute skewness

			if skewness < minSkew:	#if skewness is < current min
				minSkew = skewness
				
		return minSkew

	else:		#if q < n
		skewness = "Error! q should be greater than or equal to n"
	return skewness

minSkew = getMinSkew(genomeString, n)
print("Min Skewness = " + str(minSkew))