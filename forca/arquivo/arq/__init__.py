from time import sleep

def show(msg, endl='\n', time=.05):
	for l in msg:
		print(l, end='', flush=True)
		sleep(time)
	print(endl, end='')


def arquivoExiste(nome):
	try:
		a = open(nome, 'rt')
		a.close()
	except:
		return False
	else:
		return True
	
	
def criarArquivo(nome):
	print('Criando arquivo "{}"\nAguarde'.format(nome),end='')
	show('...',time=1)
	try:
		a = open(nome, 'wt+')
	except:
		print('\033[31mHouve um erro na criação do arquivo "{}"\033[m'.format(nome))
	else:
		print('\033[32mArquivo "{}" criado com sucesso\033[m'.format(nome))
	finally:
		a.close()
		
		
def escrever(nome, temas):
	try:
		a = open(nome, 'at')
	except:
		print('\033[31mHouve um erro ao tentar abrir o arquivo "{}"\033[m'.format(nome))
	else:
		try:
			a.write('palavras = dict()\n{}\n#Abaixo ficam as palavras adicionadas pelos jogadores\n '.format(temas))
		except:
			print('\033[31mHouve um erro ao tentar escrever no arquivo "{}"\033[m'.format(nome))
		finally:
			a.close()
			
			

def escreverNovaPalavra(tema, palavra, nome='temas.py'):
	try:
		a = open(nome, 'at')
	except:
		print('\033[31mHouve um erro ao tentar adicionar a nova palavra\033[m')
	else:
		try:
			a.write('\npalavras["{}"].append("{}")'.format(tema, palavra))
		except:
			print('\033[31mHouve um erro ao tentar adicionar a nova palavra\033[m')
		else:
			print('\033[32mPalavra "{}" adicionada com sucesso\033[m'.format(palavra))
		finally:
			a.close()
		
		
		
		
			
			