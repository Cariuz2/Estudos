A = int(input('Isira o valor de A: '))
O = int(input('Insira o valor de O: '))

num = None
AO = []
inicializador = A + 1
finalizador = O - 1
while True:

    if O < A:
        print('O código não pode ser inicializado A é maior O')
        break
    
    else:
        if inicializador > finalizador:
            print(AO)
            break
        else:
            AO.append(inicializador)
            inicializador += 1

            
