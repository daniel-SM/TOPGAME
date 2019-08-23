
from PRCRND_ITNSprsngm import procurandoItens

def venderItens(itensPerson,moedas):
    item= input("\nNº do item: ")
    
    aux= True
    i= 0
    while(i < len(itensPerson)):
        if(item == itensPerson[i][0]):
            aux= False
            
            moedas+= itensPerson[i][3]
            texto= itensPerson[i][4]
            tipo= itensPerson[i][5]
            
            print("Venda efetuada!")
            print("Você ganhou",itensPerson[i][3],"moedas")
            print("Você tem",moedas,"moedas")
        
            itensPerson.pop(i)
        
            poder= procurandoItens(itensPerson,texto,tipo)
        
        i+= 1
        
    if(aux):
        print("Item não encontrado!")
        itensPerson,moedas,poder= venderItens(itensPerson,moedas)
        
    return itensPerson,moedas,poder,tipo
        
    