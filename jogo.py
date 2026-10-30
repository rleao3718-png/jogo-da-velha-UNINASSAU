def exibir_tabuleiro(tab):
    print("\n    0  1  2")
    print("\ -----------")
    for i in range(3):
        print(f"{i} | " + " | ".join(tab[i]) + " | ")
        print("  -------------")

rodando = True
while rodando: 
    print("\n=== JOGO DA VELHA ===")
    print("1. jogar")
    print("3. sair")

    opcao = input("eescolha uma opção: ")

    if opcao == "1":
        print("\nIniciando nova partida...")
    elif opcao == "3":
        print("\nSaindo do jogo. até mais!")
        rodando = False
    else:
        print("\nOpção invalida! escolha 1 ou 3.")