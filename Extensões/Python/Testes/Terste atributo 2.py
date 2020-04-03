#código 3 - exemplo de classe com itens fortemente privado
class PrimeiraClassFortementePrivada():
    def __init__(self):
        self.__atributoFrotementePrivado = 520741
 
    def __primeiroMetodoFrotementePrivado(self):
        print("método fortemente privado")
        
        
        
        
#código 4 - acessando os itens fortemente privados
# utilizando o método padrão de aceso.
 
p2 = PrimeiraClassFortementePrivada()
# erro loco
p2._primeiroMetodoPrivado()
# AttributeError: 'PrimeiraClassFortementePrivada'
# object has no attribute '_primeiroMetodoPrivado'
 
print(p2.__atributoFrotementePrivado)
# AttributeError: 'PrimeiraClassFortementePrivada' 
# object has no attribute '__atributoFrotementePrivado       