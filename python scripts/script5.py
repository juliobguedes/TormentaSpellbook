# coding: utf-8
# (C) Júlio Barreto
# Corrigir layouts de posts em markdown

import os

def findQuotes(string):
	quotesIndex = 0
	while (True):
		if (string[quotesIndex] == '"'):
			quotesIndex += 1
			break
		quotesIndex += 1
	return quotesIndex	

def fixTitle(string):
	firstQuote = findQuotes(string)
	newString = string[firstQuote:-1]
	secondQuote = findQuotes(newString)
	newString = newString[:secondQuote-1]
	newString = "**Titulo**:" + newString + "\n"
	return newString

def correct(lines):
	title = lines[2]
	title = title.replace("title", "")
	title = fixTitle(title)
	lines[2] = title

	lines.pop(6)
	lines.pop(5)
	lines.pop(4)
	lines.pop(3)
	lines.pop(1)
	lines.pop(0)

allFiles = [i for i in os.listdir(os.getcwd()) if i.endswith("markdown")]

for file in allFiles:
	archive = open(file, 'r')
	lines = archive.readlines()
	correct(lines)
	toSave = "".join(lines)
	path = "spells/"
	save = open(path + file, 'w')
	save.write(toSave)
	save.close()
