from random import randint
HANGMANPICS = ["""
+----+
/    /
     /
     /
     /
     /
     /
     /
     /
==========
""",
"""

 +----+
 /    /
 O    /
      /
      /
      /
      /
      /
      /
==========
""",
"""
 +----+
 /    /
 O    /
/     /
      /
      /
      /
      /
      /
==========
""",
"""
 +----+
 /    /
 O    /
/ \   /
      /
      /
      /
      /
      /
==========
""",
"""
 +----+
 /    /
 O    /
/|\   /
      /
      /
      /
      /
      /
==========
""",
"""
 +----+
 /    /
 O    /
/|\   /
/     /
      /
      /
      /
      /
==========
""",
"""
 +----+
 /    /
 O    /
/|\   /
/ \   /
      /
      /
      /
      /
==========
"""]

def cabecalho(msg, tam=42):
	print('-'*tam)
	print(msg.center(tam))
	print('-'*tam)


def leiaInt(msg, err='\033[31mErro: digite um número inteiro válido\033[m'):
	try:
		num = int(input(msg))
	except:
		print(err)
	else:
		return num


def menu(lista):
	for c, i in enumerate(lista):
		print('\033[33m{}- \033[34m{}\033[m'.format(c+1, i))
	opc = leiaInt('\033[32mSua opção: \033[m', '\033[31mEssa opção não é valida\033[m')
	return opc


def randomList(dicionario):
	tema = randint(1, 2)
	if tema == 1:
		return ['Animais', dicionario["animais"]]
	else:
		return ['Frutas' ,dicionario["frutas"]]
	



def randomWord(lista):
	random = randint(0, len(lista)-1)
	palavra = lista[random]
	return palavra


def getGuess(todosPalpites):
	while True:
		guess = input('\033[34mQual o seu palpite? \033[m')
		guess = guess.lower()
		if len(guess) != 1:
			print('\033[31mDigite uma unica letra\033[m')
		elif not guess in 'abcdefghijklmnopqrstuvwxyzç':
			print('\033[31mDigite uma LETRA\033[m')
		elif guess in todosPalpites:
			print('\33[31mVocê já fez esse palpite antes\033[m')
		else:
			return guess
	
	
def interface(HANGMANPICS, palavra, palpitesCorretos, palpitesErrados, tema):
	print('O tema é {}'.format(tema))
	print('\033[36mPalpites errados: \033[33m{}\033[m'.format(palpitesErrados))
	print(HANGMANPICS[len(palpitesErrados)])
	blanks = '-'*len(palavra)
	for i in range(len(palavra)):
		if palavra[i] in palpitesCorretos:
			blanks = blanks[:i] + palavra[i] + blanks[i+1:]
	for letra in blanks:
		print('\033[35m{}\033[m'.format(letra), end='')
	print()
	
	
	
	
	
	
