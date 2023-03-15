from selecionar_palavra import carrega_palavra_secreta

def comecar_nova_rodada():
    palavra = carrega_palavra_secreta()

    print(palavra)

    tentativas = 0

    chances = 6

    letras_erradas = []

    visualizacao = ['_'] * len(palavra)

    print(visualizacao)

    while tentativas < chances:

        letra = input('Qual letra você quer tentar? ').strip().upper()[0]

        if letra in palavra:
            print('Letra certa!')
            for posicao_da_letra in range(len(palavra)):
                if letra == palavra[posicao_da_letra]:
                    visualizacao[posicao_da_letra] = letra

        else:
            print('Errou')
            tentativas += 1
            letras_erradas.append(letra)
        print(f'Erros ({tentativas}/6) = {letras_erradas}... ')

        print(visualizacao)

        if not '_' in visualizacao:
            print('Você ganhou!')
            break

        if tentativas == chances:
            print('Mamou')
