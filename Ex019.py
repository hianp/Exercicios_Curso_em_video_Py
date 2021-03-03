import random
a1 = str(input('Alunos 1: '))
a2 = str(input('Aluno 2: '))
a3 = str(input('Aluno 3: '))
a4 = str(input('Aluno 4: '))

alunos = [a1, a2, a3, a4]

ae = random.choice(alunos) #vai fazer somente uma escoha da lista

print(ae)

