from random import randint
from time import sleep
from interface import *
from arquivo import *
from temas import *

gameDone = False
opc = 'N'
cabecalho('MENU')
while True:
	if opc == 'N':
		while True:
			resposta = menu(['jogar', 'adicionar nova palavra', 'sair'])
			if str(resposta) in '123':
				if resposta == 1:
					cabecalho('FORCA')
					opc = 'S'
					tema = randomList(palavras)
					palavra = tema[1]
					tema = tema[0]
					palavra = randomWord(palavra)
					palpitesCorretos = ''
					palpitesErrados = ''
					todosPalpites = ''
					break
				elif resposta == 2:
					cabecalho('NOVA PALAVRA')
					while True:
						_tema = menu(['animais', 'frutas', 'cancelar'])
						if str(_tema) in '123':
							if _tema == 1:
								_tema = 'animais'
							elif _tema == 2:
								_tema = 'frutas'
							elif _tema == 3:
								break
							nova_palavra = str(input('Digite a nova palavra: ')).lower()
							if nova_palavra in palavras[_tema]:
								print('\033[31mA palavra "{}" já existe no tema {}'.format(nova_palavra, _tema))
								sleep(1)
							else:
								aprovado = True
								for l in nova_palavra:
									if not l in 'abcdefghijklmnopqrstuvwxyzç':
										aprovado = False
										break
								if aprovado:
									escreverNovaPalavra(_tema, nova_palavra)
								else:
									print('\033[31mHouve um erro ao adicionar a nova apalvra. Dica: Evite acentuação\033[m')
									sleep(1)
								break
						elif str(_tema).isnumeric():
							print('\033[31mEsse tema não existe\033[m')
				elif resposta == 3:
					print('BYE')
					quit()
			elif str(resposta).isnumeric():
				print('\033[31mEssa opção não é valida\033[m')
	
	interface(HANGMANPICS, palavra, palpitesCorretos, palpitesErrados, tema)
	palpite = getGuess(todosPalpites)
	todosPalpites += palpite
	if palpite in palavra:
		palpitesCorretos += palpite

	elif not palpite in palavra:
		palpitesErrados += palpite
	
	if not len(palpitesErrados) == len(HANGMANPICS)-1:
		perdeu = gameDone = False
	else:
		perdeu = gameDone = True
	
	if not perdeu:	
		for i in range(len(palavra)):
			if not palavra[i] in palpitesCorretos:
				encontrouTodasAsLetras = gameDone = False
				break
			else:
				encontrouTodasAsLetras = gameDone = True
			
	if gameDone:
		if perdeu:
			print('\033[31mVocê perdeu :(\033[m')
			print('\033[33mA palavra era {}\033[m'.format(palavra))
			
		elif encontrouTodasAsLetras:
			print('\033[32mVocê venceu :)\033[m')
			print('\033[33mA palavra era {}\033[m'.format(palavra))
			
		while True:
			try:
				opc = str(input('\033[36mQuer jogar de novo?[S/N]:\033[m ')).upper().strip()[0]
			except:
				print('\033[31mEssa opção é invalida\033[m')
			else:
				if opc == 'N':
						cabecalho('MENU')
						break

				elif opc == 'S':
					cabecalho('NOVO JOGO')
					tema = randomList(palavras)
					palavra = tema[1]
					tema = tema[0]
					palavra = randomWord(palavra)

					palpitesCorretos = ''
					palpitesErrados = ''
					todosPalpites = ''
					break







