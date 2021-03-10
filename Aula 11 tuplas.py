"""
Tuplas (tuple)

Tuplas são bastante parecidas com listas.

Existem duas diferenças basicas:

    1 - As tuplas são representadas por parenteses ()
    print(type(()))
    R: <class 'tuple'>

    2 - As tuplas são imutaveis: Isso significa que ao se criar uma tupla ela não muda. Toda operação
    em uma tupla gera uma nova tupla.

# Por quê utilizar tuplas?

 - Tuplas são mais rápidos do que listas.
 - Tuplas deixam seu código mais seguro*

 * Isso porque trabalhar com elementos imutáveis traz segurança para o código

---------- CUIDADO 1: As tuplas são representadas por (), mas veja:  ----------

tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))

R:(1, 2, 3, 4, 5, 6)
<class 'tuple'>

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)
print(type(tupla2))
R: (1, 2, 3, 4, 5, 6)
<class 'tuple'>


---------- CUIDADO 2: Tuplas com 1 elemento ----------

tupla3 = (4)  # Isso não é uma tupla!
print(tupla3)
print(type(tupla3))

R: 4
<class 'int'>

tupla4 = (4,)  # Isso é uma tupla!
print(tupla4)
print(type(tupla4))
R: (4,)
<class 'tuple'>

tupla5 = 4,
print(tupla5)
print(type(tupla5))
R: (4,)
<class 'tuple'>

# CONCLUSÃO: Podemos concluir que as tuplas são definidas pela vírgula e não pelo uso do parênteses
(4)  -> Não é tupla
(4,) -> É tupla
4,   -> É tupla


----------------------------------------------------------------------------------------------------

 Podemos gerar uma tupla dinamicamente com range(inicio, fim, passo)

tupla = tuple(range(11))
print(tupla)
print(type(tupla))

R: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
 <class 'tuple'>


----------------------------------------------------------------------------------------------------

 Desempacotamento de tupla

tupla = ('Geek University', 'Programação em Python: Essencial')
escola, curso = tupla
print(escola)
print(curso)
R: Geek University
Programação em Python: Essencial

OBS: Gera erro (ValueErro) se colocarmos um número diferente de elementos para desenpacotar.

----------------------------------------------------------------------------------------------------

[1] - Métodos para: adição e remoção de elementos nas tuplas não existem, dado o fato das tuplas serem imutáveis.

[2] - Soma*, Valor Máximo*, Valor Mínimo* e Tamanho podem ser usados.
 * Se os valores forem todos inteiros ou reais

tupla = (1, 2, 3, 4, 5, 6)
print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

R: 21
6
1
6


----------------------------------------------------------------------------------------------------

 Concatenação de tuplas

tupla1 = (1, 2, 3)
print(tupla1)
R: (1, 2, 3)

tupla2 = (4, 5, 6)
print(tupla2)
R: (4, 5, 6)

print(tupla1 + tupla2)  # Tuplas são imutaveis
print(tupla1)
print(tupla2)
R: (1, 2, 3, 4, 5, 6)
(1, 2, 3)
(4, 5, 6)


tupla3 = tupla1 + tupla2
print(tupla3)
print(tupla1)
print(tupla2)
R: (1, 2, 3, 4, 5, 6)
(1, 2, 3)
(4, 5, 6)

tupla1 += tupla2  # Tuplas são imutáveis, mas podemos sobrescrever seus valores.
print(tupla1)
R: (1, 2, 3, 4, 5, 6)

----------------------------------------------------------------------------------------------------

 Verificar se determinado elemetno está contido na tupla

tupla = (1, 2, 3)
print(3 in tupla)  # True
print(6 in tupla)  # False
print(1 in tupla)  # True
print(0 in tupla)  # False
print(2 in tupla)  # True


----------------------------------------------------------------------------------------------------

 Iterando sobre uma tupla

tupla = (1, 2, 3)

for n in tupla:
    print(n)
R: 1
2
3


for indice, valor in enumerate(tupla):
    print(indice, valor)
R: 0 1
1 2
2 3


----------------------------------------------------------------------------------------------------

 Contando elementos detro de uma tupla

tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')

print(tupla.count('a'))
R: 2

print(tupla.count('b'))
R: 2

print(tupla.count('c'))
R: 1

escola = tuple('Geek University')
print(escola)
R: ('G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y')

print(escola.count('e'))
R: 3


----------------------------------------------------------------------------------------------------

 Dicas na utilização de tuplas

[1] - Devemos utilizar tuplas SEMPRE que não precisarmos modificar os dados contidos em uma coleção

# Exemplo 1
#Não tem porque adicionar mais elementos nessa tupla
meses = ('Janeiro', 'Fevereiro', 'Março', 'AbriL', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

meses2 = ['Janeiro', 'Fevereiro', 'Março', 'AbriL', ' Maio', 'Junho', 'Julho', 'Agosto', ' Setembro', 'Outubro', 'Novembro', 'Dezembro']

# O acesso de elementos de uma tupla também é semelhante a de uma lista

print(meses[6])
R: Julho


[2] - Iterar com while

i = 0

while i < len(meses):
    print(meses[i])
    i += 1

R: Janeiro
Fevereiro
Março
AbriL
Maio
Junho
Julho
Agosto
Setembro
Outubro
Novembro
Dezembro


[3] - Verificamos em qual índice um elemento está na tupla

meses = ('Janeiro', 'Fevereiro', 'Março', 'AbriL', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

print(meses.index('Julho'))
R: 6
# OBS: Caso o elemento não exista, será gerado ValueError.



[4] - Slicing

meses = ('Janeiro', 'Fevereiro', 'Março', 'AbriL', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

----Tupla[inicio, fim, passo]----

print(meses[0:])
# R: ('Janeiro', 'Fevereiro', 'Março', 'AbriL', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

print(meses[5:9])
# R: ('Junho', 'Julho', 'Agosto', 'Setembro')


----------------------------------------------------------------------------------------------------

 Copiando uma tupla para outra

tupla = (1, 2, 3)
print(tupla)
# R: (1, 2, 3)
nova = tupla  # Na tupla não temos o problema de Shallow Copy

print(nova)
# R: (1, 2, 3)
print(tupla)
# R: (1, 2, 3)

outra = (4, 5, 6)

nova = nova + outra

print(nova)
# R: (1, 2, 3, 4, 5, 6)
print(tupla)
# R: (1, 2, 3)




"""

nome = "hian"
print(nome[0])
