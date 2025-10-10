import os
import sys
import random
import time 

# --- Funções Complementares ---

def animacaoRolando(duracao=2, intervalo=0.3):
    """
    Mostra uma pequena animação no terminal da palavra 'rolando...'
    com os pontos variando (. .. ... ....) e repetindo por 'duracao' segundos.
    """
    pontos = [".", "..", "...", "...."]
    inicio = time.time()
    
    while time.time() - inicio < duracao:
        for p in pontos:
            # \r volta o cursor para o início da linha
            print(f"Rolando{p}    ", end="\r", flush=True) 
            time.sleep(intervalo)
    print("Rolando.... pronto!      ") # Espaços extras para limpar a linha

def limparTerminal():
    if (sys.platform.startswith('win')):
        os.system('cls')
    else: 
        os.system('clear')

# --- Funções do Jogo ---

def ordemDados(noOnibus=False):
    """Retorna uma lista de dados (cores) embaralhada."""
    if noOnibus == False:
        # 6 Verdes, 4 Amarelos, 3 Vermelhos, 1 Rosa, 1 Branco, 1 Papai Noel (Total 16)
        dados = ['verde','verde','verde','verde','verde','verde','amarelo','amarelo','amarelo','amarelo','vermelho','vermelho','vermelho','rosa','branco', 'papai noel']
    else:
        # Adiciona 1 Onibus (Total 17)
        dados = ['verde','verde','verde','verde','verde','verde','amarelo','amarelo','amarelo','amarelo','vermelho','vermelho','vermelho','rosa','branco', 'papai noel', 'onibus']
    
    # O random.shuffle modifica a lista in-place e retorna None. 
    # Devemos embaralhar e retornar a própria lista 'dados'.
    random.shuffle(dados)
    return dados

def verificarPontos(resultadoDados, ordemDados):
    """Calcula os pontos (cérebros, tiros, pegadas) de uma rolagem."""
    numeroDePegadas = 0
    numeroDeTiros = 0
    numeroDeCerebros = 0
    
    # É importante iterar sobre os resultados e usar o índice para a ordemDados
    for i in range(len(resultadoDados)):
        resultado = resultadoDados[i]
        cor = ordemDados[i]
        
        if resultado == 'cerebro':
            numeroDeCerebros += 1
        elif resultado == 'tiro':
            numeroDeTiros += 1
        elif resultado == 'pegada':
            numeroDePegadas += 1
        elif resultado == 'dois cerebros':
            numeroDeCerebros += 2
        elif resultado == 'dois tiros':
            numeroDeTiros += 2
        elif resultado == 'capacete':
            # o Capacete te permite aguentar 1 tiro, logo você fica com "-1 tiro"(aguentando assim 4 tiros)
            numeroDeTiros -= 1
        if resultado == 'pegada' and cor == 'verde':
            numeroDePegadas -= 1
            numeroDeCerebros += 1
            
    return (numeroDePegadas, numeroDeCerebros, numeroDeTiros)

def verificarCorDadoComPegada(resultadoDados, ordemDados):
    """Retorna a cor dos dados que resultaram em 'pegada'."""
    coresComPegadas = []
    for i in range(len(resultadoDados)):
        if resultadoDados[i] == 'pegada':
            coresComPegadas.append(ordemDados[i])
    return coresComPegadas

