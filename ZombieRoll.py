import os
import sys
import random
import time 

def main():
    AbrirMenuIncial()



def AbrirMenuIncial():
    print("Zombie Roll \n")
    numeroDeJogadores = SelecionarNumeroDeJogadores()
    print(f"O numero selecionado foi de {numeroDeJogadores}")
    IniciarJogo(numeroDeJogadores)


def SelecionarNumeroDeJogadores():
        print("Selecione o numero de jogadores:\n")
        numeroDeJogadores = input()
        if (numeroDeJogadores.isdigit() == False):
            LimparTerminal
            print("insira um valor numerico de inteiros > 1")
            SelecionarNumeroDeJogadores()
        if (numeroDeJogadores == '1'):
            LimparTerminal
            print("Insira um valor numerico inteiro > 1")
            SelecionarNumeroDeJogadores()
        numeroDeJogadores = int(numeroDeJogadores)
        return numeroDeJogadores

def IniciarJogo(numeroDeJogadores, turno = 1):
    LimparTerminal()
    turno =1
    jogadorDaRodada = 0
    dadosDaPartida = {}
    for i in range(numeroDeJogadores):
        nomeJogador = input(f'Digite o nome do jogador numero {i +1}')
        dadosDaPartida[nomeJogador] = []
    RodarTurno(dadosDaPartida,numeroDeJogadores, jogadorDaRodada, turno)

def RodarTurno(dadosDaPartida, numeroDeJogadores, jogadorDaRodada, turno, pontosJogador = []): 
    dadosDaPartida = dadosDaPartida
    numeroDeJogadores = numeroDeJogadores
    turno = turno
    jogadorDaRodada = jogadorDaRodada
    numeroDePegadas = 0
    numeroDeTiros = 0
    numeroDeCerebros = 0
    jogando = True
    desejaContinuarJogando = ''
    if(jogadorDaRodada> numeroDeJogadores):
        jogadorDaRodada = 0
    nomeJogador = dadosDaPartida[jogadorDaRodada]
    resultadoDados = None
    if pontosJogador == []:
        pontosJogador.append([0]*len(dadosDaPartida))
    print(f"Turno: {turno}")
    print("Rolagem de "+nomeJogador)
    
    ordemDados = ordemDados()

    while jogando == True:
        print("-----------------------")
        resultadoDados, ordemDados = rolarDados(ordemDados)
        if resultadoDados == 0:
            print("Você já rolou todos os dados possíveis, passaremos seu turno")
            jogadorDaRodada+=1
            turno+=1
            RodarTurno(dadosDaPartida,numeroDeJogadores, jogadorDaRodada, turno, pontosJogador)

        print("Dados rolados foram: ")
        print(f'Dado {ordemDados[0]}: {resultadoDados[0]}, dado {ordemDados[1]}: {resultadoDados[1]} e dado {ordemDados[2]}: {resultadoDados[2]}')
        novas_pegadas, novos_cerebros, novos_tiros = VerificarPontos(resultadoDados, ordemDados)
        numeroDePegadas += novas_pegadas
        numeroDeCerebros += novos_cerebros
        numeroDeTiros += novos_tiros
        if numeroDeTiros> 3:
            print('Você tomou mais do que 3 tiros, passaremos seu turno. Você não ganhou nenhuma pontuação ')
            jogadorDaRodada+=1
            turno+=1
            RodarTurno(dadosDaPartida,numeroDeJogadores, jogadorDaRodada, turno, pontosJogador)
        desejaContinuarJogando = input('Você deseja continuar jogando?(s/n)')
        if desejaContinuarJogando == 'n':
            jogando = False
            if pontosJogador[0][jogadorDaRodada] >= 13:
                print(f'Parabéns, o jogador {nomeJogador} ganhou o jogo!!!')
                return 0
            pontosJogador[0][jogadorDaRodada] += numeroDeCerebros
            jogadorDaRodada+=1
            turno+=1
            RodarTurno(dadosDaPartida,numeroDeJogadores, jogadorDaRodada, turno, pontosJogador)
        else:
            pass
        if numeroDePegadas == 0:
            pass
        else: 
            coresComPegadas = VerificarCorDadoComPegada(resultadoDados, ordemDados)
            del ordemDados[0:2]
            ordemDados = random.shuffle(ordemDados)
            ordemDados = coresComPegadas.extend(ordemDados)

        
        




    jogadorDaRodada+=1
    turno+=1
    RodarTurno(dadosDaPartida,numeroDeJogadores, jogadorDaRodada, turno, pontosJogador)
    return dadosDaPartida, nomeJogador, turno, pontosJogador




def ordemDados(noOnibus = False):
    if noOnibus == False:
        dados = ['verde','verde','verde','verde','verde','verde','amarelo','amarelo','amarelo','amarelo','vermelho','rosa','branco', 'papai noel']
    else:
        dados = ['verde','verde','verde','verde','verde','verde','amarelo','amarelo','amarelo','amarelo','vermelho','rosa','branco', 'papai noel', 'onibus']
    dados = random.shuffle(dados)
    return dados

