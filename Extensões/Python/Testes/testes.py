armarzena_contas = [
]

while len(armarzena_contas) < 5:
    armarzena_contas.append(len(armarzena_contas)+1)
print(len(armarzena_contas))
print(armarzena_contas)


class telefone:
    def __init__(self,nome):
        self.nome = nome 
    def ligar(self):
        return ("Ligando para {}".format(self.nome))
    
s8 = telefone("Galaxy")

s8.ligar
print(s8.ligar())