# Linguagem de Programação II
# AC03 ADS-EaD - Banco
#
# Email: ermirio.bonfim@aluno.faculdadeimpacta.com.br

from typing import Union, List, Dict

Number = Union[int, float]


class Cliente():
    """
    Classe Cliente do Banco.

    possui os atributos PRIVADOS:*OK
    - nome, *OK
    - telefone,*OK
    - email.*OK
    caso o email não seja válido (verificar se contém o @) gera um ValueError,
    caso o telefone não seja um número inteiro gera um TypeError
    """

    def __init__(self, nome: str, telefone: int, email: str):
        self.__nome = nome
        self.__telefone = telefone
        self.__email = email

    def get_nome(self):
        return self.__nome

    def get_telefone(self):
        return self.__telefone

    def set_telefone(self, novo_telefone: int):
        """
        Mutador do atributo telefone, caso não receba um número,
        gera um TypeError
        """
        if type (novo_telefone) is not int:  
            raise TypeError ("Você não digitou um número")
        self.__telefone = novo_telefone

    def get_email(self):
        return self.__email

    def set_email(self, novo_email: str):
        """
        Mutador do atributo Email, caso não receba um email válido
        (contendo o @), gera um ValueError.
        """
        if '@' in novo_email:
            self.__email = novo_email 
        else:
            raise ValueError("Digite um e-mail válido")


class Banco():
    """
    A classe Banco deverá receber um nome em sua construção e deverá
    implementar os métodos:
    - abre_conta(): abre uma nova conta, atribuindo o numero da conta em ordem
    crescente a partir de 1 para a primeira conta aberta.
    - lista_contas(): apresenta um resumo de todas as contas do banco

    DICA: crie uma variável interna que armazene todas as contas do banco
    DICA2: utilze a variável acima para gerar automaticamente o número das
    contas do banco
    """

    def __init__(self, Banco: str):
        self.__Banco = "nome"
        self.__contas = []  #Variável para armazenar as contas
    
    def get_nome(self):
        return self.__Banco
        """Acessor do Atributo Nome."""

    def abre_conta(self, clientes: List[Cliente], saldo_ini: Number):
        self.__cliente = clientes
        self.__saldo_ini = saldo_ini
        
        if saldo_ini < 0:
            raise ValueError("Saldo Insuficiente")
        else:
            self.__saldo_ini = saldo_ini
            self.__contas.append(len(self.__contas)+1)   
            
        
            

            ('O saldo Inicial Deverá ser maior que zero')

        """
        Método para abertura de nova conta, recebe os clientes
        e o saldo inicial.
        Caso o saldo inicial seja menor que 0 devolve um ValueError
        """

    def lista_contas(self):
        """Retorna a lista com todas as contas do banco."""
        return self.__contas

class Conta():
    """
    Classe Conta:
    - Todas as operações (saque e deposito, e saldo inicial) devem aparecer
    no extrato como tuplas, exemplo ('saque', 100), ('deposito', 200) etc.
    - Caso o saldo inicial seja menor que zero deve lançar um ValueError
    - A criação da conta deve aparecer no extrato com o valor
    do saldo_inicial, exemplo: ('saldo_inicial', 1000)

    DICA: Crie uma variável interna privada para guardar as
    operações feitas na conta
    """

    def __init__(self, clientes: List[Cliente],
                 numero_conta: int,
                 saldo_inicial: Number):
        self.clientes = clientes
        

    def get_clientes(self) :
        '''
        Acessor para o atributo clientes
        '''
        return self.__clientes

    def get_saldo(self) :
        
        '''
        Acessor para o atributo saldo
        '''
        return self.__saldo
    

    def get_numero(self) :
        '''
        Acessor para o atributo numero
        '''
        return self.__numero_conta

    def saque(self, valor: Number) :
        '''
        Método de saque da classe Conta, operação deve aparecer no extrato

        Caso o valor do saque seja maior que o saldo da conta,
        deve retornar um ValueError, e não efetuar o saque
        '''
        pass

    def deposito(self, valor: Number):
        '''
        Método depósito da classe Conta, operação deve aparecer no extrato
        '''
        pass

    def extrato(self) -> List[Dict[str, Number]]:
        '''
        Retorna uma lista com as operações (Tuplas) executadas na Conta
        '''
        pass
