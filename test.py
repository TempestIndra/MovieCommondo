import collections
import operator

x = "this is a test this is a a b aaa"

wordList = list(x.split(' '))

def findFrequency(wordList):
	wordFrequency = []

	for word in wordList:
		wordFrequency.append(wordList.count(word))

		wordFrequencyDictionary = {}

	for word in wordList:
		wordFrequencyDictionary.update(zip(wordList, wordFrequency))
		
	return sorted(wordFrequencyDictionary.items(), key = operator.itemgetter(1)))

y = findFrequency(wordList)
print(y)
print(sorted(y))

#print(collections.OrderedDict(y))

print(sorted(y.items(), key = operator.itemgetter(1)))