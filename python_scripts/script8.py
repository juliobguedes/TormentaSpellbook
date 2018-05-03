# coding: utf-8
# (C) Júlio Barreto
# Adding url to feats' JSONs

import os

allFiles = [i for i in os.listdir(os.getcwd()) if i.endswith(".json")]

for file in allFiles:
	archive = open(file, 'r')
	lines = archive.readlines()
	archive.close()
	txt = file[:-4]
	txt += "markdown"
	where = len(lines) -2
	lines.insert(where, '"url":"feats/' + txt + '",\n')
	save = open(file, 'w')
	save.write("".join(lines))
	save.close()
