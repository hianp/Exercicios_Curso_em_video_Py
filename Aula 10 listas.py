"""
listas (list)

listas em python funcionam como vetores/matrizes (arrays) em outras linguagens, com a diferença
de serem dinamico e também de podermos colocar qualquer tipo de dado.

linguagens c/java: arrays
    - possuem tamanho e tipo de dado fixo;
    ou seja, nesta linguagem se você criar um array do tipo int e com tamanho 5, este array
    será sempre do tipo inteiro e poderá ter sempre no máximo 5 valores.

já em python:
    - dinâmico: não possuem tamanho fixo; ou seja, podemos criar a lista e simplesmente ir adicionando elementos;
    - qualquer tipo de dado: não possuem tipo de dado fixo; ou seja, podemos colocar qualquer tipo de dado.

As listas sao mutáveis: Ou seja, elas podem mudar constantemente

as listas em python são representadas por colchetes: []

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['g', 'e', 'e', 'k', ' ', 'u', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('geek university')

cores = ['verde', 'amarelo', 'azul', 'branco']


-----------------------------------------------------------------------
#podemos facilmente checar se determinado valor está contido na lista.

num = 7
if num in lista4:
    print(f'encontrei o número {num}')
else:
    print(f'não encontrei o número {num}')


-----------------------------------------------------------------------

# podemos fácilmente orderar uma lista.

lista1.sort()
print(lista1)

-----------------------------------------------------------------------
# podemos fácilmente contar o número de ocorrências de um valor em uma lista

print(lista1.count(1))
print(lista5.count('e'))


-----------------------------------------------------------------------
# adicionar elementos em listas

#obs: para adicionar elementos em listas, utilizamos a funçao append

print(lista1)
lista1.append(42)
print(lista1)

#obs: com append, nós só conseguimos adicionar 1 elemento por vez

lista1.append(12, 34, 52) #erro
-----------------------------------------------------------------------

# mas podemos adicionar uma lista dentro da outra
lista1.append([8, 3, 1])
print(lista1)

for [8, 3, 1] in lista1:
    print('escontrei a lista.')
else:
    print('não encontrei a lista.')

^^^^^^^ coloca a lista como elemnto unico (sub-lista)^^^^^^

-----------------------------------------------------------------------

para adicionarmos multiplos elementos de uma só vez em uma lista, usamos o extend, assim
mantendo a forma simples da lista (sem sub-listas)
#coloca cada elemento da lista como valor adiconal à lista

lista1.extend([123, 44, 67])
print(lista1)


------------------------------------------------------------------------

#podemos inserir um novo elemento na lista informando a posição do índice.
isso não substitui o valor inicial. o mesmo será deslocado para a direita da lista.


lista1.insert(2, 'novo valor')
print(lista1)
r: [1, 99, 'novo valor', 4, 27, 15, 22, 3, 1, 44, 42, 27]


------------------------------------------------------------------------

# podemos facilmente juntar duas listas.

lista6 = lista1 + lista2
print(lista6)
r: [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27, 'g', 'e', 'e', 'k', ' ', 'u', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

# podemos usar o extend para juntar duas listas também

lista1.extend(lista2)
print(lista1)
r: [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27, 'g', 'e', 'e', 'k', ' ', 'u', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']


------------------------------------------------------------------------

# podemos facilmente inverter uma lista
# para inverter a ordem das listas usamos o reverse.

exemplo 1 - forma 1

lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)

r: [27, 42, 44, 1, 3, 22, 15, 27, 4, 99, 1]
['y', 't', 'i', 's', 'r', 'e', 'v', 'i', 'n', 'u', ' ', 'k', 'e', 'e', 'g']

exemplo 2 - forma 2

print(lista1[::-1])
print(lista2[::-1])

r:[27, 42, 44, 1, 3, 22, 15, 27, 4, 99, 1]
['y', 't', 'i', 's', 'r', 'e', 'v', 'i', 'n', 'u', ' ', 'k', 'e', 'e', 'g']

------------------------------------------------------------------------

# podemos também copiar uma lista./ fazer uma cópia

lista6 = lista1.copy()
print(lista6)

r: [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]



------------------------------------------------------------------------

para saber o tamanho de uma lista, usamos o len()

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
print(len(lista1))

r: 11

------------------------------------------------------------------------
 podemos remover facilmente o ultimo elemento de uma lista com o pop()

  - o pop não somente remove o último elemento mas também o retorna
print(lista5)
lista5.pop()
print(lista5)
r: ['g', 'e', 'e', 'k', ' ', 'u', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
['g', 'e', 'e', 'k', ' ', 'u', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't']

# podemos remover um elemento pelo indice.
print(lista5)
lista5.pop(2)
print(lista5)
r: ['g', 'e', 'e', 'k', ' ', 'u', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
['g', 'e', 'k', ' ', 'u', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

#obs: os elementos à direita deste índice serão deslocados para a esquerda.
#obs: se não houver elemento no índice informado, teremos o erro indexError.

------------------------------------------------------------------------

# podemos remover todos os elementos (zerar uma lista)
print(lista5)
lista5.clear()
print(lista5)
r: []



-------------------------------------------------------------------------

# podemos facilemente repetir elementos de uma lista
nova = [1, 2, 3]
nova = nova * 3
print(nova)


-------------------------------------------------------------------------

# podemos facilemente converter uma string em lista

 - exemplo 1

curso = 'programação em python essencial'
curso = curso .split()
print(curso)
r: ['programação', 'em', 'python:', 'essencial']

#obs: por padrão, o split separa os elementos da lista pelo espaço entre elas.

 - exemplo 2
# mudamos o separador das palavras do padrão(espaço) para as vírgulas.


curso1 = 'programação,em,python:,essencial'
curso1 = curso1.split(',')
print(curso1)
r: ['programação', 'em', 'python:', 'essencial']

-------------------------------------------------------------------------
#convertendo uma lista em uma string

lista6 = ['programaçao', 'em', 'python:', 'essencial']
print(lista6)

# abaixo estamos falando: pega a lista6, coloca espaço entre cada elemento e transforma em uma string.
curso = ' '.join(lista6)
print(curso)
r: programaçao em python: essencial

curso = '$'.join(lista6)
print(lista6)
R: programação$em$Python:$Essencial

-------------------------------------------------------------------------
#podemos realmente colocar qualquer tipo de dado em uma lista, inclusive misturando esses dados

lista6 = [1, 2.34, true, 'geek', 'd', [1, 2, 3], 45618565]
print(lista6)
print(type(lista6))

r: [1, 2.34, true, 'geek', 'd', [1, 2, 3], 45618565]
<class 'list'>


-------------------------------------------------------------------------
# iterando sobre listas

 - exemplo 1 -> utilizando for

soma = 0
for elemento in lista1:
    print(elemento, end=' ')
    soma += elemento
print(soma)
r: *soma dos elementos da lista1

 - exemplo 2 -> utilizando for

lista2 = ['g', 'e', 'e', 'k', ' ', 'u', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

soma = ''
for elemento in lista5:
    soma += elemento
print(soma)
r: geek university


 - exemplo 3 -> utilizando while

carrinho = []
produto = ''

while produto != 'sair':
    print("adicione um produto na lista ou digite 'sair' para sair:")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)


----------------------------------------------------------------------
# utilizando variáveis  em listas

numeros = [1, 2, 3, 4, 5]
num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros2 = [num1, num2, num3, num4, num5]
print(numeros)
print(numeros2)

r:[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]

------------------------------------------------------------
# fazemos acesso aos elementos de forma indexada
#           0         1        2        3
cores = ['verde', 'amarelo', 'azul', 'branco']

print(cores[0])  # verde
print(cores[1])  # amarelo
print(cores[2])  # azul
print(cores[3])  # branco

r: verde
amarelo
azul
branco


# fazer acesso aos elementos de forma indexada inversa

print(cores[-1])  # branco
print(cores[-2])  # azul
print(cores[-3])  # amarelo
print(cores[-4])  # verde

r: branco
azul
amarelo
verde


------------------------------------------------------------

 - utilizando for

cores = ['verde', 'amarelo', 'azul', 'branco']

for cor in cores:
    print(cor, end=' -> ')
print('\n')
indice = 0
r: verde -> amarelo -> azul -> branco ->

 - utilizando while

while indice < len(cores):
    print(cores[indice], end="" ' -> ' if indice < 3 else ' -> fim')
    indice += 1
r: verde -> amarelo -> azul -> branco -> fim


-------------------------------------------------------------
enumerate

cores = ['verde', 'amarelo', 'azul', 'branco']

# gerar indices em um for

for indice, cor in enumerate(cores):
    print(indice, cor)

r:
0 verde
1 amarelo
2 azul
3 branco


-------------------------------------------------------------
# Listas aceitam valores repetidos


lista = []
lista.append(42)
lista.append(42)
lista.append(33)
lista.append(33)
lista.append(42)
print(lista)

R: [42, 42, 33, 33, 42]

-------------------------------------------------------------

# Outros metedos não tão importantes mas também úteis

# Encontrar o índice de um elemento na lista

numeros = [5, 6, 7, 8, 9, 10]

# Em qual índice da lista está o valor 6
print(numeros.index(6))

# Em qual índice da lista está o valor 9
print(numeros.index(9))

# OBS: caso não tenha esse elemento na lista, será apresentado erro ValueError
print(numero.index(19) -> Gera ERRO


 - Exemplo 2
 OBS: Retorna o índice do primeiro elemento encontrado

numeros = [5, 6, 7, 5, 8, 9, 10]
print(numeros.index(5))

R:1
4

# Podemos fazer busca dentro de um range, ou seja. qual índice começar a buscar
print(numeros.index(5, 1))  # buscar apartir do índice 1
print(numeros.index(5, 2))  # buscar apartir do índice 2
print(numeros.index(5, 3))  # buscar apartir do índice 3
print(numeros.index(5, 4))  # buscar apartir do índice 4

R: 3
3
3
ERROR


# Podemos fazer busca dentro de um range, ínicio/fim

print(numeros.index(8, 3, 6))  # Busca o índice do valor 8, entre os índices 3 a 6
R: 4

-------------------------------------------------------------

# Revisão de slicing

# lista[ínicio:fim:passo]
# range(ínicio:fim:passo)

# Trabalhando com slice de listas com o parâmetro 'ínicio'.

lista = [1, 2, 3, 4]

print(lista[1:])
# R: [2, 3, 4]


# Trabalhando com slice de listas com o parâmetro 'Fim'.

print(lista[:2])  # Começa no índice 0, pega até o índice 2-1(não vai até o 2)
# R: [1, 2]

print(lista[:4])  # Começa no índice 0, pega até o índice 4-1(não vai até o 4)
# R: [1, 2, 3, 4]

print(lista[1:3])  # Começa no índice 1, pega até o índice 3-1(não vai até o 3)


# Trabalhando com slice de lista com o parâmetro 'passo'.

print(lista[1::2])  # Começa em 1, vai até o final de 2 em 2
# R: [2, 4]
print(lista[::2])  # Começa em 0, vai até o final de 2 em 2
# R: [1, 3]

-------------------------------------------------------------
# Invertendo valores em uma lista

nomes = ['Geek', 'Univesity']

nomes[0], nomes[1] = nomes[1], nomes[0]

print(nomes)
# R: ['Univesity', 'Geek']

# Utilizando de formas pythonicas

nomes = ['Geek', 'Univesity']
nomes.reverse()
print(nomes)
# R: ['Univesity', 'Geek']

-------------------------------------------------------------
# Soma, Valor maximo*, Valor mínimo*, Tamanho

# * Se os valores forem todos inteiros ou reais.

lista = [1, 2, 3, 4, 5, 6]

print(sum(lista))  # Soma
R: 21
print(max(lista))  # Máximo valor
R: 6
print(min(lista))  # Mínimo valor
R: 1
print(len(lista))  # Tamanho da lista
R: 6


-------------------------------------------------------------
# Transformando uma lista em tupla

lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))
R: [1, 2, 3, 4, 5, 6]
<class 'list'>

tupla = tuple(lista)
print(tupla)
print(type(tupla))
R: (1, 2, 3, 4, 5, 6)
<class 'tuple'>

-------------------------------------------------------------
# Desempacotamento de listas

lista = [1, 2, 3]

num1, num2, num3 = lista

print(num1)
print(num2)
print(num3)

# R: 1
# 2
# 3

# OBS: se tivermos mais elementos para desempacotador do que variaveis para receber os valores, teremos ValueError
# OBS1.1: Se tivermos um número diferente de elementos na lista ou variaveis para receber os dados, teremos ValueError

-------------------------------------------------------------

# Copiando uma lista para outra (Shallow Copy e Deep Copy)

# Forma 1 - Deep Copy

lista = [1, 2, 3]
print(lista)

nova = lista.copy()  # cópia

print(nova)

nova.append(4)

print(lista)
print(nova)
R: [1, 2, 3]
[1, 2, 3]
[1, 2, 3]
[1, 2, 3, 4]

# Veja que ao utilizarmos lista.copy() copiamos os dados da lista para uma nova lista, mas elas ficam totalmente
# independentes, ou seja, modificando uma lista, não afeta a aoutra. Isso em Python é chamado Deep Copy(cópia profunda)


# Forma 2 - Shallow Copy

lista = [1, 2, 3]
print(lista)

nova = lista  # cópia

print(nova)

nova.append(4)

print(lista)
print(nova)
R: [1, 2, 3]
[1, 2, 3]
[1, 2, 3, 4]
[1, 2, 3, 4]

# Veja que utilizamos a cópia via atribuição e copiamos os dados da lista para a nova lista, mas após realizar
# modificaçoes em uma das listas, essa modificaçao se refletiu em ambas as listas. Isso em Python é chamado
# Shallow Copy.
"""
