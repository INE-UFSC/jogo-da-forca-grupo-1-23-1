from selecionar_palavra import carrega_palavra_secreta

class JogoDeForca:
    
    def __init__(self):
        self.palavra = carrega_palavra_secreta().upper()
        self.tentativas = set()
        self.chances = 7
        self.tentativas.add(" ")
        
    def adivinhar(self, letra):
        letra = letra.upper()
        
        if letra in self.tentativas:
            print(f"Você já tentou a letra '{letra}', tente outra letra.")
            return
        
        self.tentativas.add(letra)
        
        if letra not in self.palavra:
            self.chances -= 1
            print(f"A letra '{letra}' não está na palavra.")
            print(f"Você tem {self.chances} chances restantes.")
            return
        
        print(f"A letra '{letra}' está na palavra.")
        
        if self.ganhou():
            print("Parabéns, você ganhou!")
            return

    def desenha_forca(self):
        print("  _______     ")
        print(" |/      |    ")

        if(self.chances == 6):
            print (" |      (_)   ")
            print (" |            ")
            print (" |            ")
            print (" |            ")

        if(self.chances == 5):
            print (" |      (_)   ")
            print (" |      \     ")
            print (" |            ")
            print (" |            ")

        if(self.chances == 4):
            print (" |      (_)   ")
            print (" |      \|    ")
            print (" |            ")
            print (" |            ")

        if(self.chances == 3):
            print (" |      (_)   ")
            print (" |      \|/   ")
            print (" |            ")
            print (" |            ")

        if(self.chances == 2):
            print (" |      (_)   ")
            print (" |      \|/   ")
            print (" |       |    ")
            print (" |            ")

        if(self.chances == 1):
            print (" |      (_)   ")
            print (" |      \|/   ")
            print (" |       |    ")
            print (" |      /     ")

        if (self.chances == 0):
            print (" |      (_)   ")
            print (" |      \|/   ")
            print (" |       |    ")
            print (" |      / \   ")

        print(" |            ")
        print("_|___         ")
        print()


    def ganhou(self):
        return set(self.palavra) <= self.tentativas
    
    def jogar(self):
        self.print_linha()
        print("Começando o jogo de forca!")
        self.print_linha()
        while self.chances > 0:
            print()
            print(f"Palavra: {self.get_palavra_mascarada()}")
            letra = input("Digite uma letra: ")
            self.adivinhar(letra)
            self.desenha_forca()
            self.print_linha()
            if self.ganhou() or self.chances == 0:
                print(f"A palavra era '{self.palavra}'.")
                break
        if self.ganhou():
            self.jogar_novamente()
        else:
            print("Você perdeu!")
            self.jogar_novamente()        

        
    def get_palavra_mascarada(self):
        return "".join([letra if letra in self.tentativas else "-" for letra in self.palavra])
    
    def jogar_novamente(self):
        resposta = input("Deseja jogar novamente? (s/n) ")
        if resposta.lower() == "s":
            self.__init__()
            self.jogar()
        else:
            print("Obrigado por jogar!")
            return
    
    def print_linha(self):
        print("*****************************************************************************")

jogo = JogoDeForca()
jogo.jogar()