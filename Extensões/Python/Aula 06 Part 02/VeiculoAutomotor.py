
class Frenagem():
    
    def brecar(self):
        acao  = 'brecar com duas rodas'
        print (acao)
        return acao


class ignicao():
    def ligar(self):
        return "vrum"   

class VeiculoAutomotor(Frenagem,ignicao):
    
    def buzinar(self,vezes):
        return vezes
    
    def brecar(self):
        acao = "breca com 4 rodas"
        return acao
    
      
    
    
####INSTANCINDO 

fusca = VeiculoAutomotor()
print(fusca.brecar())



        
 #####################################################################       