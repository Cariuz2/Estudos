lista = [10,20,30,45,26,18,27]

def converter_temperaturas_dupla(list):
    Fah = []
    Kel = []
    
    for i in list:
        Fah.append(i * 9/5 +35)
        Kel.append(i + 273.15)
    return Fah, Kel

resultado = converter_temperaturas_dupla(lista)
print(resultado)
