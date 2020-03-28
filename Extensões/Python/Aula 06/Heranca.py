
class Frenagem():
    
    def brecar(self):
        print ("pressiona todas as  rodas")
        return 

class carro(frenagem):
    def brecar(self):
        print ("Pressiona duas rodas")
        return    

class trator(Frenagem):
    def brecar(self):
        super().brecar()
        return
    
class moto(Frenagem):
    def brecar(self):
        print("pressiona uma roda")
        return
        
        
        