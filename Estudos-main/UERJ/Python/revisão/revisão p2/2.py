def converter_temperaturas(temp):
    f = 0
    ftemp = []
    for c in temp:
        f = c * 9 / 5 + 32
        ftemp.append(f)
    return ftemp

resultado = converter_temperaturas([23,44,35,38,21])
print(resultado)