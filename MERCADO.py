##DK
#
#
import time

from LIMPAR import limpar
from DESEJO import desejoErro
from ITENS import itensAtaque,itensDefesa,itensLife,itensRegener,itensMagia
from MSTRND_ITNS import mostrandoItens
from MSTRND_ITNSprsngm import mostrandoItensPrsngm
from CMPRND_ITNS import comprandoItens
from VENDER_ITNS import venderItens

def mercado(itensPerson,moedas,life,ataque,defesa,lifeRegen,magia):
    
    limpar(100)
    print("\n||-------##-------##------##------||")
    print("||      BEM-VINDO AO MERCADO      ||")
    print("||-------##-------##------##------||")
    time.sleep(1)
    
    print("||      Você tem",moedas,"moedas.")
    print("||--------------------------------||")
    time.sleep(1)
    
    print("\n||--------------------------||")
    print("||   LOJAS                  ||")
    print("||   1. Loja de Armas       ||")
    print("||   2. Loja de Escudos     ||")
    print("||   3. Loja de Poções      ||")
    print("||   4. Loja de Armaduras   ||")
    print("||   5. Loja de Magias      ||")
    print("||   6. Vender Itens        ||")
    print("||   7. Sair                ||")
    print("||--------------------------||")
    
    loja= input("\nNumº da loja: ")
    
    while loja not in ["1","2","3","4","5","6","7"]:
        print("Inválido!")
        loja= input("Numº da loja: ")
    
    limpar(10)
    
    if(loja == "1"):
        print("||--------------------||")
        print("||    LOJA DE ARMAS   ||")
        print("||--------------------||\n")
        
        mostrandoItens(itensAtaque,"ataque")
        desejo= input("\nComprar algum item?\n(S: sim) ou (N: não): ")
        desejo= desejoErro(desejo)
        if(desejo == "s"):
            itensPerson,moedas,ataque= comprandoItens(itensPerson,itensAtaque,moedas,ataque,"ataque",0,True)
    
    elif(loja == "2"):
        print("||--------------------||")
        print("||  LOJA DE ESCUDOS   ||")
        print("||--------------------||\n")
        
        mostrandoItens(itensDefesa,"defesa")
        desejo= input("\nComprar algum item?\n(S: sim) ou (N: não): ")
        desejo= desejoErro(desejo)
        if(desejo == "s"):
            itensPerson,moedas,defesa= comprandoItens(itensPerson,itensDefesa,moedas,defesa,"defesa",1,True)
    
    elif(loja == "3"):
        print("||--------------------||")
        print("||   LOJA DE POÇÕES   ||")
        print("||--------------------||\n")
        
        mostrandoItens(itensLife,"vida a mais")
        desejo= input("\nComprar algum item?\n(S: sim) ou (N: não): ")
        desejo= desejoErro(desejo)
        if(desejo == "s"):
            poder= 0
            itensPerson,moedas,poder= comprandoItens(itensPerson,itensLife,moedas,poder,"vida a mais")
            life+= poder
    
    elif(loja == "4"):
        print("||---------------------||")
        print("||  LOJA DE ARMADURAS  ||")
        print("||---------------------||\n")
        
        mostrandoItens(itensRegener,"vida p/ fase")
        desejo= input("\nComprar algum item?\n(S: sim) ou (N: não): ")
        desejo= desejoErro(desejo)
        if(desejo == "s"):
            itensPerson,moedas,lifeRegen= comprandoItens(itensPerson,itensRegener,moedas,lifeRegen,"vida p/ fase",2,True)
            
    elif(loja == "5"):
        print("||--------------------||")
        print("||   LOJA DE MAGIAS   ||")
        print("||--------------------||\n")
        
        mostrandoItens(itensMagia,"ataque extra")
        desejo= input("\nComprar algum item?\n(S: sim) ou (N: não): ")
        desejo= desejoErro(desejo)
        if(desejo == "s"):
            poder= 0
            itensPerson,moedas,poder= comprandoItens(itensPerson,itensMagia,moedas,poder,"ataque extra")
            magia+= poder
            
    elif(loja == "6"):
        print("||--------------------||")
        print("||    VENDER ITENS    ||")
        print("||--------------------||\n")
        
        if(len(itensPerson) > 0):
            mostrandoItensPrsngm(itensPerson)
            desejo= input("\nVender algum item seu?\n(S: sim) ou (N: não): ")
            desejo= desejoErro(desejo)
            if(desejo == "s"):
                itensPerson,moedas,poder,tipo= venderItens(itensPerson,moedas)
                if(tipo == 0):
                    ataque= poder
                elif(tipo == 1):
                    defesa= poder
                elif(tipo == 2):
                    lifeRegen= poder
        else:
            print("\nVOCÊ NÃO TEM ITENS!!!\n")
            desejo= input("Sair do mercado?\n(S: sim) ou (N: não): ")
            desejo= desejoErro(desejo)
            if(desejo == "s"):
                return itensPerson,moedas,life,ataque,defesa,lifeRegen,magia
    
    elif(loja == "7"):
        print("||--------------------||")
        print("||        SAIR        ||")
        print("||--------------------||\n")
        
        print("Sair do mercado!\n")
        desejo= input("Quer mesmo sair?\n(S: sim) ou (N: não): ")
        desejo= desejoErro(desejo)
        if(desejo == "s"):
            print("\nSaindo do mercado...")
            return itensPerson,moedas,life,ataque,defesa,lifeRegen,magia      
    else:
        print("Inválido!")
        limpar(100)
        itensPerson,moedas,life,ataque,defesa,lifeRegen,magia= mercado(itensPerson,moedas,life,ataque,defesa,lifeRegen,magia) 

    if(desejo == "n"):
        limpar(100)
        itensPerson,moedas,life,ataque,defesa,lifeRegen,magia= mercado(itensPerson,moedas,life,ataque,defesa,lifeRegen,magia)

    return itensPerson,moedas,life,ataque,defesa,lifeRegen,magia




