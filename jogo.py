placar_j_um = 0
placar_j_dois = 0

total_partidas = 1
total_empates = 0


placar_j_um_bot = 5
placar_bot = 0

total_partidas_bot = 17
total_empates_bot = 0

tabuleiro = [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]

simbolo_atual = "X"
rodando = True

while rodando:

    print("\n=== JOGO DA VELHA ===")
    print("\n1. Jogar - 2 Jogadores")
    print("2. Jogar - Contra Bot")
    print("3. Campeonato - 2 Jogadores")
    print("4. Campeonato - Contra Bot")
    print("5. Ver Regras")
    print("6. Estatísticas")
    print("7. Sair")


    opcao = input("\nEscolha uma opção. Digite um número de 1 a 7: ")



    if opcao == "1":
        print("\nIniciando nova partida de 2 jogadores.")
        for i in range(3):
            for j in range(3):
                 tabuleiro[i][j] = " "

        print("\n    0   1   2")
        print("  --------------")
        for i in range(3): 
            print(f"{i} | {tabuleiro[i][0]} | {tabuleiro[i][1]} | {tabuleiro[i][2]} |")
            print("  -------------")
    


    if opcao == "3":
        rodando_campeonato = True

        while rodando_campeonato:

            print("\n=== CAMPEONATO - 2 JOGADORES ===")
            print("\n0. Menu")
            print("1. Melhor de 3")
            print("2. Melhor de 5")

            escolha_campeonato = input ("\nEscolha uma opção. Digite 0 para voltar ao Menu ou 1 e 2 para jogar: ")

            if escolha_campeonato == "0":
                rodando_campeonato = False
                continue

            elif escolha_campeonato == "1":
                print("\n=== MELHOR DE 3 ===")
                rodando_campeonato = False
        
            elif escolha_campeonato == "2":
                print("\n=== MELHOR DE 5 ===")
                rodando_campeonato = False
        
            else:
                print("\nEscolha inválida. Digite um número de 0 a 2.")



if opcao == "4":
        rodando_campeonato_bot = True

        while rodando_campeonato_bot:

            print("\n=== CAMPEONATO - BOT ===")
            print("\n0. Menu")
            print("1. Melhor de 3")
            print("2. Melhor de 5")

            escolha_campeonato_bot = input ("\nEscolha uma opção. Digite 0 para voltar ao Menu ou 1 e 2 para jogar: ")

            if escolha_campeonato_bot == "0":
                rodando_campeonato_bot = False
                continue

            elif escolha_campeonato_bot == "1":
                print("\n=== MELHOR DE 3 ===")
                rodando_campeonato_bot = False
        
            elif escolha_campeonato_bot == "2":
                print("\n=== MELHOR DE 5 ===")
                rodando_campeonato_bot = False
        
            else:
                print("\nEscolha inválida. Digite um número de 0 a 2.")



    elif opcao == "5":
        print("\n=== REGRAS ===")
        print("\nO jogo da velha é um jogo de tabuleiro simples, que pode ser jogado por duas pessoas. O objetivo do jogo é preencher uma grade de 3 por 3 com os símbolos 'X' e 'O'")
        print("\nO jogador deve posiciona-los de forma que um jogador consiga obter três símbolos iguais em linha reta, seja na horizontal, na vertical ou na diagonal, antes do outro jogador.")
        print("\nO primeiro jogador coloca o seu símbolo em uma das células vazias da grade. O segundo jogador então faz o mesmo, e os jogadores alternam até que todas as células sejam preenchidas ou um dos jogadores consiga completar uma linha, coluna ou diagonal com seus símbolos.")
        print("\nSe um jogador conseguir obter três símbolos em linha reta, ele vence o jogo. Se todas as células forem preenchidas e nenhum dos jogadores conseguir completar uma linha reta, o jogo termina em empate.")


    
    elif opcao == "6":
        print("\n=== ESTATÍSTICAS ===")

        if total_partidas == 0:
            print("\nNenhuma partida registrada.")
        
        else:
            porcentagem_j_um = (placar_j_um / total_partidas) * 100
            porcentagem_j_dois = (placar_j_dois / total_partidas) * 100
            
            porcentagem_j_um_bot = (placar_j_um_bot / total_partidas_bot) * 100
            porcentagem_bot = (placar_bot / total_partidas_bot) * 100
            
            print("\n=== ESTATÍSTICAS ===")
            
            print("\n--- 2 Jogadores ---")
            print(f"\nVitórias do Jogador 1: {placar_j_um}")
            print(f"Vitórias do Jogador 2: {placar_j_dois}")
            print(f"Porcentagem de Vitória - Jogador 1: {porcentagem_j_um:.2f}%")
            print(f"Porcentagem de Vitória - Jogador 2: {porcentagem_j_dois:.2f}%")
            print(f"Total de Partidas: {total_partidas}")
            print(f"Total de Empates: {total_empates}")
            
            print("\n--- Contra Bot ---")
            print(f"\nVitórias do Jogador 1: {placar_j_um_bot}")
            print(f"Vitórias do Bot: {placar_bot}")
            print(f"Porcentagem de Vitória - Jogador 1: {porcentagem_j_um_bot:.2f}%")
            print(f"Porcentagem de Vitória - Bot: {porcentagem_bot:.2f}%")
            print(f"Total de Partidas: {total_partidas_bot}")
            print(f"Total de Empates: {total_empates_bot}")



    elif opcao == "7":
        porcentagem_j_um = (placar_j_um / total_partidas) * 100
        porcentagem_j_dois = (placar_j_dois / total_partidas) * 100

        porcentagem_j_um_bot = (placar_j_um_bot / total_partidas_bot) * 100
        porcentagem_bot = (placar_bot / total_partidas_bot) * 100

        print("\n=== ESTATÍSTICAS ===")

        print("\n--- 2 Jogadores ---")
        print(f"\nVitórias do Jogador 1: {placar_j_um}")
        print(f"Vitórias do Jogador 2: {placar_j_dois}")
        print(f"Porcentagem de Vitória - Jogador 1: {porcentagem_j_um:.2f}%")
        print(f"Porcentagem de Vitória - Jogador 2: {porcentagem_j_dois:.2f}%")
        print(f"Total de Partidas: {total_partidas}")
        print(f"Total de Empates: {total_empates}")

        print("\n--- Contra Bot ---")
        print(f"\nVitórias do Jogador 1: {placar_j_um_bot}")
        print(f"Vitórias do Bot: {placar_bot}")
        print(f"Porcentagem de Vitória - Jogador 1: {porcentagem_j_um_bot:.2f}%")
        print(f"Porcentagem de Vitória - Bot: {porcentagem_bot:.2f}%")
        print(f"Total de Partidas: {total_partidas_bot}")
        print(f"Total de Empates: {total_empates_bot}")
        print("\nSaindo do jogo. Até mais!")
        rodando = False



    else:
        print("\nOpção inválida! Escolha um número de 1 a 7.")

    if simbolo_atual == "X":
       simbolo_atual = "O"
    else:
       simbolo_atual = "X"
    
    
