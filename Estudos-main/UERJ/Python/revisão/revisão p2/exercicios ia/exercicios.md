# Exercícios de Revisão P3

## 1
Crie uma função chamada `indices_multiplos` que receba uma lista de números inteiros e um valor inteiro `n` e retorne uma nova lista contendo os índices dos elementos que são múltiplos de `n`.

---

## 2
Crie uma função chamada `converter_temperaturas_dupla` que receba uma lista de temperaturas em graus Celsius e retorne um dicionário contendo:

- uma lista com as temperaturas convertidas para Fahrenheit;
- uma lista com as temperaturas convertidas para Kelvin.

Use:

```python
F = C * 9/5 + 32
K = C + 273.15
```

---

## 3
Crie uma função chamada `contar_iniciais` que receba uma lista de nomes e retorne um dicionário onde cada chave seja uma letra inicial e o valor associado seja a quantidade de nomes que começam com essa letra.

---

## 4
Crie uma função chamada `agrupar_idades` que receba um dicionário contendo nomes como chaves e idades como valores e retorne um novo dicionário em que cada idade seja uma chave e o valor seja uma lista com os nomes das pessoas que possuem aquela idade.

---

## 5
Crie uma função chamada `soma_diagonais` que receba uma matriz quadrada de números inteiros e retorne a soma dos elementos da diagonal principal e da diagonal secundária.

---

## 6
Crie uma função chamada `linha_com_mais_negativos` que receba uma matriz de números inteiros e retorne o índice da linha que possui a maior quantidade de números negativos.

---

## 7
Crie uma função chamada `media_linhas` que receba uma matriz de números e retorne uma lista contendo a média dos valores de cada linha da matriz.

---

## 8
Crie uma função chamada `pares_impares_positivos` que receba uma lista de números inteiros e retorne um dicionário contendo três listas:

- uma com os números pares;
- uma com os números ímpares;
- uma com os números positivos.

---

## 9
Crie uma função chamada `maior_diferenca_consecutiva` que receba uma lista de números inteiros e retorne a maior diferença absoluta encontrada entre pares de elementos consecutivos da lista.

---

## 10
Crie uma função chamada `frequencia_elementos` que receba uma lista de números inteiros e retorne um dicionário informando quantas vezes cada número aparece na lista.

---

## 11
Crie uma função chamada `rotacionar_lista` que receba uma lista e um número inteiro `k` e retorne uma nova lista com os elementos deslocados `k` posições para a direita.

---

## 12
Crie uma função chamada `matriz_simetrica` que receba uma matriz quadrada e retorne `True` caso ela seja simétrica e `False` caso contrário.

Uma matriz é simétrica quando:

```python
matriz[i][j] == matriz[j][i]
```

---

## 13
Crie uma função chamada `segundo_maior` que receba uma lista de números inteiros e retorne o segundo maior valor da lista sem utilizar o método `sort()`.

---

## 14
Crie uma função chamada `maior_sequencia_crescente` que receba uma lista de números inteiros e retorne o tamanho da maior sequência crescente consecutiva encontrada na lista.

---

## 15
Crie uma função chamada `estatisticas_matriz` que receba uma matriz de números inteiros e retorne um dicionário contendo:

- o maior elemento;
- o menor elemento;
- a média de todos os elementos;
- a quantidade de números pares;
- a quantidade de números negativos.

---

## Dica

Se eu fosse apostar no que tem mais chance de aparecer na prova, focaria principalmente nas questões **3, 4, 5, 6, 10 e 15**, pois elas combinam os tópicos mais cobrados da revisão original:

- Funções
- Listas
- Dicionários
- Matrizes
- Contagem de elementos
- Laços de repetição