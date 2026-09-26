def posicoes_pares(numeros):
    lista_posicoes = []
    for i, valor in enumerate(numeros):
        if valor%2 == 0:
            lista_posicoes.append(numeros[i])
    return lista_posicoes

resultado = posicoes_pares([1,2,3,4,5,6,7,8,9,10])
print(resultado)