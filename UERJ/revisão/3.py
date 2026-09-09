# 3 - Leia números inteiros positivos até que o usuário digite 0. Some apenas os números pares e exiba o resultado.

numeros = []
soma = 0
while True:
    valor = int(input('Insira valores inteiro positivos (pare com 0): '))

    if valor < 0:
        print('Valores negativos não são permitidos')
        continue
    
    elif valor == 0:
        print('Lista encerrada')
        break
    
    else:
        numeros.append(valor)

for i in numeros:
    if i % 2 == 0:
        soma += i
print(soma)