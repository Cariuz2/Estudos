matriz = [[-5,  3, -8],[ 2, -1,  -7],[ 0, -4,  9]]

def contar_negativos(M):
    r = 0
    for i in range(0,len(M)):
        for j in range(0,len(M[i])):
            if M[i][j] < 0:
                r += 1
    return r

resultado = contar_negativos(matriz)
print(resultado)