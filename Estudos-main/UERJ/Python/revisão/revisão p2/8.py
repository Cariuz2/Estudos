numeros = [42, 7, 89, 15, 63, 28, 91, 4, 52, 76, 33, 18, 95, 61, 22, 84, 11, 47, 70, 39]

def separar_pares_impares(n):
    pares = []
    impares = []
    for i in n:
        #impar
        if i % 2 != 0:
            impares.append(i)
        else:
            pares.append(i)
    return pares, impares





resultado = separar_pares_impares(numeros)
print(resultado)