def rolarDados(ordemDados):
    '''
    cerebro = 1
    pegada = 2
    tiro = 3
    dois cerebros = 4
    dois tiros = 5
    capacete = 6
    energetico =7
    '''
    mapeamentoValores = {
    1: "cerebro",
    2: "pegada",
    3: "tiro",
    4: "dois cerebros",
    5: "dois tiros",
    6: "capacete",
    7: "energetico"
}
    valoresDadosIniciais =[]
    dadoVerde = [1,1,1,2,3,3] #'cerebro','cerebro','cerebro','pegada','tiro','tiro'
    dadoAmarelo = [1,1,2,2,3,3] #'cerebro','cerebro','pegada','pegada','tiro','tiro'
    dadoVermelho = [1,2,2,3,3,3] #'cerebro', 'pegada', 'pegada','tiro','tiro','tiro'
    dadoRosa = [1,2,2,2,3,3] #'cerebro', 'pegada','pegada', 'pegada','tiro','tiro'
    dadoBranco = [2,2,2,3,4,5] #'pegada','dois cerebros','dois tiros','capacete','energetico'
    dadoPapaiNoel = [1,2,3,4,6,7] #'cerebro'. 'pegada', 'tiro', 'dois cerebros', 'capacete', 'energetico'
    dadoOnibus = []
    if (len(ordemDados)<3):
        print("Não há mais dados para rolar. fim do turno")
        return 0
    ordemDados = ordemDados
    dadosIniciais = [ordemDados[0],ordemDados[1],ordemDados[2]]
    print(f'Voce tirou os seguintes dados:{dadosIniciais[0]},{dadosIniciais[1]} e {dadosIniciais[2]} ')
    for corDado in ordemDados:
        if(corDado) == 'verde':
            dadoVerde = random.shuffle(dadoVerde)
            valoresDadosIniciais.append(dadoVerde[0])
        elif(corDado) == 'amarelo':
            dadoAmarelo = random.shuffle(dadoAmarelo)
            valoresDadosIniciais.append(dadoAmarelo[0])
        elif(corDado) == 'vermelho':
            dadoVermelho = random.shuffle(dadoVermelho)
            valoresDadosIniciais.append(dadoVermelho[0])
        elif(corDado) == 'rosa':
            dadoBranco = random.shuffle(dadoBranco)
            valoresDadosIniciais.append(dadoBranco[0])
        elif(corDado) == 'branco':
            dadoRosa = random.shuffle(dadoRosa)
            valoresDadosIniciais.append(dadoRosa[0])
        elif(corDado) == 'papai noel':
            dadoPapaiNoel = random.shuffle(dadoPapaiNoel)
            valoresDadosIniciais.append(dadoPapaiNoel[0])
        elif(corDado) == 'onibus':
            pass
    AnimacaoRolando()


    for numero in valoresDadosIniciais:
        resultados = mapeamentoValores[numero]
    
    return resultados, ordemDados 
    
def VerificarPontos(resultadoDados, ordemDados):
    ordemDados = ordemDados
    numeroDePegadas = 0
    numeroDeTiros = 0
    numeroDeCerebros = 0
    for i in resultadoDados:
        if i == 'cerebro':
            numeroDeCerebros += 1
        elif i == 'tiro':
            numeroDeTiros += 1
        elif i == 'pegada':
            numeroDePegadas += 1
        elif i == 'dois cerebros':
            numeroDeCerebros += 2
        elif i == 'dois tiros':
            numeroDeTiros += 2
        elif i == 'capacete':
            numeroDeTiros -= 1
        if i == 'pegada' and ordemDados[i] == 'verde':
            numeroDePegadas -= 1
            numeroDeCerebros += 1
    return(numeroDePegadas, numeroDeCerebros, numeroDeTiros)

def VerificarCorDadoComPegada(resultadoDados, ordemDados):
    numeroDado = 0
    coresComPegadas = []
    for i in resultadoDados:
        if i == 'pegada':
            coresComPegadas.append(ordemDados[numeroDado])
        numeroDado += 1
    return coresComPegadas

# funcoes complementares
def AnimacaoRolando(duracao=3, intervalo=0.3):
    """
    Mostra uma pequena animação no terminal da palavra 'rolando...'
    com os pontos variando (. .. ... ....) e repetindo por 'duracao' segundos.
    """
    pontos = [".", "..", "...", "...."]
    inicio = time.time()
    
    while time.time() - inicio < duracao:
        for p in pontos:
            print(f"Rolando{p}   ", end="\r", flush=True)
            time.sleep(intervalo)
    print("Rolando.... pronto!   ")

def LimparTerminal():
    if (sys.platform.startswith('win')):
        os.system('cls')
    else: 
        os.system('clear')


main()