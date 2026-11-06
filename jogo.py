tabuleiro = [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]
simbolo_atual = "X"
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

        print("\n    0  1  2")
        print("  -----------")
        for i in range(3): 
            print(f"{i} | {tabuleiro[i][0]} | {tabuleiro[i][1]} | {tabuleiro[i][2]} |")
            print("  -------------")

    elif opcao == "3":
        print("\nSaindo do jogo. até mais!")
        rodando = False
    else:
        print("\nOpção invalida! escolha 1 ou 3.")

    if simbolo_atual == "X":
       simbolo_atual == "O"
    else:
       simbolo_atual == "X"
