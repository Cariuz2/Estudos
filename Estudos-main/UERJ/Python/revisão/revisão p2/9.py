lista = [14, 42, 7, 89, 53, 21, 66, 30, 95, 12]

def maior_consecutivo(l):
    r = 0
    tempsoma = 0
    i = 0
  
    while True:
        tempsoma = l[i] + l[i+1]
      
        if tempsoma >= r:
            r = tempsoma
          
        else:
            tempsoma = 0
          
        i += 1
      
        if i+1 >= len(l):
            break
        
    return r

resultado = maior_consecutivo(lista)
print(f'O resultado é {resultado}')
