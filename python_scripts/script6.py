# coding: utf-8
# (C) Júlio Barreto
# Define Spells Procedence (Arcane or Divine)

import os

def updateClasses(classes):
	classes = classes.replace(" ", "")
	classes = classes.replace('"', "")
	classes = classes.replace("[", "")
	classes = classes.replace("]", "")
	classes = classes.replace("classes:", "")
	return classes

def getProcedence(arr):
	lista = []
	if (arr.count("mago") > 0 or arr.count("feiticeiro") > 0):
		lista.append("Arcana")
	if (arr.count("clerigo") > 0 or arr.count("abencoado") > 0 or arr.count("druida") > 0 or arr.count("paladino") > 0 or arr.count("ranger") > 0):
		lista.append("Divina")
	return lista

def corrigeAspas(string):
	string = list(string)
	for i in range(len(string)):
		if (string[i] == "'"):
			string[i] = '"'
	string = "".join(string)
	return string

def addProcedence(lista):
	classes = lista[13]
	classes = updateClasses(classes)
	arcDiv = getProcedence(classes)
	arcDiv = corrigeAspas(str(arcDiv))
	lista.insert(4, ('"procedence":' + str(arcDiv) + ',\n'))

allFiles = [i for i in os.listdir(os.getcwd()) if i.endswith("json")]

for file in allFiles:
	archive = open(file, 'r')
	lista = archive.readlines()
	addProcedence(lista)
	saving = "".join(lista)
	path = "newJson/"
	save = open(path + file, 'w')
	save.write(saving)
	save.close()
