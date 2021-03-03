import random


a1 = str(input('Alunos 1: '))
a2 = str(input('Aluno 2: '))
a3 = str(input('Aluno 3: '))
a4 = str(input('Aluno 4: '))

alunos = [a1, a2, a3, a4]

random.shuffle(alunos) #vai embaralhar

print('A ordem de apresentação será:')
print(alunos)


