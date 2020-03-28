# Linguagem de Programação II
# Atividade Contínua 02 - Classes e Herança
#
# e-mail: ermirio.bonfim@aluno.faculdadeimpacta.com.br


"""
Implementar aqui as cinco classes filhas de Mamifero ou Reptil,
de acordo com o caso, conforme dado no diagrama apresentado no padrão UML.

Os atributos específicos de cada classe filha devem ser recebidos
como parâmetros no momento da criação, a única exceção é o número de vidas
do gato, que sempre começa em 7.

Os métodos de cada classe filha devem sempre RETORNAR uma string
no seguinte formato '<nome do animal> <método em questão no gerúndio>'
Sem nenhuma pontuação, conforme os exemplos a seguir.

Exemplo:
método trocar_pele() retorna '<nome> trocando de pele'
método dormir() retorna '<nome> dormindo'
método miar() retorna '<nome> miando'
Onde <nome> é o nome dado para cada animal (o valor atributo nome de
cada instância, não o nome da classe)

"""


class Reptil:
    """
    Classe mãe - não deve ser editada
    """
    def __init__(self, nome, cor, idade):
        self.nome = nome
        self.cor = cor
        self.idade = idade

    def tomar_sol(self):
        return '{} tomando sol'.format(self.nome)

    def botar_ovo(self):
        if self.idade > 2:
            return '{} botou um ovo'.format(self.nome)
        else:
            return '{} ainda não atingiu maturidade sexual'.format(self.nome)

class Mamifero:
    """
    Classe mãe - não deve ser editada
    """
    def __init__(self, nome, cor_pelo, idade, tipo_pata):
        self.nome = nome
        self.cor_pelo = cor_pelo
        self.idade = idade
        self.tipo_pata = tipo_pata

    def correr(self):
        return '{} correndo'.format(self.nome)

    def mamar(self):
        if self.idade <= 1:
            return '{} mamando'.format(self.nome)
        else:
            return '{} já desmamou'.format(self.nome)

class Camaleao(Reptil):
    """
    Exemplo de solução do exercício:

    Além dos atributos da classe mãe, possui o atributo:
    inseto_favorito, do tipo string.

    Implementa os métodos específicos:
    mudar_de_cor() e comer_inseto()
    """
    def __init__(self, nome, cor, idade, inseto_favorito):
        super().__init__(nome, cor, idade)
        self.inseto_favorito = inseto_favorito

    def mudar_de_cor(self):
        return '{} mudando de cor'.format(self.nome)

    def comer_inseto(self):
        return '{} comendo inseto'.format(self.nome)

class Cavalo(Mamifero):
    """
    Além dos atributos da classe mãe, possui o atributo:
    cor_crina, do tipo string.
    """ 
    """
    Implementa os métodos específicos:
    galopar() e relinchar()
    """
    def __init__(self, nome, cor_pelo, idade, tipo_pata,cor_crina):
        super().__init__(nome, cor_pelo, idade, tipo_pata)
        self.cor_crina = cor_crina
                
    def galopar(self):
        return '{} Galopar'.format(self.nome)
        
    def relinchar(self):
        return '{} relinchar'.format(self.nome)
         
class Cobra(Reptil):
    """
    Além dos atributos da classe mãe, possui o atributo:
    veneno, do tipo booleano.

    Implementa os métodos específicos:
    rastejar() e trocar_pele()
    """
    def __init__(self, nome, cor, idade,veneno):
        super().__init__(nome, cor, idade)
        self.veneno = veneno
        
    def rastejar(self):
        return '{} Rastejando'.format(self.nome)
    
    def trocar_pele (self):
        return '{} trocar de pele'.format(self.nome)
    
class Cachorro(Mamifero):
    """
    Além dos atributos da classe mãe, possui o atributo:
    raca, do tipo string. (raça, porém sem o ç)

    Implementa os métodos específicos:
    latir() e rosnar()
    """
    def __init__(self, nome, cor_pelo, idade, tipo_pata,raca):
        super().__init__(nome, cor_pelo, idade, tipo_pata)
        self.raca = raca
        
    def latir(self):
        return '{} Latindo'.format(self.nome)
    
    def rosnar (self):
        return '{} Rosnando'.format(self.nome)   

