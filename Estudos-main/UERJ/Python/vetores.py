# vetor_a = [10,20,30]
# vetor_b = []

# for i in range(0, len(vetor_a)):
#     vetor_b.append(vetor_a[i])

# print(vetor_b)

# vetor_b[1] = 0

# print(max(vetor_a))
# print(min(vetor_a))
# print(sum(vetor_a))

# linhas = int(input('Número de linhas: '))
# colunas = int(input('Número de colunas: '))
# A = []

# for i in range(0, linhas):
#     A.append([])
#     for j in range(0, colunas):
#         A[i].append(int(input('Elemento [{}][{}]: '.format(i, j))))

# At = [[0 for i in range(0, linhas)] for j in range(colunas)]

# for i in range(0,linhas):
#     for j in range(0,colunas):
#         At[j][i]=A[i][j]
# print(A,sep='\n')
# print(At,sep='\n')

M = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
linhas = len(M)

soma = 0
for i in range(0, linhas):
    soma += M[i][i]
print(soma)