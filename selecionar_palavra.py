import random
def carrega_palavra_secreta():
    arquivo = open("tudo.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


def dica(palavra_secreta):
    dica = " "
    lista = ["frutas-dificil", "frutas-facil", "frutas-medio", "paises-africa", "paises-americas",
             "paises-europa",
             "times-champions", "times-seriea", "times-serieb", "times-seriec"]
    for c in lista:
        arquivo = open(c + ".txt", "r")
        palavras = []

        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha.upper())

        arquivo.close()
        if palavra_secreta in palavras:
            dica = c
    return dica

#palavra_secreta = carrega_palavra_secreta()
#dica = dica(palavra_secreta)
#print(palavra_secreta,dica)