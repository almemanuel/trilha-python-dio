from conta_corrente import ContaCorrente

conta = ContaCorrente()
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

while True:
    opcao = input(menu)
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        print(conta.depositar(valor))
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        print(conta.sacar(valor))
    elif opcao == "e":
        print(conta.imprimir_extrato())
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
