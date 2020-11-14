#! python3
#pigLatin.py -- A pig lagin program
#Idea: Al sweigart
#program: Ayotunde Okunubi

description = """Pig Latin is a silly made-up language that alters English words.
If a word begins with a vowel, the word yay is added to the end of it.
If a word begins with a consonant or consonant cluster (like ch or gr),
that consonant or cluster is moved to the end of the word followed by ay."""

"""
Ayotunde in Pig Latin would be Ayotundeyay
John in Pig Latin would be ohnJay"""

import pprint

word = input("Please input your sentence/words")
word = word.lower()
wordList = word.split(' ')
vowels = ['a', 'e', 'i', 'o', 'u']

result = ''

for word in wordList:
    wordList = list(word)
    print(wordList)
    if wordList[0] in vowels:
        toMove = wordList[0]
        del wordList[0]
        wordList.append (toMove)
        wordList.append('yay')
        for item in wordList:
            result+=item
print (result)


#First Problem solved, solve the rest later
                
            
