# coding: utf-8
# (C) Júlio Barreto
# Corrigindo nome dos arquivos

import os

def fixFilename(text):
	text = text.lower()
	newText = ""
	for letter in text:
		if letter == " ":
			newText += "_"
		elif letter == "/":
			newText += "-"
		else:
			newText += letter

	return newText

def junta(lista):
	volta = ""
	for i in range(len(lista)):
		volta += lista[i]

	return volta

allFiles = [i for i in os.listdir(os.getcwd()) if i.endswith("markdown")]

for file in allFiles:
	print file

	archive = open(file, "r")
	
	lista = archive.readlines()

	texto = junta(lista)

	name = lista[2].split()
	name = " ".join(name[1:])
	name = name[1:-1]
	name = fixFilename(name)

	path = "posts/"

	save = open((path + name + ".markdown"), "w")
	save.write(texto)
	save.close()
