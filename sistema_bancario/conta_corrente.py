LIMITE_SAQUES = 3
LIMITE_VALOR = 500

class ContaCorrente:
    def __init__(self):
        self._saldo = 0
        self._extrato = ""
        self._n_saques = 0


    def depositar(self, /, valor):
        if valor > 0:
            self._saldo += valor
            self._extrato += f"Depósito: R$ {valor:.2f}\n"
            return f"Depósito realizado\nSaldo atual: R$ {self._saldo:.2f}"
        return "Valor inválido para depósito"


    def sacar(self, *, valor):
        if self._n_saques < LIMITE_SAQUES:
            if valor > 0:
                if valor > self._saldo:
                    return "Saldo insuficiente"
                elif valor > LIMITE_VALOR:
                    return "O valor do saque excede ao limite"
                self._saldo -= valor
                self._extrato += f"Saque: R$ {valor:.2f}\n"
                return f"Saque de R$ {valor:.2f} realizado\nSaldo atual: R$ {self._saldo:.2f}"
            return "Valor inválido para saque"
        return "Número de saques excedido"


    def imprimir_extrato(self):
        return f"""
================ EXTRATO ================
{"Não foram realizadas movimentações" if self._extrato is None else self._extrato}
==========================================
    """