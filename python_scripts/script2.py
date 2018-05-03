# coding: utf-8
# (C) Júlio Barreto
# Script de conversao das magias em markdown para json
# version 1.0.0

import os

procedences = ["Arcana", "Divina"]
levels = ["level0", "level1", "level2", "level3", "level4", "level5", "level6", "level7", "level8", "level9"]
descriptions = ["Abjuracao", "acido", "Adivinhacao", "agua", "Ar", "Caos", "Cura", "Eletricidade", "Encantamento", "Escuridao", "Essencia", "Fogo", "Frio", "Sonico", "Terra","Bem", "Mal", "Ordem", "Luz", "Ilusao", "Invocacao", "Medo", "Necromancia", "Tempo", "Transmutacao"]
executionTimes = ["livre", "movimento", "padrao", "completa", "concentracao", "rodadas"]
ranges = ["pessoal","toque", "metros", "ilimitada"]
effects = ["criatura", "objeto", "cilindro", "cone", "esfera", "linha", "explosao", "dispersao", "emanacao", "raio", "outros"]
durations = ["instantanea", "concentracao", "permanente", "descarregar"]
resTests = ["fortitude", "reflexos", "vontade"]
resTypes = ["anula", "parcial", "metade", "nenhum"]
ingredients = ["componente material", "experiência"]
gods = ["Allihanna", "Azgher", "Hynnin", "Kallyandranoch", "Keenn", "Khalmyr", "Lena", "Lin-Wu", "Marah", "Megalokk", "Nimb", "Oceano", "Ragnar", "Sszzas", "Tanna-Toh", "Tauron", "Tenebra", "Thyatis", "Valkária", "Wynna"]
classes = ["Abencoado", "Bardo", "Clerigo", "Druida", "Feiticeiro", "Mago", "Paladino", "Ranger"]

def fixFilename(text):
	text = text.lower()
	newText = ""
	for letter in text:
		if letter in "áàãâ":
			newText += "a"
		elif letter in "éê":
			newText += "e"
		elif letter in "íìî":
			newText += "i"
		elif letter in "óòõô":
			newText += "o"
		elif letter in "úùû":
			newText += "u"
		elif letter in "ç":
			newText += "c"
		elif letter == " ":
			newText += "_"
		elif letter == "/":
			newText += "-"
		else:
			newText += letter

	return newText

def setAttributes(arr1, arr2):
	attributes = []
	for i in arr1:
		for j in arr2:
			if compare(i,j):
				addOn(attributes, i.lower())
				
	return attributes
				
def addOn(arr, element):
	if element not in arr:
		arr.append(element)
		
def compare(obj1, obj2):
	obj1 = obj1.lower()
	obj2 = obj2.lower()
	
	return obj1 == obj2
	
def arrToString(lista):

	if len(lista) == 0:
		return "[]"

	string = "["
	for i in lista:
		string += '"' + i + '"'
		if i == lista[-1]:
			string += "]"
		else:
			string += ", "
			
	return string
	
def transformation(lista):

	name = lista[2].split()
	name = " ".join(name[1:])

	date = lista[3].split()
	date = date[1]

	source = lista[4].split()
	source = " ".join(source[1:])

	tags = lista[5].split()
	tags = " ".join(tags[1:])
	tags = tags[1:(len(tags)-1)].split(", ")

	level = setAttributes(tags, levels)
	description = setAttributes(tags, descriptions)
	executionTime = setAttributes(tags, executionTimes)
	range = setAttributes(tags, ranges)
	effect = setAttributes(tags, effects)
	duration = setAttributes(tags, durations)
	restTest = setAttributes(tags, resTests)
	resType = setAttributes(tags, resTypes)
	god = setAttributes(tags, gods)
	classe = setAttributes(tags, classes)

	json = '{\n"name":' + name + ', \n'
	json += '"date":"' + date + '", \n'
	json += '"source":"' + source + '", \n'
	json += '"level":' + arrToString(level) + ", \n"
	json += '"descriptions":' + arrToString(description) + ", \n"
	json += '"executionTimes":' + arrToString(executionTime) + ", \n"
	json += '"ranges":' + arrToString(range) + ", \n"
	json += '"effects":' + arrToString(effect) + ", \n"
	json += '"durations":' + arrToString(duration) + ", \n"
	json += '"restTests":' + arrToString(restTest) + ", \n"
	json += '"resTypes":' + arrToString(resType) + ", \n"
	json += '"gods":' + arrToString(god) + ", \n"
	json += '"classes":' + arrToString(classe) + "\n}"

	name = name[1:-1]
	path = "jsonSpells/"

	name = fixFilename(name)

	save = open((path + name + ".json"), "w")
	save.write(json)
	save.close()

allFiles = [i for i in os.listdir(os.getcwd()) if i.endswith("markdown")]

for file in allFiles:
	print file

	archive = open(file, "r")
	archiveFields = archive.readlines()
	transformation(archiveFields)

