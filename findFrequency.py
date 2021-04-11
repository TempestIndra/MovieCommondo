import operator
# takes in list of words
# returns dictionary of words, frequency


def findFrequency(wordList):
    wordFreq = []
    wordFreqDict = {}

    # counts words, adds values to dictionary
    for word in wordList:
        wordFreq.append(wordList.count(word))
        wordFreqDict.update(zip(wordList, wordFreq))

    # sorts words alphabetically
    wordFreqDict = sorted(wordFreqDict.items(), key=operator.itemgetter(0))

    return wordFreqDict

# takes in list of lists containing string for movie script and movie title
# returns list consisting of movie title and then (word, frequency)


def combine(wordList, movieTitles):
    result = [list(''), list('')]
    for scripts, titles in zip(wordList, movieTitles):

        wordFreqDict = findFrequency(scripts)
        # wordFreqDict.insert(0, titles)
        result[0].append(titles)
        result[1].append(wordFreqDict)
    return result


# # testing
# list1 = "this is a list of words this is a list".split(' ')
# list2 = "this is another list of words".split(' ')
# testTitles = ["Black Panther", "Joker"]
# testScript = [list1, list2]
# z = combine(testScript, testTitles)

# print(z)
