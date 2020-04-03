#código 1 - exemplo de classe com itens fracamente privados
class PrimeiraClassFracamentePrivada():
    def __init__(self):
        self._atributoFracamentePrivado = 520741
 
    def _primeiroMetodoFracamentePrivado(self):
        print("método fracamente privado")
        
        
        #código 2 - exemplo de classe com itens fracamente privados
p1 = PrimeiraClassFracamentePrivada()
 
p1._primeiroMetodoFracamentePrivado()
# método fracamente privado
print(p1._atributoFracamentePrivado)
# 520741