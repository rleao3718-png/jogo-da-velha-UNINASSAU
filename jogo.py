tabuleiro = [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]
def exibir_tabuleiro(tab):
    print("\n    0  1  2")
    print("  -----------")
    for i in range(3):
        print(f"{i} | " + " | ".join(tab[i]) + " | ")
        print("  -------------")

rodando = True
while rodando: 
    print("\n=== JOGO DA VELHA ===")
    print("1. jogar")
    print("3. sair")

    opcao = input("escolha uma opção: ")

    if opcao == "1":
        print("\nIniciando nova partida...")
        for i in range(3):
         for j in range(3):
             tabuleiro[i][j] = " "
        exibir_tabuleiro(tabuleiro)
    elif opcao == "3":
        print("\nSaindo do jogo. até mais!")
        rodando = False
    else:
        print("\nOpção invalida! escolha 1 ou 3.")

# Mecânica de alteração de jogadores no final de cada jogada válida:
if simbolo_atual == "X":
    simbolo_atual =="O"
else:
    simbolo_atual = "X"
     
