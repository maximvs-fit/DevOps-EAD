


class ignicao():
    def ligar(self):
        return "vrum"
      

class Frenagem():
    
    def brecar(self):
        acao  = 'brecar com duas rodas'
        print (acao)
        return acao

class VeiculoAutomotor(Frenagem,ignicao):
    
    def buzinar(self,vezes):
        return vezes
    
    def brecar(self):
        return super().brecar()
    
        
    
    
####INSTANCINDO 

fusca = VeiculoAutomotor()
print (fusca.brecar())


        
 #####################################################################       