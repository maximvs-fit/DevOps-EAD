#Definição de Classe
class VeiculoAutomotor():
   
   #Atributo # Caracteristica # Propriedade
    @property  
    def motorizacao(self):
        return self.__motorizacao 
    
    @motorizacao.setter
    def motorizacao(self,value):
        self.__motorizacao = value  
      
      
        
      #Comportamentos #Ações     
    def ligar(self):
        return True
    
    
    def brecar(self):
        return True
    

#Utilizando as ações
fusca = VeiculoAutomotor()
fusca.ligar() 
fusca.motorizacao = 1000
print (fusca.motorizacao)
fusca.brecar()


    