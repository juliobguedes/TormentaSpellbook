# coding: utf-8
# (C) Júlio Barreto
# Join all spells jsons in one big json

import os

def linesTogether(arr):
	strDone = ""
	for i in arr:
		strDone += i

	return strDone

allFiles = [i for i in os.listdir(os.getcwd()) if i.endswith("json")]
bigJson = '{"data":[\n'
for file in allFiles:
	archive = open(file, 'r')
	bigJson += linesTogether(archive.readlines()) + ", "

bigJson = bigJson[:-2]
bigJson += "]}"

save = open("feats.json", 'w')
save.write(bigJson)
save.close()
