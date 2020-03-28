

"Criando uma classe"
class objetos():
    
    "Criando Comportamento Da Classe"
    def __init__(self,local,operador):
        self.local = local
        self.operador = operador
    
    def aquecer(self):
        return True
  
    
    def borrifar(self,vezes):
        print (vezes)
        return 
  
    
    def ventilar (self,velocidade):
        return True
  
    
    def exaustao ( self, velocidade):
        return True
  



Moradores = ['Java','SqlServer', 'Delphi','Python']
Locais = ['Sala','Quarto','Cozinha','Banheiro','Garagem']
senhas = []

print("Rodando o sistema pela primeira vez")
print("A seguir defina seu nomoe de usuário")


usuario = input("Insira seu Nome ")
print("Olá  " + usuario)


print("A seguir defina uma senha ")
senha = input("Insira sua senha")
Moradores.append(senha)
print(senhas)
Moradores.append(usuario)

UserAccess = usuario
if UserAccess == Moradores[0] and senha == senhas [0]:
    print("Acesso Liberado")
else:
    print("Acesso Negado")
                                           