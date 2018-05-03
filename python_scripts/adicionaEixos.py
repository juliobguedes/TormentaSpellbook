# coding: utf-8
# (C) Júlio Barreto
# Modifica jsons para remover atributo de tendencia e adicionar atributo de eixo bondoso-maligno e eixo leal-caótico

import os
x = 10
allFiles = [i for i in os.listdir(os.getcwd()) if i.endswith(".json")]

for file in allFiles:
	archive = open(file, 'r')
	lines = archive.readlines()
	lines.pop(x)
	lines.insert(x, '"eixoBM":[], \n')
	lines.insert(x+1, '"eixoLC":[], \n')
	archive.close()
	text = "".join(lines)
	new = open(file,'w')
	new.write(text)
	new.close()
