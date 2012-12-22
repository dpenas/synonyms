#!/usr/bin/env python
# coding: utf-8
import urllib 

def retrieve_information(word):
	'''
	Given a word, it returns the HTML page with the results
	'''
	API_KEY = "de96c"
	action = "/thesaurus/" #Looks for the synonym of the word
	url = "http://api.wordreference.com/" + API_KEY + action + word
	htmlurl = urllib.urlopen(url)
	auxFile = open('auxFile.txt', 'w')
	auxFile.write(htmlurl.read())
	htmlurl.close()
	auxFile.close()

def middle_word(sentence, first, second, lastWord):
	'''Given a sentence and two characters/words to look at, it returns
	the word in the middle'''
	try:
		beginning = sentence.index(first, lastWord) + len(first)
		ending = sentence.index(second, beginning)
		return (sentence[beginning:ending], ending)
	except ValueError:
		return ("", 0)

def finding_words():
	finalsynonyms = []
	lastWord = 0
	auxFile = open('auxFile.txt', 'r')
	midword = middle_word(auxFile.read(), 'title="">', '<', lastWord)
	while midword[0] != "":
		finalsynonyms.append(midword[0])
		lastWord = midword[1]
		print lastWord
		auxFile = open('auxFile.txt', 'r')
		midword = middle_word(auxFile.read(), 'title="">', '<', lastWord)
		print midword
	auxFile.close()
	return finalsynonyms

		