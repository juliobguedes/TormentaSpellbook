# coding: utf-8
# (C) Júlio Barreto
# Script para geração de markdown contendo os talentos de TormentaRPG

import os

def normaliza(string):
	string = list(string)
	for i in range(len(string)):
		if string[i] == " ":
			string[i] = "_"
		elif string[i] == "/":
			string[i] = "-"

	return "".join(string)

def correct(lista):
	if (len(lista) == 1 and lista[0] == ''):
		return str([])
	
	string = str(lista)
	string = list(string)
	for i in range(len(string)):
		if string[i] == "'":
			string[i] = '"'

	return "".join(string)

def evaluate(value):
	if (value != ""):
		return value
	return '-1'

def json(nome, mfor, mdes, mcon, mint, msab, mcar, mbba, mniv, deuses, eixoBM, eixoLC, tipo, livro):
	texto = "{\n"
	texto += '"nome":"' + str(nome) + '",\n'
	texto += '"forMin":' + evaluate(mfor) + ',\n'
	texto += '"desMin":' + evaluate(mdes) + ',\n'
	texto += '"conMin":' + evaluate(mcon) + ',\n'
	texto += '"intMin":' + evaluate(mint) + ',\n'
	texto += '"sabMin":' + evaluate(msab) + ',\n'
	texto += '"carMin":' + evaluate(mcar) + ',\n'
	texto += '"bbaMin":' + evaluate(mbba) + ',\n'
	texto += '"nivMin":' + evaluate(mniv) + ',\n'
	texto += '"deuses":' + correct(deuses) + ',\n'
	texto += '"eixoBM:":' + correct(eixoBM) + ',\n'
	texto += '"eixoLC:":' + correct(eixoLC) + ',\n'
	texto += '"url":"' + normaliza(nome) + '.json", \n'
	texto += '"tipo":"' + tipo + '",\n'
	texto += '"livro":"' + livro + '"\n'
	texto += '}'
	return texto

def markdown(nome, mfor, mdes, mcon, mint, msab, mcar, mbba, mniv, deuses, eixoBM, eixoLC, tipo, livro, descr):
	texto = "**Titulo**:" + nome + "\n\n"
	texto += "**Talento de " + tipo + "**" + "\n\n"
	texto += "**" + livro + "**" + "\n\n"
	texto += descr
	return texto

def generateMD(nome, mfor, mdes, mcon, mint, msab, mcar, mbba, mniv, deuses, eixoBM, eixoLC, tipo, livro, descr):
	path = "features/markdowns/"
	newNome = normaliza(nome)
	saveFile = open(path+newNome+".markdown", 'w')
	texto = markdown(nome, mfor, mdes, mcon, mint, msab, mcar, mbba, mniv, deuses, eixoBM, eixoLC, tipo, livro, descr)
	saveFile.write(texto)
	saveFile.close()

def generateJSON(nome, mfor, mdes, mcon, mint, msab, mcar, mbba, mniv, deuses, eixoBM, eixoLC, tipo, livro):
	path = "features/jsons/new/new/"
	newNome = normaliza(nome)
	saveFile = open(path+newNome+".json", 'w')
	texto = json(nome, mfor, mdes, mcon, mint, msab, mcar, mbba, mniv, deuses, eixoBM, eixoLC, tipo, livro)
	saveFile.write(texto)
	saveFile.close()
	
def generate(nome, mfor, mdes, mcon, mint, msab, mcar, mbba, mniv, deuses, eixoBM, eixoLC, tipo, livro, descr):
	generateJSON(nome, mfor, mdes, mcon, mint, msab, mcar, mbba, mniv, deuses, eixoBM, eixoLC, tipo, livro)
	generateMD(nome, mfor, mdes, mcon, mint, msab, mcar, mbba, mniv, deuses, eixoBM, eixoLC, tipo, livro, descr)

livro = raw_input("Qual o livro usado como fonte? ")
while True:
	tipo_talento = raw_input("Qual o tipo de talento? ")
	while True:
		os.system('cls' if os.name == 'nt' else 'clear')
		nome = raw_input("Digite o nome do Talento: ")
		if (nome == ""):
			break
		min_for = raw_input("Digite a força minima para usar esse talento (Caso não possua, deixe em branco): ")
		min_des = raw_input("Digite a destreza minima para usar esse talento (Caso não possua, deixe em branco): ")
		min_con = raw_input("Digite a constituição minima para usar esse talento (Caso não possua, deixe em branco): ")
		min_int = raw_input("Digite a inteligência minima para usar esse talento (Caso não possua, deixe em branco): ")
		min_sab = raw_input("Digite a sabedoria minima para usar esse talento (Caso não possua, deixe em branco): ")
		min_car = raw_input("Digite a carisma minima para usar esse talento (Caso não possua, deixe em branco): ")
		bba_min = raw_input("Digite o BBA minimo para usar esse talento (Caso não possua, deixe em branco): ")
		niv_min = raw_input("Digite o nível minimo para usar esse talento (Caso não possua, deixe em branco): ")
		deuses = raw_input("Digite os deuses que é necessário ser devoto para adquirir o talento (separe por ', ' caso seja mais de um; caso não haja, deixe em branco):").split(", ")
		eixoBM = raw_input("Digite a(s) tendência(s) no eixo Bondoso-Maligno necessária(s) para adquirir o talento (separe por ', ' caso seja mais de um; caso não haja, deixe em branco):").split(", ")
		eixoLC = raw_input("Digite a(s) tendência(s) no eixo Leal-Caótico necessária(s) para adquirir o talento (separe por ', ' caso seja mais de um; caso não haja, deixe em branco):").split(", ")
		print("Digite a descrição do talento, incluindo pré-requisitos, benefícios e especiais: \n")
		descr = ""
		while True:
			entrada = raw_input()
			if entrada == "":
				break
			descr += " " + entrada
		
		generate(nome, min_for, min_des, min_con, min_int, min_sab, min_car, bba_min, niv_min, deuses, eixoBM, eixoLC, tipo_talento, livro, descr)

	cont = raw_input("Deseja continuar adicionando talentos do livro %s? s/n" % livro)
	if (cont == "n"):
			break
