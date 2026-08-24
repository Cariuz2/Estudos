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

