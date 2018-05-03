# coding: utf-8
# (C) Júlio Barreto
# Remove duplicate lines

import os

allFiles = [i for i in os.listdir(os.getcwd()) if i.endswith(".json")]

for file in allFiles:
	archive = open(file, 'r')
	lines = archive.readlines()
	archive.close()
	
	for i in range(len(lines)-1, 0, -1):
		if lines[i] == lines[i-1]:
			lines.pop(i)

	txt = "".join(lines)
	path = "new/"
	arq = open(path+file, 'w')
	arq.write(txt)
	arq.close()
	
