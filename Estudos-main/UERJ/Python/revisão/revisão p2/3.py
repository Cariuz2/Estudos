def criar_tabela(list):
    dicionario = {}
    for i in list:
        v = (i, len(i))
        dicionario.update({v})
    return dicionario
resultado = criar_tabela(['Júlia','Gustavo','Leonardo','Eric','Alessandra'])
print(resultado)


def criar_tabela2(list):
    return {nome: len(nome) for nome in list}
resultado = criar_tabela2(['Júlia','Gustavo','Leonardo','Eric','Alessandra'])
print(resultado)

