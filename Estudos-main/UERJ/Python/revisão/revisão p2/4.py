def inverter_dicionario(thisdict):
    dict2 = {}
    for chave, valor in thisdict.items():
        v = (valor, chave)
        dict2.update({v})
    return dict2

resultado = inverter_dicionario({'Júlia': 5, 'Gustavo': 7, 'Leonardo': 8, 'Eric': 4, 'Alessandra': 10})
print(resultado)