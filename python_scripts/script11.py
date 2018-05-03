# coding: utf-8
# (C) Júlio Barreto
# Remove all urls and add new and correct urls

import os

allFiles = [i for i in os.listdir(os.getcwd()) if i.endswith(".json")]

for file in allFiles:
	archive = open(file, 'r')
	lines = archive.readlines()
	for i in range(len(lines)-1, 0, -1):
		if "url" in lines[i]:
			lines.pop(i)

	newfile = str(file)
	filename = newfile.replace("json", "markdown")

	lines.insert(len(lines)-2, '"url":"feats/'+filename+'", \n')

	path = "feats/"
	newSave = open(path+file, 'w')
	newSave.write("".join(lines))
	newSave.close()
