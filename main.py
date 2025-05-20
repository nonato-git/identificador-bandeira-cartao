def identificar_bandeira(numero_cartao):
    if numero_cartao.startswith('4'):
        return 'Visa'
    elif numero_cartao.startswith(('51', '52', '53', '54', '55')):
        return 'MasterCard'
    elif numero_cartao.startswith(('34', '37')):
        return 'American Express'
    elif numero_cartao.startswith('6011'):
        return 'Discover'
    else:
        return 'Bandeira desconhecida'

numero = input("Digite o número do cartão: ")
print("Bandeira:", identificar_bandeira(numero))
