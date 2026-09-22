#1 - Peça a idade de um atleta e informe a categoria:

# • Infantil (<12)
# • Juvenil (12-17)
# • Adulto (≥18)

# idade = None

# while True:
#     try:
#         idade = int(input('Insira a sua idade: '))
    
#         if idade > 0 and idade < 12:
#             print('Sua categoria é infantil')
#             break
#         elif idade >= 12 and idade <= 17:
#             print('Sua categoria é juvenil')
#             break
#         elif idade >= 18 and idade < 100:
#             print('Sua categoria é adulta')
#             break
#         else:
#             print('Você provavelmente está mortou ou mentindo mesmo')
    
#     except ValueError:
#         print('Valor não esperado')
#     print('Digite novamente')

# #2 2 - Peça uma senha ao usuário. Se estiver correta (ex: "1234"), exiba “Acesso permitido”, caso contrário “Acesso negado”.
# senha = None
# verificador = None

# #Criador da senha
# while True:
#     senha = input('Crie uma senha de 6 dígitos: ')
#     if len(senha) > 6:
#         print('Senha muito longa.')
        
#     elif len(senha) <= 1:
#         print('Senha muito curta.')
        
#     else:
#         print('Senha criada.')
#         break
    

# #Verificador
# while True:
#     verificador = input('Insira sua senha: ')
#     if verificador == senha:
#         print('Senha correta')
#         break
#     else: 
#         print('Senha incorreta')
    
# 3 - Peça uma temperatura em °C e informe se está:

# • Frio (<15°C)
# • Agradável (15–25°C)
# • Quente (>25°C)

# temperatura = None

# while True:
#     try:
#         temperatura = int(input('Insira a temperatura (C°): '))
#         if temperatura < 15:
#             print('A temperatura está fria')
#             break
#         elif temperatura >= 15 and temperatura <= 25:
#             print('A temperatura está agradável')
#             break
#         elif temperatura > 25:
#             print('A temperatura está quente')
#             break
#     except ValueError:
#         print('Valor não esperado')
    
# 4 - Peça um número de 1 a 7 e informe qual dia da semana corresponde (1 = Domingo, 2 = Segunda, …).

# valor = None

# while True:

#     try:
#         valor = int(input('Insira um número de 1 a 7 e informarei o dia da semana: '))

#     except ValueError:
#         print('Valor não esperado')
#         continue
    
#     if valor == 1:
#         print('Hoje é domingo')
#     elif valor == 2:
#         print('Hoje é segunda-feira')
#     elif valor == 3:
#         print('Hoje é terça-feira')        
#     elif valor == 4:
#         print('Hoje é quarta-feira')
#     elif valor == 5:
#         print('Hoje é quinta-feira')
#     elif valor == 6:
#         print('Hoje é sexta-feira')
#     elif valor == 7:
#         print('Hoje é sábado')  
#     else:
#         print('Número fora do intervalo (1 a 7)')
#         continue
    
#     break

#5 - Peça para o usuário escolher entre "floresta", "caverna" ou "montanha" e imprima uma frase diferente para cada escolha.

# palavras = ['floresta', 'caverna', 'montanha']
# identificador = None
# opcoes = '012'

# while True:

#     identificador = input(f'Escolha: {palavras[0]}[0], {palavras[1]}[1] ou {palavras[2]}[2]: ')

#     if identificador in opcoes:

#         for i in identificador:

#             if i == '0':
#                 print('Floresta de madeira escura')
#             elif i == '1':
#                 print('Caverna escura')
#             elif i == '2':
#                 print('Monte Everest')

#         break
    
#     else:

#         print('Opção não identificada')
#         continue

#6 - Peça ao usuário que informe se está "sol", "chuva" ou "frio" e sugira uma roupa adequada para cada caso.

# palavras = ['sol', 'chuva', 'frio']
# identificador = None
# opcoes = '012'

# while True:

#     identificador = input(f'Escolha: {palavras[0]}[0], {palavras[1]}[1] ou {palavras[2]}[2]: ')

#     if identificador in opcoes:

#         for i in identificador:

#             if i == '0':
#                 print('Utilize roupas mais curtas')
#             elif i == '1':
#                 print('Use um guarda chuva e um casaco')
#             elif i == '2':
#                 print('Use casaco e luvas')

#         break
#     else:

#         print('Opção não identificada')
#         continue

#7 - Pergunte a hora do dia (0–23) e informe se é dia (6–18) ou noite (19–5).

# hora = None

# while True:

#     try:

#         hora = int(input('Informe as horas (0-23): '))

#     except ValueError:

#         print('Valor inesperado.')
#         continue
    
#     if hora > 6 and hora < 18:

#         print('Está de dia')
#         break
    
#     elif hora < 6 and hora >= 0 or hora > 18 and hora <= 23:

#         print('Está de noite')
#         break
    
#     else:

#         print('O valor está fora do previsto')
#         continue

# 8 - Peça um número e informe se ele está dentro do intervalo 1–100 ou fora dele.

numero = None

while True:
    try:
        numero = int(input('Insira um número: '))
    except ValueError:
        print('Valor inválido')
