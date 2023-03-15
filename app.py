from selecionar_palavra import carrega_palavra_secreta

class JogoDeForca:
    def __init__(self, palavra):
        self.palavra = palavra.lower()
        self.tentativas = 6
        self.letras_usadas = set()
        self.palavra_atual = "_" * len(self.palavra)
    
    def jogar(self):
        while self.tentativas > 0 and "_" in self.palavra_atual:
            self.exibir_status()
            letra = input("Digite uma letra: ").lower()
            if letra in self.letras_usadas:
                print("Você já usou essa letra!")
            elif letra in self.palavra:
                print("Acertou!")
                self.adicionar_letra(letra)
            else:
                print("Errou!")
                self.tentativas -= 1
            print()
        if "_" not in self.palavra_atual:
            print(f"Parabéns, você acertou a palavra '{self.palavra}'!")
        else:
            print(f"Fim de jogo! A palavra era '{self.palavra}'.")
    
    def adicionar_letra(self, letra):
        self.letras_usadas.add(letra)
        for i in range(len(self.palavra)):
            if letra == self.palavra[i]:
                self.palavra_atual = self.palavra_atual[:i] + letra + self.palavra_atual[i+1:]
    
    def exibir_status(self):
        print(f"Palavra: {self.palavra_atual}")
        print(f"Tentativas restantes: {self.tentativas}")
        print(f"Letras usadas: {' '.join(sorted(self.letras_usadas))}")
        print()

palavra_secreta = carrega_palavra_secreta()
jogo = JogoDeForca(palavra_secreta)
jogo.jogar()