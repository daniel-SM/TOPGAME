#-*-coding:utf8;-*-
#qpy:3
#qpy:console

##---------##----------##-----------##

import random,time

from DESEJO       import desejoErro
from BATALHA_Nlog import batalhaNlog
from HISTORY_GAME import Game_History
from CONSULTA_JOGOS import consultaJogos

print('''
||---------##---------##---------##--||
||                                   ||
||  ###### #####  #####              ||
||    ##  ##  ### ##  ##             ||
||    ##  ## # ## #####              ||
||    ##   #####  ##                 ||
||                                   ||
||     ####    #### ###  ### #####   ||
||    ##      ## ## ######## ###     ||
||    ## ### ###### ## ## ## ##      ||
||     #### ###  ## ##    ## #####   ||
||                                   ||
||--------##---------##---------##---||
''')
time.sleep(2)

iniciarZero = True

file = open("storage/emulated/0/qpython/projects3/TOPGAME/Database/dadosGame.txt",'r')
jogoSalvo = eval(file.readline().rstrip())
qtdJogos  = int(file.readline())
file.close()

if(jogoSalvo == True):
    desejo = input("\nContinuar algum progresso salvo?\n(S: sim) ou (N: não): ")
    desejo = desejoErro(desejo)
    
    if(desejo == "s"):
        
        jogoSalvo = consultaJogos(qtdJogos)
        
        print("\nResgatando o progresso...\n")
        time.sleep(1)

        file = open("storage/emulated/0/qpython/projects3/TOPGAME/Database/Dados_Salvos/"+str(jogoSalvo),'r')
        arquivo = file.readlines()
        file.close()
        
        nome        = str(arquivo[1].rstrip())
        fase        = int(arquivo[2].rstrip())
        life        = int(arquivo[3].rstrip())
        lifeRegen   = int(arquivo[4].rstrip())
        ataque      = int(arquivo[5].rstrip())
        defesa      = int(arquivo[6].rstrip())
        magia       = int(arquivo[7].rstrip())
        moedas      = int(arquivo[8].rstrip())
        itensPerson = eval(arquivo[9].rstrip())
        lifeInim    = int(arquivo[10].rstrip())
        ataqueInim  = int(arquivo[11].rstrip())
        defesaInim  = int(arquivo[12].rstrip())
        aumentar    = False
        iniciarZero = False

if(iniciarZero == True):    
    nome = input("\nNome: ")
    
    while(nome == "" or nome == ' '):
        print("Inválido!!!")
        nome = input("\nNome: ")
        
    fase        = 0
    life        = 100
    lifeRegen   = 30
    ataque      = 80
    defesa      = 40
    magia       = 0
    moedas      = 300
    itensPerson = []
    lifeInim    = 70
    ataqueInim  = 50
    defesaInim  = 20
    aumentar    = True

    # História do Jogo
    Game_History(nome)

fim = False

while(fase < 15):
    if(fim):
        break

    if(life > 0):
        if(fase > 0) and (aumentar == True):
            life+= lifeRegen
            lifeInim+= random.choice([5,10])
            ataqueInim+= random.choice([10,10,20])
            defesaInim+= random.choice([10,10,20])
            
            moedas+= 150+(50*(fase-1))
        
        itensPerson,moedas,ataque,defesa,magia,life,lifeRegen,fase,fim,aumentar = batalhaNlog(qtdJogos,nome,itensPerson,lifeRegen,life,lifeInim,magia,ataque,ataqueInim,defesa,defesaInim,moedas,jogoSalvo,fase)
        
    else:
        print("||----------------------------||")
        print("||                            ||")
        print("||  O JOGO ACABOU PRA VOCÊ!!  ||")
        print("||                            ||")
        print("||----------------------------||")
        
        break
    
    fase += 1


