#DS  
#
import time
import random

from DANO import calcAtaque
from DESEJO import desejoErro
from SUSPENSE import suspense
     
def batalha(life,lifeInim,ataque,ataqueInim,defesa,defesaInim,magia,moedas,i):

    if(ataque-defesaInim <= 0) and (ataqueInim-defesa <= 0):
        print('''
        ||------------------------||
        ||         EMPATE         ||
        ||------------------------||
        ||   Você e seu inimigo   ||
        ||  tem ataque e defesa   ||
        ||      equivalentes!     ||
        ||------------------------||
        ''')
        time.sleep(1)
        i-= 1
        return life,magia,moedas,i,False
    
    jogs= 0
    jogsInim= 0
    
    while(life > 0)and(lifeInim > 0):
        
        sorteio= random.choice([1,2])
        
        if(jogs > 1):
            jogs= 0
            jogsInim+= 1
            if(jogsInim > 1):
                print("\nSeu inimigo novamente!\n")
            print("\nSeu inimigo está atacando!")
            suspense(0.3)
            life,fim= calcAtaque(1,life,ataqueInim,defesa)
            if(fim == True):
                break
                        
        if(jogsInim > 1):
            jogsInim= 0
            jogs+= 1
            
            if(jogs > 1):
                print("\nVocê novamente!")
            
            print("\n||------------------||")
            print("||     Sua vez!     ||")
            print("||------------------||")
            print("||   AÇÕES:         ||")
            print("||   1. Atacar      ||")
            print("||   2. Usar Magia  ||")
            print("||   3. Defender    ||")
            print("||   4. Fugir       ||")
            print("||------------------||")
        
            acao= input("Ação: ")
        
            while acao not in ["1", "2", "3", "4"]:
                print("Inválido!")
                acao= input("Ação: ")
                     
            if(acao == "1"):
                print("\nVocê está atacando!")
                suspense(0.3)
                lifeInim,fim= calcAtaque(0,lifeInim,ataque,defesaInim)
            elif(acao == "2"):
                print("\nVocê está atacando!")
                print("Sua magia é",magia)
                suspense(0.3)
                lifeInim,fim= calcAtaque(0,lifeInim,ataque,defesaInim,magia)
                magia= 0
            elif(acao == "3"):
                sorteio= 2
            elif(acao == "4"):
                desejo= input("\nQuer mesmo fugir?\n(S: sim) ou (N: não): ")
                desejo= desejoErro(desejo)
                if(desejo == "s"):
                    i-= 1
                    print("\n||---------------------------||")
                    print("||           FUGIU           ||")
                    print("||---------------------------||")
                    print("||  Você fugiu da batalha!   ||")
                    print("||  Você perdeu 100 moedas!  ||")
                    print("||---------------------------||")
                    if(moedas > 100):
                        moedas-= 100
                    else:
                        moedas= 0
                    print("||  Você tem",moedas,"moedas")
                    print("||---------------------------||")
                    
                    return life,magia,moedas,i,True
            if(fim == True):
                break
        
        if(sorteio == 1):
            jogsInim= 0
            jogs+= 1
            if(jogs > 1):
                print("\nVocê novamente!")
        
            print("\n||------------------||")
            print("||     Sua vez!     ||")
            print("||------------------||")
            print("||   AÇÕES:         ||")
            print("||   1. Atacar      ||")
            print("||   2. Usar Magia  ||")
            print("||   3. Defender    ||")
            print("||   4. Fugir       ||")
            print("||------------------||")
                
            acao= input("\nAção: ")
        
            while acao not in ["1", "2", "3", "4"]:
                print("Inválido!")
                acao= input("\nAção: ")        
            if(acao == "1"):
                print("\nVocê está atacando!")
                suspense(0.3)
                lifeInim,fim= calcAtaque(0,lifeInim,ataque,defesaInim)
            elif(acao == "2"):
                print("\nVocê está atacando!")
                print("Sua magia é",magia)
                suspense(0.3)
                lifeInim,fim= calcAtaque(0,lifeInim,ataque,defesaInim,magia)
                magia = 0
            elif(acao == "3"):
                sorteio= 2
                fim = False
            elif(acao == "4"):
                desejo= input("\nQuer mesmo fugir?\n(S - sim) ou (N - não): ")
                desejo= desejoErro(desejo)
                if(desejo == "s"):
                    i-= 1
                    print("\n||---------------------------||")
                    print("||           FUGIU           ||")
                    print("||---------------------------||")
                    print("||  Você fugiu da batalha!   ||")
                    print("||  Você perdeu 100 moedas!  ||")
                    print("||---------------------------||")
                    if(moedas > 100):
                        moedas-= 100
                    else:
                        moedas= 0
                    print("||  Você tem",moedas,"moedas")
                    print("||---------------------------||")

                    return life,magia,moedas,i,True
            if(fim == True):
                break

        if(sorteio == 2):
            jogs= 0
            jogsInim+= 1
            if(jogsInim > 1):
                print("\nSeu inimigo novamente!")
            print("\nSeu inimigo está atacando!")
            suspense(0.3)
            life,fim= calcAtaque(1,life,ataqueInim,defesa)
            if(fim):
                break
                   
    return life,magia,moedas,i,True

# batalha(life,lifeInim,ataque,ataqueInim,defesa,defesaInim,magia,moedas)
#batalha(100,100,140,120,90,60,0,100,1)

