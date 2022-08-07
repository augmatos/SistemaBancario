from banco import Banco
from cliente import Cliente
from conta import ContaCorrente, ContaPoupanca

banco = Banco()

cliente_1 = Cliente('Augusto', 23)
cliente_2 = Cliente('José', 19)
cliente_3 = Cliente('Anna', 22)

conta_1 = ContaPoupanca(11111, 125976, 0)
conta_2 = ContaCorrente(22222, 486521, 0)
conta_3 = ContaPoupanca(12120, 875261, 0)

cliente_1.inserir_conta(conta_1)
cliente_2.inserir_conta(conta_2)
cliente_3.inserir_conta(conta_3)

banco.inserir_cliente(cliente_1)
banco.inserir_conta(conta_1)

banco.inserir_cliente(cliente_2)
banco.inserir_conta(conta_2)

banco.inserir_cliente(cliente_3)
banco.inserir_conta(conta_3)

if banco.autenticar(cliente_2):
    cliente_1.conta.depositar(0)
    cliente_1.conta.sacar(20)
else:
    print('Cliente não autenticado.')

print('####################')

if banco.autenticar(cliente_2):
    cliente_2.conta.depositar(0)
    cliente_2.conta.sacar(20)
else:
    print('Cliente não autenticado.')

print('####################')

if banco.autenticar(cliente_3):
    cliente_3.conta.depositar(0)
    cliente_3.conta.sacar(20)
else:
    print('Cliente não autenticado.')
