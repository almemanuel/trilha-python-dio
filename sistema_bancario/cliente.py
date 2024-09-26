from endereco import Endereco
from conta_corrente import ContaCorrente

AGENCIA = "0001"

class Cliente():
    def __init__(self, nome, nascimento, cpf, logradouro, nro, bairro, cidade, uf):
        self.nome = nome
        self.nascimento = nascimento
        self.cpf = cpf
        self.endereco = Endereco(logradouro, nro, bairro, cidade, uf)
        self._contas = []
        self.agencia = AGENCIA


    def criar_conta(self):
        self._contas.append(ContaCorrente())
        return f"Conta criada com sucesso!\nAg {AGENCIA} C/C {len(self._contas)}"