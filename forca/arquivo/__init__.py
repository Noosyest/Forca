from arquivo.arq import *
arq = 'temas.py'

temas = """palavras["frutas"]= "maça banana abacaxi abacate melancia".split()
palavras["animais"]= "macaco cachorro gato macaco elefante".split()"""
	
	
if not arquivoExiste(arq):
	criarArquivo(arq)
	escrever(arq,temas)
