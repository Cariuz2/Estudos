#1 - Ler o valor de três números e escrever a média
""" print('Calculadora de média \nInsira 3 números:')
n1 = int(input())
n2 = int(input())
n3 = int(input())
avg = (n1+n2+n3)/3
print(f'A média dos númneros é: {avg}')  """

# 2 - Ler dois valores inteiros e trocar o conteúdo desses valores (escrever os valores antes e depois da troca)
""" vi1 = int(input('Insira um valor inteiro: 2'))
vi2 = int(input('Insira outro valor inteiro: '))

print(f'Seus valorares {vi1} {vi2}')

vi1 = int(input('Insira outro valor inteiro: '))
vi2 = int(input('Insira outro valor inteiro: '))

print(f'Seus valorares atualizados {vi1} {vi2}') """

#3 - Ler a idade de uma pessoa em anos e imprimir essa idade em dias. Considere que um ano tem 365 dias.

""" idade = int(input('Insira a sua idade e te diremos quantos dias você tem de vida: \n'))
print('Você tem ', idade*365,'de vida') """

#4 4 - Desenvolva um programa em Python que solicite ao usuário a distância percorrida durante uma viagem (em quilômetros) e a quantidade de combustível consumida (em litros). Em seguida, calcule o consumo médio do veículo em quilômetros por litro (km/L) e exiba o resultado na tela.

""" d = int(input('Insira a distância percorrida (em Km): '))
oil = int(input('Insira o gasto de combustível (em L): '))
eficiencia = d/oil
print(f'A efiência do seu carro é {eficiencia} km por litro') """

# 5)
""" nome = input('Insira o nome do produto: ')
valor = int(input('Insira o valor da unidade do produto: '))
quantidade = int(input('Insira a quantidade comprada: '))
print(f'Você gastou {valor*quantidade} reais em {quantidade} {nome}.') """

# 6)
""" number = int(input('Insira um valor de 10 casas: '))
ant = number - 1
suc = number + 1
print(f'Seu antecessor é {ant} e seu sucessor é {suc}.') """

# 7)
""" farinha = 400 #g
acucar = 250 #g
leite = 200 #mL

porcao = int(input('Insira a quantidade de porções desejadas: '))

receita = porcao/8

print(f'Você vai precisar de {farinha*receita}g de farinha, {acucar*receita}g de açúcar e {leite*receita}mL de leite para fazer {porcao}.') """

# 8)
""" valor = int(input('Insira o valor da conta: '))
gorjeta = valor*0.1
pessoas = int(input('Quantas pessoas pagarão a conta? '))
print(f'Valor total {valor+gorjeta} reais; {valor} reais mais {gorjeta} reais de gorjeta e cada um pagará {(valor+gorjeta)/pessoas} reais. ') """