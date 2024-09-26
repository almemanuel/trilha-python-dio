def analise_vendas(vendas):
    # TODO: Calcule o total de vendas e realize a média mensal:
    total_vendas = sum(vendas)
    media_vendas = total_vendas / len(vendas)
    return f"{total_vendas}, {media_vendas:.2f}"

def obter_entrada_vendas():
    # Solicita a entrada do usuário em uma única linha
    entrada = input()
    vendas = list(map(int, entrada.split(',')))
    # TODO: Converta a entrada em uma lista de inteiros:
    return vendas

vendas = obter_entrada_vendas()
print(analise_vendas(vendas))
