from cliente import Cliente
from datetime import datetime

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[c] Nova conta
[l] Listar contas
[u] Novo usuário
[q] Sair

=> """
clientes = []

def buscar_cliente(cpf=None, agencia=None, conta=None):
    global clientes
    if cpf is not None:
        for i, cliente in enumerate(clientes):
            if cliente.cpf == cpf:
                return i
    elif agencia is not None and conta is not None:
        for i, cliente in enumerate(clientes):
            if cliente.agencia == agencia and len(cliente._contas) >= conta:
                return i
    return None


while True:
    opcao = input(menu)
    if opcao == "d":
        agencia = input("Agência: ")
        conta = int(input("Conta: "))
        cliente = buscar_cliente(agencia=agencia, conta=conta)
        if cliente is not None:
            valor = float(input("Informe o valor do depósito: "))
            print(clientes[cliente]._contas[conta - 1].depositar(valor))
            continue
        print("Conta não encontrada")
    elif opcao == "s":
        agencia = input("Agência: ")
        conta = int(input("Conta: "))
        cliente = buscar_cliente(agencia=agencia, conta=conta)
        if cliente is not None:
            valor = float(input("Informe o valor do saque: "))
            print(clientes[cliente]._contas[conta - 1].sacar(valor=valor))
            continue
        print("Conta não encontrada")
    elif opcao == "e":
        agencia = input("Agência: ")
        conta = int(input("Conta: "))
        cliente = buscar_cliente(agencia=agencia, conta=conta)
        if cliente is not None:
            print(clientes[cliente]._contas[0].imprimir_extrato())
            continue
        print("Conta não encontrada")
    elif opcao == 'c':
        cpf = str(input("CPF: "))
        cliente = buscar_cliente(cpf=cpf)
        if cliente is not None:
            print(clientes[cliente].criar_conta())
            continue
        print("Cliente não encontrado")
    elif opcao == 'l':
        cpf = str(input("CPF: "))
        cliente = buscar_cliente(cpf=cpf)
        if cliente is not None:
            for conta in range(0, len(clientes[cliente]._contas)):
                print(f"Ag: {clientes[cliente].agencia} C/C: {conta + 1}")
    elif opcao == 'u':
        cpf = str(input("CPF (somente numeros): "))
        cliente = buscar_cliente(cpf=cpf)
        if cliente is not None:
            print("Cliente já cadastrado")
            continue
        nome = input("Nome: ")
        while True:
            nascimento = input("Data de Nascimento (ddmmyyyy): ")
            try:
                nascimento = datetime.strptime(nascimento, "%d%m%Y")
                break
            except:
                print("Data inválida, por favor insira a data no formato ddmmyyyy")
        logradouro = input("Logradouro: ")
        nro = input("Número: ")
        bairro = input("Bairro: ")
        cidade = input("Cidade: ")
        uf = input("UF (sigla): ")
        clientes.append(Cliente(nome, nascimento, cpf, logradouro, nro, bairro, cidade, uf))
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
