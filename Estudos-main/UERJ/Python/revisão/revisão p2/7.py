matriz = [[5,  3, 8],[2, 1, 7],[0, 4, 9]]

def maior_linha(M):
    r = 0
    soma = 0
    for i in range(0,len(M)):
        soma = 0
        for j in range(0,len(M[i])):
            soma += M[i][j]
        if soma >= r:
            r = soma
    return r
resultado = maior_linha(matriz)
print(resultado)