class Jacare(Reptil):
    """
    Além dos atributos da classe mãe, possui o atributo:
    num_dentes, do tipo inteiro.

    Implementa os métodos específicos:
    atacar() e dormir()
    """
    def __init__(self, nome, cor, idade, num_dentes):
        super().__init__(nome, cor, idade)
        self.num_dentes = num_dentes
    
    def atacar(self):
        return '{} Atacando'.format(self.nome)
    
    def dormir (self):
        return '{} Dormindo'.format(self.nome)
        
class Gato(Mamifero):
    """
    Além dos atributos da classe mãe, possui o atributo:
    vidas, do tipo inteiro.

    Implementa os métodos específicos:
    miar() e morrer()

    No método morrer, você deve verificar quantas vidas o gato ainda
    tem sobrando, se for igual a zero, retornar:
    '<nome> morreu'
    se ainda houver vidas sobrando, retirar uma vida (que começa em 7),
    e retornar:
    '<nome> tem <vidas> vidas sobrando'
    Onde <vidas> é o número de vidas restantes do gato em questão.
    """
    def __init__(self, nome, cor_pelo, idade, tipo_pata):
        super().__init__(nome, cor_pelo, idade, tipo_pata)
        self.vidas = 7
        
    def miar(self):
        return '{} miando'.format(self.nome)
    
    def morrer(self):
        if self.vidas <= 0:
            return '{} morreu'.format(self.nome)
        else:
            self.vidas = self.vidas -1
            return '{} tem {} vidas'.format(self.nome, self.vidas) 
        

def main ():    
    cachorro = Cachorro("toto", "Preto", 2, "Quadrupede", "SRD")
    print(cachorro.nome)
    print(cachorro.cor_pelo)
    print(cachorro.idade)
    print(cachorro.tipo_pata)
    print(cachorro.raca)
    print(cachorro.latir())
    print(cachorro.rosnar())
    print(cachorro.correr())
    print(cachorro.mamar())
    print("______________________________________")   
        
    cavalo = Cavalo("Pangaré", "Branco", 10, "Quadrupede", "Bicolor")
    print(cavalo.nome)
    print(cavalo.cor_pelo)
    print(cavalo.idade)
    print(cavalo.tipo_pata)
    print(cavalo.cor_crina)
    print(cavalo.galopar())
    print(cavalo.relinchar())
    print(cavalo.correr())
    print(cavalo.mamar())
    print("______________________________________")

    gato = Gato("kiko", "cinza", 3, "Quadrupede")
    print(gato.nome)
    print(gato.cor_pelo)
    print(gato.idade)
    print(gato.tipo_pata)
    print(gato.miar())
    print(gato.morrer())
    print(gato.correr())
    print(gato.mamar())
    print("______________________________________")
    
    camaleao = Camaleao("jorge", "verde", 2, "cupim")
    print(camaleao.nome)
    print(camaleao.cor)
    print(camaleao.idade)
    print(camaleao.inseto_favorito)
    print(camaleao.tomar_sol())
    print(camaleao.botar_ovo())
    print(camaleao.comer_inseto())
    print(camaleao.mudar_de_cor())
    print("______________________________________")

    cobra = Cobra("Gibóia", "Verde e Preta", 5, True)
    print(cobra.nome)
    print(cobra.cor)
    print(cobra.idade)
    print(cobra.veneno)
    print(cobra.tomar_sol())
    print(cobra.trocar_pele())
    print(cobra.rastejar())
    print(cobra.botar_ovo())
    print("______________________________________")

    jacare = Jacare("olga", "Verde", 10, 50)
    print(jacare.nome)
    print(jacare.cor)
    print(jacare.idade)
    print(jacare.num_dentes)
    print(jacare.tomar_sol())
    print(jacare.botar_ovo())
    print(jacare.atacar())
    print(jacare.dormir())

if __name__ == "__main__":
    main()  