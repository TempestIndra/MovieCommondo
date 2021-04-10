import operator

def findFrequency(wordList):
	wordFrequency = []
	wordFrequencyDictionary = {}

	for word in wordList:
		wordFrequency.append(wordList.count(word))
		wordFrequencyDictionary.update(zip(wordList, wordFrequency))
		
	wordFrequencyDictionary = sorted(wordFrequencyDictionary.items(), key = operator.itemgetter(0))
	
	return wordFrequencyDictionary

def main(wordList, movieTitles):
	result = {}
	for scripts, titles in zip(wordList, movieTitles):
		
		y = findFrequency(scripts)
		print(y)
		print(titles)
	return result	


list1 = "this is a list of words this is a list".split(' ')
list2 = "this is another list of words".split(' ')
testTitles = ["Black Panther", "Joker", "Avengers"]
testScript = [list1, list2]
z = list(main(testScript, testTitles))

for thing in z:
	print(list(thing))