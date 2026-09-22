# 4 - Leia uma palavra do usuário e conte quantas vogais minúsculas aparecem. Não use funções prontas como count().

palavra = input('Insira uma palavra: ')
vogaismin = 'aeiou'
resultado = 0
for i in palavra:
    if i in vogaismin:
        resultado += 1

print(resultado)