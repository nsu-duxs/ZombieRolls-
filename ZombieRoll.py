import os
import sys
import random
import time 

def main():
    AbrirMenuIncial()


main()


def AbrirMenuIncial():
    print("Zombie Roll \n")
    numeroDeJogadores = SelecionarNumeroDeJogadores()
    print(f"O numero selecionado foi de {numeroDeJogadores}")
    IniciarJogo(numeroDeJogadores)


def SelecionarNumeroDeJogadores():
        print("Selecione o numero de jogadores:\n")
        numeroDeJogadores = input()
        if (numeroDeJogadores.isDigit() == False):
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
    dadosDaPartida = {}
    for i in range(numeroDeJogadores):
        nomeJogador = input(f'Digite o nome do jogador numero {i +1}')
        dadosDaPartida[nomeJogador] = []
    RodarTurno(dadosDaPartida, nomeJogador, turno)

def RodarTurno(dadosDaPartida, nomeJogador, turno):
    print(f"Turno: {turno}")
    print("Rolagem de "+nomeJogador)
    ordemDados = ordemDados()
    dadosIniciais = [ordemDados[0],ordemDados[1],ordemDados[2]]
    del ordemDados[0:2]
    print("-----------------------")

    return ordemDados




def ordemDados(noOnibus = False):
    dados = ['verde','verde','verde','verde','verde','verde','amarelo','amarelo','amarelo','amarelo','vermelho','rosa','branco', 'papai noel']
    dados = random.shuffle(dados)
    return dados

def rodarDados(ordemDados):
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
    ordemDados = ordemDados
    dadosIniciais = [ordemDados[0],ordemDados[1],ordemDados[2]]
    del ordemDados[0:2]
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
    AnimacaoRolando()


    for numero in valoresDadosIniciais:
        resultados = mapeamentoValores[numero]
    
    

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
    if (sys.platform.startwith('win')):
        os.system('cls')
    else: 
        os.system('clear')