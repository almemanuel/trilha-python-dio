class Endereco:
    def __init__(self, logradouro, nro, bairro, cidade, uf):
        self.logradouro = logradouro
        self.nro = nro
        self.bairro = bairro
        self.cidade = cidade
        self.uf = uf


    def __str__(self):
        return f"{self.logradouro}, {self.nro} - {self.bairro} - {self.cidade}/{self.uf}"