def soma_bordas(M):
    maxm = 0
    soma = 0
    for i in range(0, len(M)):
        maxi = len(M[i])
        if maxi >= maxm:
            maxm = maxi

    maxc = maxm - 1

    for i in range(0, len(M)):
        soma += M[i][0] + M[i][maxc]
           
            
    
    return soma

resultado = soma_bordas([[1,2,3],[4,5,6],[7,8,9]])
print(resultado)