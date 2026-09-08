# 1 a) Leia as notas (valores entre 0 e 10) até que seja digitada a nota -1.

notas = []

while True:

    try:

        nota = float(input('Insira a(s) nota(s): '))

        if nota == -1:
            
            break

        elif nota > 10:

            print('Nota acima do permitido')
            continue

        elif nota < 0: 

            print('Nota abaixo do permitido')
            continue
        
        else:

            notas.append(nota)

    except ValueError:

         print('Nota com valor indefinido')

print(notas)

# b) Mostre a maior nota abaixo de 7.

notas.sort()
mnota = -1
reprovados = 0

for i in notas:

    if i < 7:

        reprovados += 1

    if i < 7 and i > mnota:
        
        mnota = i

print(f'Nota mais alta abaixo da média: {mnota}')


# c) Caso não exista nenhuma nota abaixo de 7, informe que todos os alunos foram aprovados.

if mnota == -1:

    print('Todos foram aprovados')

else:
    
    print(f'{reprovados} alunos foram reprovados')
