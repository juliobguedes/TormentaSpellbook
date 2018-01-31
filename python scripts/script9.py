# coding: utf-8
# (C) Júlio Barreto
# Summarize feats' types

import os

x = 13
every = set([])

allFiles = [i for i in os.listdir(os.getcwd()) if i.endswith(".json")]

for file in allFiles:
	archive = open(file, 'r')
	lines = archive.readlines()
	interest = lines[x]
	if not ("tipo" in interest):
		print file
	every.add(interest)
	
print every

