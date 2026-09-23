matriz_a = [[2,3,-1],[0,6,2],[7,8,10]]
matriz_b = [[2],[-1],[1]]

print(f'{len(matriz_b)}x{len(matriz_b[0])}')

matriz_ab = [[0 for i in range(0, len(matriz_b[0]))]for j in range(0, len(matriz_a))]

for i in range(0, len(matriz_ab)):
    for j in range(0, len(matriz_ab[0])):
        for k in range(0, len(matriz_a)):
            for l in range(0, len(matriz_b[0])):
                matriz_ab[i][j] = matriz_a[i][l] * matriz_b[j][k]
                print(f'{matriz_ab[i][j]} = {matriz_a[i][l]} x {matriz_b[j][k]}')

print(matriz_ab)



