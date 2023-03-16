from jogar_uma_rodada import comecar_nova_rodada

comecar_nova_rodada()
fim = input("Deseja jogar novamente? (y/n):").split()[0]
while fim not in "YyNn":
    print("digite apenas 'y' ou 'n'.")
    fim = input("Deseja jogar novamente? (y/n):").split()[0]
if fim == ("y"):
    comecar_nova_rodada()
else:
    exit()