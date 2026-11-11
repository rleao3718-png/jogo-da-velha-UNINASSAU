#arquivo criado pra não mexer no codigo principal enquanto a partida de bot ainda ta em criação - jessica
#placar dos jogadores - jessica
placar_j_um = 0
placar_j_dois = 0

#total de partidas e empates dos jogadores - jessica
total_partidas = 0
total_empates = 0

#placar do jogador 1 e do bot - jessica
placar_j_um_bot = 0
placar_bot = 0

#total de partidas e empates do jogador 1 e do bot - jessica
total_partidas_bot = 0
total_empates_bot = 0

#representação do tabuleiro - marilia
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
        rodando_partida = True
        venceu = False
        empatou = False
        simbolo_atual = "X"
        contador_partidas = 0
        contador_rodadas = 0
        print("\nNova Partida - 2 Jogadores.")

        contador_partidas += 1
        print(f"\n=== Partida N. {contador_partidas} ===")

        #resetando o tabuleiro - marilia
        for i in range(3):
            for j in range(3):
                tabuleiro[i][j] = " "

        #mostrando o tabuleiro inicial - marilia
        print("\n    0   1   2")
        print("  --------------")
        for i in range(3): 
            print(f"{i} | {tabuleiro[i][0]} | {tabuleiro[i][1]} | {tabuleiro[i][2]} |")
            print("  -------------")
        

        while rodando_partida:
            contador_rodadas += 1
            print(f"\n--- Rodada N. {contador_rodadas} ---")

            #começando a partida - jessica
            print(f"\nÉ a vez do jogador {simbolo_atual}.")
            escolha_linha = input("Escolha a linha (0, 1 ou 2): ")
            escolha_coluna = input("Escolha a coluna (0, 1 ou 2): ")

            #checando se a escolha é válida - jessica
            if ((escolha_linha != "0" and escolha_linha != "1" and escolha_linha != "2") or (escolha_coluna != "0" and escolha_coluna != "1" and escolha_coluna != "2")):
                print("\nEscolha inválida! Digite 0, 1 ou 2.")
                contador_rodadas -= 1
                continue

            #convertendo a escolha pra inteiro - jessica
            escolha_linha = int(escolha_linha)
            escolha_coluna = int(escolha_coluna)

            #checando se a casa escolhida ta ocupada - jessica
            if tabuleiro[escolha_linha][escolha_coluna] == "X" or tabuleiro[escolha_linha][escolha_coluna] == "O":
                print("\nEssa casa já está ocupada! Escolha outra.")
                contador_rodadas -= 1
                continue

            tabuleiro[escolha_linha][escolha_coluna] = simbolo_atual

            #checando se houve empate - jessica
            for i in range(3):
                for j in range(3):
                    if tabuleiro[i][j] == " ":
                        break
                    elif tabuleiro[i][j] != " " and i == 2 and j == 2:
                        empatou = True

            for i in range(3):
                    #vitoria na horizontal - jessica
                    if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == simbolo_atual and tabuleiro[i][0] != " ":
                        print(f"\nO jogador {simbolo_atual} venceu!")
                        venceu = True

                    #vitoria na vertical
                    if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] == simbolo_atual and tabuleiro[0][i] != " ":
                        print(f"\nO jogador {simbolo_atual} venceu!")
                        venceu = True

            #vitoria na diagonal - jessica
            if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == simbolo_atual and tabuleiro[0][0] != " ":
                print(f"\nO jogador {simbolo_atual} venceu!")
                venceu = True
            if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == simbolo_atual and tabuleiro[0][2] != " ":
                print(f"\nO jogador {simbolo_atual} venceu!")
                venceu = True

            #mostrando o tabuleiro final - jessica
            print("\n    0   1   2")
            print("  --------------")
            for i in range(3):
                print(f"{i} | {tabuleiro[i][0]} | {tabuleiro[i][1]} | {tabuleiro[i][2]} |")
                print("  -------------")

            #trocando o simbolo do jogador atual - marilia
            if simbolo_atual == "X":
                   simbolo_atual = "O"
            else:
                   simbolo_atual = "X"

            #checando se houve vitoria ou empate - jessica
            if venceu or empatou:
                if venceu:
                    if simbolo_atual == "O":
                        placar_j_um += 1
                    else:
                        placar_j_dois += 1

                else:
                    total_empates += 1
                    print("\nEmpate!")

                #atualizando o placar e resetando tudo - jessica
                total_partidas += 1
                venceu = False
                empatou = False

                print("\n=== PLACAR ===")
                print(f"\nJogador 1: {placar_j_um}")
                print(f"Jogador 2: {placar_j_dois}")
                print(f"Empates: {total_empates}")
                print(f"Total de partidas: {total_partidas}")

                resposta = (input("\nJogar novamente? Digite 0 para retornar ao Menu e 1 para jogar novamente: "))

                if resposta == "0":
                    rodando_partida = False

                #limpando o tabuleiro e resetando o simbolo atual - jessica
                elif resposta == "1":
                    for i in range(3):
                        for j in range(3):
                            tabuleiro[i][j] = " "

                    simbolo_atual = "X"
                    contador_rodadas = 0
                    
                    contador_partidas += 1
                    print(f"\n=== Partida N. {contador_partidas} ===")

                    #mostrando o tabuleiro pra partida nova - jessica
                    print("\n    0   1   2")
                    print("  --------------")
                    for i in range(3):
                        print(f"{i} | {tabuleiro[i][0]} | {tabuleiro[i][1]} | {tabuleiro[i][2]} |")
                        print("  -------------")
                
                else:
                    print("\nOpção inválida. Voltando ao menu.")
                    rodando_partida = False



    #incompleto
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

            elif escolha_campeonato == "1":
                print("\n=== MELHOR DE 3 ===")
                simbolo_atual = "X"
                campeonato_3 = True
                venceu = False
                empatou = False
                contador_partidas_camp_3 = 0
                contador_rodadas_camp_3 = 0

                placar_j_um_camp_3 = 0
                placar_j_dois_camp_3 = 0
                total_empates_camp_3 = 0
                total_partidas_camp_3 = 0

                for i in range(3):
                    for j in range(3):
                        tabuleiro[i][j] = " "

                contador_partidas_camp_3 += 1
                print(f"\n=== Partida N. {contador_partidas_camp_3} ===")
                
                #mostrando o tabuleiro inicial - marilia
                print("\n    0   1   2")
                print("  --------------")
                for i in range(3): 
                    print(f"{i} | {tabuleiro[i][0]} | {tabuleiro[i][1]} | {tabuleiro[i][2]} |")
                    print("  -------------")
                

                while campeonato_3:
                    contador_rodadas_camp_3 += 1
                    print(f"\n--- Rodada N. {contador_rodadas_camp_3} ---")
                    
                    #começando a partida - jessica
                    print(f"\nÉ a vez do jogador {simbolo_atual}.")
                    escolha_linha = input("Escolha a linha (0, 1 ou 2): ")
                    escolha_coluna = input("Escolha a coluna (0, 1 ou 2): ")

                    #checando se a escolha é válida - jessica
                    if ((escolha_linha != "0" and escolha_linha != "1" and escolha_linha != "2") or (escolha_coluna != "0" and escolha_coluna != "1" and escolha_coluna != "2")):
                        print("\nEscolha inválida! Digite 0, 1 ou 2.")
                        contador_rodadas_camp_3 -= 1
                        continue

                    #convertendo a escolha pra inteiro - jessica
                    escolha_linha = int(escolha_linha)
                    escolha_coluna = int(escolha_coluna)

                    #checando se a casa escolhida ta ocupada - jessica
                    if tabuleiro[escolha_linha][escolha_coluna] == "X" or tabuleiro[escolha_linha][escolha_coluna] == "O":
                        print("\nEssa casa já está ocupada! Escolha outra.")
                        contador_rodadas_camp_3 -= 1
                        continue

                    tabuleiro[escolha_linha][escolha_coluna] = simbolo_atual

                    #checando se houve empate - jessica
                    for i in range(3):
                        for j in range(3):
                            if tabuleiro[i][j] == " ":
                                break
                            elif tabuleiro[i][j] != " " and i == 2 and j == 2:
                                empatou = True

                    for i in range(3):
                            #vitoria na horizontal - jessica
                            if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == simbolo_atual and tabuleiro[i][0] != " ":
                                print(f"\nO jogador {simbolo_atual} venceu!")
                                venceu = True

                            #vitoria na vertical
                            if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] == simbolo_atual and tabuleiro[0][i] != " ":
                                print(f"\nO jogador {simbolo_atual} venceu!")
                                venceu = True

                    #vitoria na diagonal - jessica
                    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == simbolo_atual and tabuleiro[0][0] != " ":
                        print(f"\nO jogador {simbolo_atual} venceu!")
                        venceu = True
                    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == simbolo_atual and tabuleiro[0][2] != " ":
                        print(f"\nO jogador {simbolo_atual} venceu!")
                        venceu = True

                    #mostrando o tabuleiro final - jessica
                    print("\n    0   1   2")
                    print("  --------------")
                    for i in range(3):
                        print(f"{i} | {tabuleiro[i][0]} | {tabuleiro[i][1]} | {tabuleiro[i][2]} |")
                        print("  -------------")

                    #trocando o simbolo do jogador atual - marilia
                    if simbolo_atual == "X":
                        simbolo_atual = "O"
                    else:
                        simbolo_atual = "X"

                    #checando se houve vitoria ou empate - jessica
                    if venceu or empatou:
                        if venceu:
                            if simbolo_atual == "O":
                                placar_j_um_camp_3 += 1
                            else:
                                placar_j_dois_camp_3 += 1

                        else:
                            total_empates_camp_3 += 1
                            print("\nEmpate!")

                        #atualizando o placar e resetando tudo - jessica
                        total_partidas_camp_3 += 1
                        venceu = False
                        empatou = False

                        print("\n=== PLACAR ===")
                        print(f"\nJogador 1: {placar_j_um_camp_3}")
                        print(f"Jogador 2: {placar_j_dois_camp_3}")
                        print(f"Empates: {total_empates_camp_3}")
                        print(f"Total de partidas: {total_partidas_camp_3}")

                        if placar_j_um_camp_3 == 2 or placar_j_dois_camp_3 == 2:
                            print("\nCampeonato encerrado!")
                            if placar_j_um_camp_3 == 2:
                                print("\nO jogador 1 venceu o campeonato!")
                            else:
                                print("\nO jogador 2 venceu o campeonato!")

                            campeonato_3 = False

                        elif total_partidas_camp_3 >= 3:
                            if placar_j_um_camp_3 > placar_j_dois_camp_3:
                                print("\nCampeonato encerrado!")
                                print("\nO jogador 1 venceu o campeonato!")
                            elif placar_j_dois_camp_3 > placar_j_um_camp_3:
                                print("\nCampeonato encerrado!")
                                print("\nO jogador 2 venceu o campeonato!")
                            else:
                                print("\nO campeonato terminou empatado!")
                            campeonato_3 = False

                        else:
                            for i in range(3):
                                for j in range(3):
                                    tabuleiro[i][j] = " "
                        
                            simbolo_atual = "X"
                            contador_rodadas_camp_3 = 0

                            contador_partidas_camp_3 += 1
                            print(f"\n=== Partida N. {contador_partidas_camp_3} ===")

                            #mostrando o tabuleiro pra partida nova - jessica
                            print("\n    0   1   2")
                            print("  --------------")
                            for i in range(3):
                                print(f"{i} | {tabuleiro[i][0]} | {tabuleiro[i][1]} | {tabuleiro[i][2]} |")
                                print("  -------------")
                            continue


        
            elif escolha_campeonato == "2":
                print("\n=== MELHOR DE 5 ===")
                simbolo_atual = "X"
                campeonato_5 = True
                venceu = False
                empatou = False
                contador_partidas_camp_5 = 0
                contador_rodadas_camp_5 = 0

                placar_j_um_camp_5 = 0
                placar_j_dois_camp_5 = 0
                total_empates_camp_5 = 0
                total_partidas_camp_5 = 0

                for i in range(3):
                    for j in range(3):
                        tabuleiro[i][j] = " "

                contador_partidas_camp_5 += 1
                print(f"\n=== Partida N. {contador_partidas_camp_5} ===")
                
                #mostrando o tabuleiro inicial - marilia
                print("\n    0   1   2")
                print("  --------------")
                for i in range(3): 
                    print(f"{i} | {tabuleiro[i][0]} | {tabuleiro[i][1]} | {tabuleiro[i][2]} |")
                    print("  -------------")
                

                while campeonato_5:
                    contador_rodadas_camp_5 += 1
                    print(f"\n--- Rodada N. {contador_rodadas_camp_5} ---")
                    
                    #começando a partida - jessica
                    print(f"\nÉ a vez do jogador {simbolo_atual}.")
                    escolha_linha = input("Escolha a linha (0, 1 ou 2): ")
                    escolha_coluna = input("Escolha a coluna (0, 1 ou 2): ")

                    #checando se a escolha é válida - jessica
                    if ((escolha_linha != "0" and escolha_linha != "1" and escolha_linha != "2") or (escolha_coluna != "0" and escolha_coluna != "1" and escolha_coluna != "2")):
                        print("\nEscolha inválida! Digite 0, 1 ou 2.")
                        contador_rodadas_camp_5 -= 1
                        continue

                    #convertendo a escolha pra inteiro - jessica
                    escolha_linha = int(escolha_linha)
                    escolha_coluna = int(escolha_coluna)

                    #checando se a casa escolhida ta ocupada - jessica
                    if tabuleiro[escolha_linha][escolha_coluna] == "X" or tabuleiro[escolha_linha][escolha_coluna] == "O":
                        print("\nEssa casa já está ocupada! Escolha outra.")
                        contador_rodadas_camp_5 -= 1
                        continue

                    tabuleiro[escolha_linha][escolha_coluna] = simbolo_atual

                    #checando se houve empate - jessica
                    for i in range(3):
                        for j in range(3):
                            if tabuleiro[i][j] == " ":
                                break
                            elif tabuleiro[i][j] != " " and i == 2 and j == 2:
                                empatou = True

                    for i in range(3):
                            #vitoria na horizontal - jessica
                            if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == simbolo_atual and tabuleiro[i][0] != " ":
                                print(f"\nO jogador {simbolo_atual} venceu!")
                                venceu = True

                            #vitoria na vertical
                            if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] == simbolo_atual and tabuleiro[0][i] != " ":
                                print(f"\nO jogador {simbolo_atual} venceu!")
                                venceu = True

                    #vitoria na diagonal - jessica
                    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == simbolo_atual and tabuleiro[0][0] != " ":
                        print(f"\nO jogador {simbolo_atual} venceu!")
                        venceu = True
                    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == simbolo_atual and tabuleiro[0][2] != " ":
                        print(f"\nO jogador {simbolo_atual} venceu!")
                        venceu = True

                    #mostrando o tabuleiro final - jessica
                    print("\n    0   1   2")
                    print("  --------------")
                    for i in range(3):
                        print(f"{i} | {tabuleiro[i][0]} | {tabuleiro[i][1]} | {tabuleiro[i][2]} |")
                        print("  -------------")

                    #trocando o simbolo do jogador atual - marilia
                    if simbolo_atual == "X":
                        simbolo_atual = "O"
                    else:
                        simbolo_atual = "X"

                    #checando se houve vitoria ou empate - jessica
                    if venceu or empatou:
                        if venceu:
                            if simbolo_atual == "O":
                                placar_j_um_camp_5 += 1
                            else:
                                placar_j_dois_camp_5 += 1

                        else:
                            total_empates_camp_5 += 1
                            print("\nEmpate!")

                        #atualizando o placar e resetando tudo - jessica
                        total_partidas_camp_5 += 1
                        venceu = False
                        empatou = False

                        print("\n=== PLACAR ===")
                        print(f"\nJogador 1: {placar_j_um_camp_5}")
                        print(f"Jogador 2: {placar_j_dois_camp_5}")
                        print(f"Empates: {total_empates_camp_5}")
                        print(f"Total de partidas: {total_partidas_camp_5}")

                        if placar_j_um_camp_5 == 3 or placar_j_dois_camp_5 == 3:
                            print("\nCampeonato encerrado!")
                            if placar_j_um_camp_5 == 3:
                                print("\nO jogador 1 venceu o campeonato!")
                            else:
                                print("\nO jogador 2 venceu o campeonato!")

                            campeonato_5 = False

                        elif total_partidas_camp_5 >= 5:
                            if placar_j_um_camp_5 > placar_j_dois_camp_5:
                                print("\nCampeonato encerrado!")
                                print("\nO jogador 1 venceu o campeonato!")
                            elif placar_j_dois_camp_5 > placar_j_um_camp_5:
                                print("\nCampeonato encerrado!")
                                print("\nO jogador 2 venceu o campeonato!")
                            else:
                                print("\nO campeonato terminou empatado!")
                            campeonato_5 = False

                        else:
                            for i in range(3):
                                for j in range(3):
                                    tabuleiro[i][j] = " "
                        
                            simbolo_atual = "X"
                            contador_rodadas_camp_5 = 0

                            contador_partidas_camp_5 += 1
                            print(f"\n=== Partida N. {contador_partidas_camp_5} ===")

                            #mostrando o tabuleiro pra partida nova - jessica
                            print("\n    0   1   2")
                            print("  --------------")
                            for i in range(3):
                                print(f"{i} | {tabuleiro[i][0]} | {tabuleiro[i][1]} | {tabuleiro[i][2]} |")
                                print("  -------------")
                            continue                
                



        
            elif escolha_campeonato != "0" and escolha_campeonato != "1" and escolha_campeonato != "2":
                print("\nEscolha inválida. Digite um número de 0 a 2.")


    #incompleto
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

            elif escolha_campeonato_bot == "1":
                print("\n=== MELHOR DE 3 ===")
                rodando_campeonato_bot = False
        
            elif escolha_campeonato_bot == "2":
                print("\n=== MELHOR DE 5 ===")
                rodando_campeonato_bot = False
        
            elif escolha_campeonato_bot != "0" and escolha_campeonato_bot != "1" and escolha_campeonato_bot != "2":
                print("\nEscolha inválida. Digite um número de 0 a 2.")



    elif opcao == "5":
        print("\n=== REGRAS ===")
        print("\nO jogo da velha é um jogo de tabuleiro simples, que pode ser jogado por duas pessoas. O objetivo do jogo é preencher uma grade de 3 por 3 com os símbolos 'X' e 'O'")
        print("\nO jogador deve posiciona-los de forma que um jogador consiga obter três símbolos iguais em linha reta, seja na horizontal, na vertical ou na diagonal, antes do outro jogador.")
        print("\nO primeiro jogador coloca o seu símbolo em uma das células vazias da grade. O segundo jogador então faz o mesmo, e os jogadores alternam até que todas as células sejam preenchidas ou um dos jogadores consiga completar uma linha, coluna ou diagonal com seus símbolos.")
        print("\nSe um jogador conseguir obter três símbolos em linha reta, ele vence o jogo. Se todas as células forem preenchidas e nenhum dos jogadores conseguir completar uma linha reta, o jogo termina em empate.")


    
    elif opcao == "6":
        print("\n=== ESTATÍSTICAS ===")

        if total_partidas == 0 and total_partidas_bot == 0:
            print("\nNenhuma partida registrada.")
        
        else:
            if total_partidas > 0:
                #calculando a porcentagem de vitórias - jessica
                porcentagem_j_um = (placar_j_um / total_partidas) * 100
                porcentagem_j_dois = (placar_j_dois / total_partidas) * 100
            
                print("\n--- 2 Jogadores ---")
                print(f"\nVitórias do Jogador 1: {placar_j_um}")
                print(f"Vitórias do Jogador 2: {placar_j_dois}")
                print(f"Porcentagem de Vitória - Jogador 1: {porcentagem_j_um:.2f}%")
                print(f"Porcentagem de Vitória - Jogador 2: {porcentagem_j_dois:.2f}%")
                print(f"Total de Partidas: {total_partidas}")
                print(f"Total de Empates: {total_empates}")

            #as partidas de bot tão separadas porque senão da erro de divisão por zero caso só haja partidas de player registradas, e vice versa - jessica
            if total_partidas_bot > 0:
                porcentagem_j_um_bot = (placar_j_um_bot / total_partidas_bot) * 100
                porcentagem_bot = (placar_bot / total_partidas_bot) * 100
            
                print("\n--- Contra Bot ---")
                print(f"\nVitórias do Jogador 1: {placar_j_um_bot}")
                print(f"Vitórias do Bot: {placar_bot}")
                print(f"Porcentagem de Vitória - Jogador 1: {porcentagem_j_um_bot:.2f}%")
                print(f"Porcentagem de Vitória - Bot: {porcentagem_bot:.2f}%")
                print(f"Total de Partidas: {total_partidas_bot}")
                print(f"Total de Empates: {total_empates_bot}")



    elif opcao == "7":
        print("\n=== ESTATÍSTICAS ===")

        if total_partidas == 0 and total_partidas_bot == 0:
            print("\nNenhuma partida registrada.")

        else:
            if total_partidas > 0:
                porcentagem_j_um = (placar_j_um / total_partidas) * 100
                porcentagem_j_dois = (placar_j_dois / total_partidas) * 100

                print("\n--- 2 Jogadores ---")
                print(f"\nVitórias do Jogador 1: {placar_j_um}")
                print(f"Vitórias do Jogador 2: {placar_j_dois}")
                print(f"Porcentagem de Vitória - Jogador 1: {porcentagem_j_um:.2f}%")
                print(f"Porcentagem de Vitória - Jogador 2: {porcentagem_j_dois:.2f}%")
                print(f"Total de Partidas: {total_partidas}")
                print(f"Total de Empates: {total_empates}")

            if total_partidas_bot > 0:
                porcentagem_j_um_bot = (placar_j_um_bot / total_partidas_bot) * 100
                porcentagem_bot = (placar_bot / total_partidas_bot) * 100

                print("\n--- Contra Bot ---")
                print(f"\nVitórias do Jogador 1: {placar_j_um_bot}")
                print(f"Vitórias do Bot: {placar_bot}")
                print(f"Porcentagem de Vitória - Jogador 1: {porcentagem_j_um_bot:.2f}%")
                print(f"Porcentagem de Vitória - Bot: {porcentagem_bot:.2f}%")
                print(f"Total de Partidas: {total_partidas_bot}")
                print(f"Total de Empates: {total_empates_bot}")

        print("\nSaindo do jogo. Até mais!")
        rodando = False


    #escrito assim por estar dando erro de opção inválida quando voltava ao menu depois de um jogo - jessica
    elif opcao != "1" and opcao != "2" and opcao != "3" and opcao != "4" and opcao != "5" and opcao != "6" and opcao != "7":
        print("\nOpção inválida! Escolha um número de 1 a 7.")