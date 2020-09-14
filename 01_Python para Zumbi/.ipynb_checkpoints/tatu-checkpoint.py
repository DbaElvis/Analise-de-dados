class Cliente:
    def __init__(self, nome, celular):
        self.nome = nome
        self.celular = celular
        
class Conta:
    def __init__(self, clientes, numero,  saldo = 0):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        
    def resumo(self):
        print('N da conta: %s - Saldo: %10.2f ' %(self.numero, self.saldo))
        
    def sacar(self, valor):
        if self.saldo >= valor:   
            self.saldo -= valor 
            
    def depositar(self, valor):   
            self.saldo += valor   
            
