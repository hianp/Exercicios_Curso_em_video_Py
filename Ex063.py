num = int(input('Digite a quantidade de termos: '))
t1 = 0
t2 = 1
cont = 3
print(f'{t1} -> {t2}', end='')

while cont <= num:
    t3 = t1 + t2
    cont += 1
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
print('\033[31m -> FIM')
