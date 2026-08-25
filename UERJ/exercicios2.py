import math
# 1. O usuário insere o raio de um círculo, e o programa calcula sua área.
""" R = int(input('Insira o raio do círculo (cm) e te devolvo a área dele: '))
Area = (math.pi*R**2)
print(f'A área do seu círculo é {round(Area, 3)}cm.') """

# 2. O usuário insere o raio de uma esfera, e o programa calcula seu volume.
""" 
r = int(input('Insira o raio (cm): '))
volume = (4/3)*math.pi*(r**3)
print(f'O volume da esfera é {round(volume, 3)}cm') """

# 3. O usuário insere seu peso (kg) e altura (m), e o programa calcula seu IMC.
""" peso = int(input('Insira seu peso (kg): '))
altura = float(input('Insira sua altura (m): '))
imc = peso / (altura**2)

print(f'Seu índice de massa corporal é {round(imc,2)}') """

# 4. O usuário insere o salário bruto e as porcentagens de descontos de INSS e IR, e o programa calcula o salário líquido.
""" 
salario = int(input('Insira seu salário: '))
inss = 0.075
ir = 0.075
liquido = salario - salario*inss - salario*ir
print(f'Seu salário líquido é de {liquido} reais.') """

# 5. O usuário insere a densidade do fluido, a aceleração da gravidade e a profundidade, e o programa calcula a pressão.

""" print('Pressão hidrostática')
d = int(input('Insira a densidade do fluido: '))
g = int(input('Insira a gravidade: '))
h = int(input('Insira a profundiade: '))
P = d*g*h
print(f'A pressão hidrostática é de {P}Pa.') """

# 6. O usuário insere o capital inicial, a taxa de juros e o tempo de investimento, e o programa calcula o montante final.
# M = C*((1+i)**t)
""" 
C = int(input('Insira o valor inicial: '))
i = float(input('Insira a taxa de juros: '))
t = float(input('Insira o tempo em meses: '))

M = C*((1+i)**t)

print(f'O valor finaldepois de {t} é {round(M,2)} reais.') """

# 7. O usuário insere a massa de uma substância, seu calor específico, a variação de temperatura e a potência de aquecimento, e o programa calcula o tempo necessário.
# m = int(input('Insira a massa da substância(g): '))
# c = float(input('Insira o calor específico(cal/gºC)'))
# T = int(input('Insira a variação de temperatura(ºC)'))
# P = int(input('Insira a potência do aquecimento (cal)'))

# t = P / (m*c*T)

# print(f'o tempo necessário será {t} minutos')

# 8. O usuário insere um tempo total em segundos, e o programa converte para horas, minutos e segundos.

# time = int(input('Insira o tempo em segundos: '))
# minutos = 0
# segundos = 0
# horas = time//3600
# Rh = time % 3600
# Rm = 0
# if Rh > 0:
#     minutos = Rh // 60
#     Rm = Rh % 60

# if horas == 1:
#     phora = ('hora')
# else:
#     phora = ('horas')
# if minutos == 1:
#     pmin = ('minuto')
# else:
#     pmin = ('minutos')
# if Rm == 1:
#     pseg = ('segundo')
# else:
#     pseg = ('segundos')


# print(f'{horas} {phora}, {minutos} {pmin} e {Rm} {pseg}')

# 9. O usuário insere as coordenadas dos dois pontos (x1, y1) e (x2, y2), e o programa calcula a distância entre eles.
# x1 = int(input('Insira o X do ponto A: '))
# y1 = int(input('Insira o Y do ponto A: '))
# x2 = int(input('Insira o X do ponto B: '))
# y2 = int(input('Insira o Y do ponto B: '))

# dab = round(math.sqrt((x2 - x1)**2 + (y2 - y1)**2))

# print(f'A distância entre A e B é de {dab} centímetros.')

# 10. O usuário insere os três lados de um triângulo, e o programa calcula o perímetro e a área usando a fórmula de Heron.

# a = int(input('Insira o valor do lado A: '))
# b = int(input('Insira o valor do lado B: '))
# c = int(input('Insira o valor do lado C: '))

# p2 = a + b + c
# p = p2/2

# Area = math.sqrt(p*(p-a)*(p-b)*(p-c))

# print(p2, Area)

# 11. O usuário insere a massa (kg) e a velocidade (m/s) de um objeto, e o programa calcula a energia cinética.

# m = int(input('Insira a massa (kg): '))
# v = int(input('Insira a velocidade (m/s)'))

# E = (m*v**2)/2

# print(f'A energia cinética é {E}J.')

# 12. O usuário insere um valor em reais e as taxas de câmbio para dólares e euros, e o programa converte o valor para ambas as moedas.

# reais = int(input('Insira o valor em reais: '))
# euro = reais * 6
# dolar = reais * 5.15

# print(f'O valor convertido em Euros: {euro} e em Dólar: {dolar}')

