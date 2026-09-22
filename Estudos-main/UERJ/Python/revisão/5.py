# 5 - Escreva um programa em Python que peça ao usuário para digitar uma palavra ou frase, inverta a sequência de caracteres digitada e exiba o resultado invertido.

palavra = input('Insira uma palavra: ')
resultado = ''
for i in palavra:
    resultado = i + resultado

print(resultado)