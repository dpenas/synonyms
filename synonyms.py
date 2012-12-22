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
	htmlurl = urllib(url)
	auxFile = open('auxFile.txt', 'w')
	auxFile.write(htmlurl.read())
	htmlurl.close()
	auxFile.close()