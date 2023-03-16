from selecionar_palavra import carrega_palavra_secreta
from selecionar_palavra import dica

def comecar_nova_rodada():
    palavra = carrega_palavra_secreta()

    #print(palavra)

    erros = 0

    tentativas = 0

    chances = 6

    letras_erradas = []

    visualizacao = ['_'] * len(palavra)

    print(visualizacao)

    while tentativas < chances:
        print(f'\033[31mDica:{dica(palavra)}\033[m')

        if tentativas > 0:
                if erros == 1:
                    print(""" ____   
 |  o    
 |    
 | 
_|_    """)        
                    
                elif erros == 2:
                    print(""" ____   
 |  o    
 |  |  
 | 
_|_    """)  
                elif erros == 3:
                    print(""" ____   
 |  o    
 | /|  
 | 
_|_    """) 
                elif erros == 4:
                    print(""" ____   
 |  o    
 | /|\  
 | 
_|_    """) 
                elif erros == 5:
                    print(""" ____   
 |  o    
 | /|\  
 | /
_|_    """) 
                elif erros == 6:
                    print(""" ____   
 |  o    
 | /|\  
 | / \
_|_    """) 
        else:
                    print(""" ____   
 |      
 |   
 | 
_|_    """)

        letra = input('Qual letra você quer tentar? ').strip().upper()[0]

        #Verificaçao de digitaçao apenas com letras
        while not (65 <= ord(letra) <= 90 or 97 <= ord(letra) <= 122):
            print("Digite apenas letras")
            letra = input('Qual letra você quer tentar? ').strip().upper()[0]


        if letra in palavra:
            print('Letra certa!')
            for posicao_da_letra in range(len(palavra)):
                if letra == palavra[posicao_da_letra]:
                    visualizacao[posicao_da_letra] = letra

        else:
            print('Errou')
            tentativas += 1
            erros += 1
            letras_erradas.append(letra)
        print(f'Erros ({tentativas}/6) = {letras_erradas}... ')

        print("~" * (len(palavra) * 5))
        print(visualizacao)

        if not '_' in visualizacao:
            print('Você ganhou!')
            break

        if tentativas == chances:
            print('Mamou')