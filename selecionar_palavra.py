import random

def carrega_palavra_secreta():
    arquivo_das_palavras = ""
    escolha_a_categoria = input("Escolha a categoria[futebol/frutas/paises]:").strip().lower()
    if escolha_a_categoria == "futebol":
        escolha_de_dificuldade = "Escolha um campeonato [serie a/serie b/serie c/champions]:"
    elif escolha_a_categoria == "frutas":
        escolha_de_dificuldade = "Escolha a dificuldade [facil/medio/dificil]:"
    else:
        escolha_de_dificuldade = "Escolha um continente [africa/americas/europa]:"

    dificuldade_das_palavras = input(escolha_de_dificuldade).strip().lower()
    
    if dificuldade_das_palavras == "facil":
        arquivo_das_palavras = "./palavras/frutas-facil.txt"
    elif dificuldade_das_palavras == "medio":
        arquivo_das_palavras = "./palavras/frutas-medio.txt"
    elif dificuldade_das_palavras == "dificil":
        arquivo_das_palavras = "./palavras/frutas-dificil.txt"
    elif dificuldade_das_palavras == "serie a":
        arquivo_das_palavras = "./palavras/times-seriea.txt"
    elif dificuldade_das_palavras == "serie b":
        arquivo_das_palavras = "./palavras/times-serieb.txt"
    elif dificuldade_das_palavras == "serie c":
        arquivo_das_palavras = "./palavras/times-seriec.txt"
    elif dificuldade_das_palavras == "champions":
        arquivo_das_palavras = "./palavras/times-champions.txt"
    elif dificuldade_das_palavras == "africa":
        arquivo_das_palavras = "./palavras/paises-africa.txt"
    elif dificuldade_das_palavras == "americas":
        arquivo_das_palavras = "./palavras/paises-americas.txt"
    elif dificuldade_das_palavras == "europa":
        arquivo_das_palavras = "./palavras/paises-europa.txt"

    arquivo = open(arquivo_das_palavras, "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    
    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

#palavra_secreta = carrega_palavra_secreta()
#print(palavra_secreta)