def rolarDados(ordemDadosDisponivel):
    """Rola 3 dados das cores disponíveis e retorna os resultados e a lista de dados atualizada."""
    
    mapeamentoValores = {
        1: "cerebro", 
        2: "pegada", 
        3: "tiro", 
        4: "dois cerebros",
        5: "dois tiros", 
        6: "capacete", 
        7: "energetico"
    }
    
    # Dados de Faces (apenas os valores em vez dos strings para simplificar o 'random.choice')
    dadoVerde = [1, 1, 1, 2, 3, 3] # 'cerebro','cerebro','cerebro','pegada','tiro','tiro'
    dadoAmarelo = [1, 1, 2, 2, 3, 3] # 'cerebro','cerebro','pegada','pegada','tiro','tiro'
    dadoVermelho = [1, 2, 2, 3, 3, 3] # 'cerebro', 'pegada', 'pegada','tiro','tiro','tiro'
    dadoRosa = [1, 2, 2, 2, 3, 3] # 'cerebro', 'pegada','pegada', 'pegada','tiro','tiro'
    dadoBranco = [2, 2, 2, 3, 4, 5] # 'pegada','dois cerebros','dois tiros','capacete','energetico' - Nota: Mapeamento corrigido para 6 faces
    dadoPapaiNoel = [1, 2, 3, 4, 6, 7] # 'cerebro'. 'pegada', 'tiro', 'dois cerebros', 'capacete', 'energetico' - Nota: Mapeamento corrigido para 6 faces
    # dadoOnibus = [] # Não Defini ainda /utilizei
    
    if len(ordemDadosDisponivel) < 3:
        # Se não houver 3 dados para rolar
        return 0, ordemDadosDisponivel
        
    # Seleciona os 3 dados a serem rolados e os remove da lista de disponíveis
    dadosRoladosCores = ordemDadosDisponivel[:3]
    ordemDadosDisponivel = ordemDadosDisponivel[3:] # Remove os 3 primeiros.
    
    print(f'Voce rolou os seguintes dados: {", ".join(dadosRoladosCores)}')
    #print(f'Voce tirou os seguintes dados:{dados_rolados_cores[0]},{dados_rolados_cores[1]} e {dados_rolados_cores[2]} ')
    
    valoresNumericos = []
    for corDado in dadosRoladosCores:
        valorNumerico = None
        if corDado == 'verde':
            valorNumerico = random.choice(dadoVerde)
        elif corDado == 'amarelo':
            valorNumerico = random.choice(dadoAmarelo)
        elif corDado == 'vermelho':
            valorNumerico = random.choice(dadoVermelho)
        elif corDado == 'rosa':
            valorNumerico = random.choice(dadoRosa)
        elif corDado == 'branco':
            valorNumerico = random.choice(dadoBranco)
        elif corDado == 'papai noel':
            valorNumerico = random.choice(dadoPapaiNoel)
        
        if valorNumerico is not None:
            valoresNumericos.append(valorNumerico)

    animacaoRolando()
    
    # Mapeia os números rolados para os resultados em string
    
    resultadosString = [] 
    
    for n in valoresNumericos:
        # 2. Calcula o valor em string para o número atual (n)
        resultadoTraduzido = mapeamentoValores[n]
        
        # 3. Adiciona o valor traduzido à lista (acumulando os resultados)
        resultadosString.append(resultadoTraduzido)

        # A variável 'resultados_string' agora contém todos os valores traduzidos.
        
    # Retorna os resultados em string e a lista de dados disponíveis ATUALIZADA
    return resultadosString, dadosRoladosCores, ordemDadosDisponivel
    
