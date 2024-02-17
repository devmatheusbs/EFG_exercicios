class ContaBancaria:
    lista_clientes = []
    def __init__(self, nome, cpf, data_nascimento, cod_conta, senha_conta, saldo=0.0) -> None:
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.cod_conta = cod_conta
        self.senha_conta = senha_conta
        self.saldo = saldo        
        ContaBancaria.lista_clientes.append(self)    
    def deposito(self, valor):
        self.saldo += valor
        print(f'Deposito efetuado, saldo atual: R$ {self.saldo}')
    def saque(self, valor, senha):
        if self.saldo >= float(valor) and senha == self.senha_conta:
            self.saldo -= float(valor)
            print(f'Saque no valor de R$ {float(valor)} efetuado com sucesso, saldo restante: R$ {self.saldo}')
        else:
            print(f'Saldo insuficiente')
    def transferencia(self, valor, conta_destino, senha):
        if self.saldo >= float(valor) and senha == self.senha_conta:
            self.saldo -= float(valor)
            conta_destino.saldo += float(valor)
            print(f'Transferência efetuado com sucesso, saldo restante: R$ {self.saldo}')
        else:
            print(f'Saldo insuficiente') 
    def extrato(self):
        print(f'Sr.(a) {self.nome} seu saldo atual é de R${self.saldo} ')
         
client01 = ContaBancaria('Matheus Barbosa', '000.000.000-00', '08/12/1994', '58001', '0000')
client02 = ContaBancaria('Prof. Heberson', '111.111.111-11', '01/01/1975','59001', '1111')

while True:
    print('*'*15, 'Seja bem vindo ao Banco Master', '*'*15)
    conta = str(input('Digite o número da sua conta: '))
    senha = str(input('Digite a senha da sua conta: '))
    cliente_autenticado = None
    for cliente in ContaBancaria.lista_clientes:
        if cliente.cod_conta == conta and cliente.senha_conta == senha:
            print(f'Seja bem vindo Sr.(a) {cliente.nome}')
            cliente_autenticado = cliente
            while True:
                servico = input('Que serviço deseja realizar? [S]aque, [D]eposito, [T]ransferência, [E]xtrato? ')
                if servico.lower() == 's':
                    valor_saque = float(input('Digite o valor do saque'))
                    senha = str(input('Digite sua senha: '))
                    cliente_autenticado.saque(valor_saque,senha)
                elif servico.lower() == 'd':
                    valor_deposito = float(input('Digite o valor do deposito'))
                    cliente_autenticado.deposito(valor_deposito)
                elif servico.lower() == 't':
                    valor_transferencia = float(input('Digite o valor da transferencia: '))
                    conta_destino_transferencia = str(input('Digite a conta destino: '))
                    for cliente_transferencia in ContaBancaria.lista_clientes:
                        if cliente.cod_conta == conta_destino_transferencia:
                            conta_destino_transferencia = cliente_transferencia                      
                    senha = str(input('Digite sua senha: '))
                    cliente_autenticado.transferencia(valor_transferencia, cliente_transferencia, senha)                
                elif servico.lower() == 'e':
                    cliente_autenticado.extrato()
                elif servico.lower() == 'x':
                    break
                else:
                    'Caractére inválido'
                
        else:
            print('Conta ou Senha incorreta.')