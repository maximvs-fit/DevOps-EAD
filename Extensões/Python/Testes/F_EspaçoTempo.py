#*******// FUNÇÃO PARA CÁLCULO DE VELOCIDADE ESPAÇO TEMNPO//*****#

def Velocidade ( espaco,tempo):
    Vm = espaco / tempo
    return Vm

E= int (input("Qual é o valor do espaço? "))
T= int (input ("Qual é o o valor do tempo? ")) 
VM= Velocidade(E,T)
print('Velocidade Média é :',VM)

