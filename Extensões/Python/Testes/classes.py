class contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.alterar_telefone(telefone)
        self.email = email
    
    
    def exibir_telefone(self):
        return self.telefone 
    
    def alterar_telefone(self, novo_numero):
        print("Chamando o altera telefone")
        if not novo_numero.isdigit():
            raise TypeError("Digite apenas os numeros")
        self.telefone = novo_numero
    
    def enviar_email(self):
        return 'Enviando email para {}'.format(self.email)        