#!/usr/bin/env python
# coding: utf-8

import urllib
import os

def retrieve_information(word):
	'''
	Given a word, it returns the HTML page with the results
	'''
	API_KEY = "de96c"
	action = "/thesaurus/" #Looks for the synonym of the word
	url = "http://api.wordreference.com/" + API_KEY + action + word
	htmlurl = urllib.urlopen(url)
	try:
		auxFile = open('auxFile.txt', 'w')
	except:
		print "Not able to create the auxFile to save the results"
		raise

	auxFile.write(htmlurl.read())
	htmlurl.close()
	auxFile.close()

def middle_word(sentence, first, second, lastWord):
	'''
	Given a sentence and two characters/words to look at, it returns
	the word in the middle
	'''
	try:
		beginning = sentence.index(first, lastWord) + len(first)
		ending = sentence.index(second, beginning)
		return (sentence[beginning:ending], ending)
	except ValueError:
		return ("", 0)

def finding_words():
	'''
	Opens the file and finds the synonyms of the given word
	'''
	finalsynonyms = []
	lastWord = 0
	try:
		auxFile = open('auxFile.txt', 'r')
	except:
		print "Not able to open auxFile (did you delete it?)"
		raise
	midword = middle_word(auxFile.read(), 'title="">', '<', lastWord)
	while midword[0] != "":
		finalsynonyms.append(midword[0])
		lastWord = midword[1]
		try:
			auxFile = open('auxFile.txt', 'r')
		except:
			print "Not able to open auxFile (did you delete it?)"
			raise
		midword = middle_word(auxFile.read(), 'title="">', '<', lastWord)
	try:
		os.remove("auxFile.txt")
	except:
		print "Not able to delete the file (did you delete it?)"
		raise
	return finalsynonyms

def find_synonyms(word):
	''' 
	Use this function to get the synonyms of the word you want 
	'''
	retrieve_information(word)
	synonyms = finding_words()
	return synonyms