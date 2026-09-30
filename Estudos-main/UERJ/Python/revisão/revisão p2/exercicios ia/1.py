lista = [1,2,3,4,5,6,7,8,9,10]
n = 4

def indices_multiplos(list, n):
    multi = []
    for i in list:
        if i % n == 0:
            multi.append(i)
    return multi

resultado = indices_multiplos(lista, n)
print(resultado)
            
