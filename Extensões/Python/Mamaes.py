


listamulheres = []
#Definido uma classe mãe
class mae:
    def __init__(self,nome,idade,estadocivil,quantfilhos):
        self.nome = nome
        self.idade=idade
        self.estadocivil = estadocivil
        self.quantfilhos = quantfilhos
    def cuidarfilhos(self):
        return '{} Cuidando do filho'.format(self.nome)
    
    def filhopracreche(self):
        return '{} Mandou o filho pra creche'.format(self.nome)
    
    def fazercomida(self):
        return '{} Fazendo comida'.format(self.nome)
    


class Mulheres(mae):
        def __init__(self, nome, idade, estadocivil, quantfilhos):
            super().__init__(nome, idade, estadocivil, quantfilhos)
 
def emcadastro():
        NovoCadastro='Sim'
        ConfirNovoCadastro = input('Fazer Novo Cadastro ? ')
        if ConfirNovoCadastro == NovoCadastro:
            mulher01=Mulheres
         
            mulher01=[input('nome'),input('Idade'),input("estado"),input('Filhos')]
            print('Nome: ',mulher01.nome)
            print('Idade: ',mulher01.idade)
            print('Estad0 Civil: ',mulher01.estadocivil)
            print('Quantidade Filhos ' ,mulher01.quantfilhos)
            print(mulher01.filhopracreche())
            print(mulher01.fazercomida())
            print(mulher01.cuidarfilhos())
        else:
            op2 = input('Cancelar Cadastro')
            if op2=='sim':
                final()
            else:
                emcadastro()           
def final():
    pass


def main ():    
    emcadastro()
    final()
    

if __name__ == "__main__":
    main()  





       