def rodarTurno(dadosDaPartida, numeroDeJogadores, jogadorDaRodada, turno, pontosJogador, ordemDadosDisponivel):
    
    # Garante que o índice do jogador está correto
    jogadorDaRodada = jogadorDaRodada % numeroDeJogadores #Usado para acessar os nomes dos jogadores
    
    # Acessa o nome do jogador pela lista de chaves (nomes) do dicionário
    nomesJogadores = list(dadosDaPartida.keys())
    nomeJogador = nomesJogadores[jogadorDaRodada]
    
    # Placar temporário do turno
    numeroDePegadas = 0
    numeroDeTiros = 0
    numeroDeCerebros = 0
    jogando = True
    
    # Inicia os pontos dos jogadores, se for a primeira vez
    if pontosJogador == []: # Verifica se a lista está vazia
        # Adiciona uma sub-lista de zeros, um para cada jogador
        pontosJogador.extend([0] * numeroDeJogadores)
    
    print("----------------------------------------")
    print(f"Turno: {turno} | Jogador: {nomeJogador} | Placar: {pontosJogador[jogadorDaRodada]} Cérebros")
    
    while jogando == True:
        
        print(f"Pontos atuais no turno: {numeroDeCerebros} Cérebros, {numeroDeTiros} Tiros, {numeroDePegadas} Pegadas.")
        print("-----------------------")
        
        # O rolarDados deve retornar os resultados, as cores roladas, e a lista de dados restantes
        resultadoDados, dadosRoladosCores, ordemDadosDisponivel = rolarDados(ordemDadosDisponivel)
        
        if resultadoDados == 0:
            print("Você já rolou todos os dados possíveis. Fim do seu turno.")
            jogando = False
            break
            
        print("Resultados rolados foram: ")
        # Exibe os resultados corretamente usando índice para unir cores e resultados
        for i in range(len(dadosRoladosCores)):
            # 2. Usa o índice (i) para pegar o item correspondente de CADA lista
            cor = dadosRoladosCores[i]
            resultado = resultadoDados[i]
            # 3. Imprime o resultado
            print(f'Dado {cor}: {resultado}')
            
        # 1. Verifica e soma os pontos da rolagem
        novasPegadas, novosCerebros, novosTiros = verificarPontos(resultadoDados, dadosRoladosCores)
        
        numeroDePegadas += novasPegadas
        numeroDeCerebros += novosCerebros
        numeroDeTiros += novosTiros
        
        # 2. Verifica condição de fim de turno (3+ tiros)
        if numeroDeTiros >= 3:
            print('Você tomou 3 ou mais tiros! Seu turno acabou e você perdeu todos os Cérebros deste turno.')
            jogando = False
            break # Vai para o fim do while
            
        # 3. Verifica condição de vitória
        if pontosJogador[jogadorDaRodada] + numeroDeCerebros >= 13:
            print(f'\n*** Parabéns, o jogador {nomeJogador} ganhou o jogo com {pontosJogador[jogadorDaRodada] + numeroDeCerebros} Cérebros! ***')
            return
            
        # 4. Pergunta se deseja continuar
        desejaContinuarJogando = input('Você deseja continuar jogando? (s/n): ').lower()
        if desejaContinuarJogando == 'n':
            # Fim do turno por escolha: SOMA os cérebros e passa o turno
            print(f'Fim de turno. Você marcou {numeroDeCerebros} Cérebros neste turno.')
            pontosJogador[jogadorDaRodada] += numeroDeCerebros
            jogando = False
            break
        #5. Se escrever sair, o jogo acaba 
        elif desejaContinuarJogando == 'sair':
            print(f'Você saiu do jogo. Até a próxima!')
            return
        # 6. Se o jogador continuar, lida com as 'pegadas'
        if numeroDePegadas > 0:
            # 6a. Pega a lista de cores que resultaram em pegadas na última rolagem
            coresComPegadas = verificarCorDadoComPegada(resultadoDados, dadosRoladosCores)

            # 6b. Embaralha o RESTANTE dos dados disponíveis no 'banco'
            #     A lista 'ordemDadosDisponivel' já foi reduzida em 3 dados pelo 'rolarDados'
            random.shuffle(ordemDadosDisponivel)

            # 6c. CRIA a nova lista de dados a serem rolados:
            #     As pegadas (que devem ser roladas) + o restante do banco embaralhado.
            #     Usamos o '+' para concatenar as listas, garantindo que as pegadas fiquem na frente.
            ordemDadosDisponivel = coresComPegadas + ordemDadosDisponivel

            # 6d. Zera as pegadas no placar temporário do turno
            numeroDePegadas = 0
        else:
            # Se não houve pegadas, os 3 dados simplesmente foram descartados (feito no rolarDados),
            # e a lista de dados restantes não precisa de modificação.
            pass
        
    # Fim do turno: Prepara-se para o próximo jogador
    jogadorDaRodada += 1
    # Se todos jogaram, aumenta o turno e reinicia o índice do jogador
    if jogadorDaRodada >= numeroDeJogadores:
        jogadorDaRodada = 0
        turno += 1
        
    # Reinicia a lista de dados disponíveis para o próximo jogador
    novaOrdemDadosDisponivel = ordemDados()

    # Passa para o próximo turno/jogador
    rodarTurno(dadosDaPartida, numeroDeJogadores, jogadorDaRodada, turno, pontosJogador, novaOrdemDadosDisponivel)

# ... (Resto das funções) ...

def iniciarJogo(numeroDeJogadores, turno = 1):
    limparTerminal()
    # As variáveis de controle de turno e jogador serão gerenciadas em RodarTurno
    turno = 1
    jogadorDaRodada = 0
    dadosDaPartida = {}
    
    # Coleta nomes dos jogadores
    for i in range(numeroDeJogadores):
        nomeJogador = input(f'Digite o nome do jogador número {i + 1}: ')
        dadosDaPartida[nomeJogador] = 0 # Inicialmente 0 pontos
        
    # Inicializa a lista de pontos e a lista de dados disponíveis para a primeira rodada
    pontosJogador = []
    ordemDadosDisponivel = ordemDados()
    
    # Inicia o jogo
    rodarTurno(dadosDaPartida, numeroDeJogadores, jogadorDaRodada, turno, pontosJogador, ordemDadosDisponivel)


def selecionarNumeroDeJogadores():
    while True: # Loop para garantir que a entrada é válida
        print("Selecione o número de jogadores (inteiro > 1):\n")
        numeroDeJogadores = input()
        
        if not numeroDeJogadores.isdigit():
            limparTerminal()
            print("Insira um valor numérico inteiro > 1.")
            continue # Volta para o início do loop
        
        numeroDeJogadores = int(numeroDeJogadores)
        
        if numeroDeJogadores < 2:
            limparTerminal()
            print("Insira um valor numérico inteiro > 1.")
            continue # Volta para o início do loop
            
        return numeroDeJogadores


def abrirMenuIncial():
    limparTerminal()
    print("----- Zombie Roll ----- \n")
    numeroDeJogadores = selecionarNumeroDeJogadores()
    print(f"O número selecionado foi de {numeroDeJogadores} jogadores.")
    iniciarJogo(numeroDeJogadores)


def main():
    abrirMenuIncial()

if __name__ == '__main__':
    main()