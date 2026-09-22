valores = 1
menor = None
numero = 0
while valores < 11:

    try:
        numero = int(input(f'Insira o {valores}º valor: '))
        valores += 1
        
    except ValueError:
        print('Valor não identificado')
        continue

    if menor == None:
        menor = numero
    elif numero < menor:
        menor = numero

print(f'O menor valor dentre os 10 é {menor}')
