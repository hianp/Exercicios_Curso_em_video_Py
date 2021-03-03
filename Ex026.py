nome = str(input('Digite seu nome: ')).lower().strip()
print(f'A letra A aparece {nome.count("a")} vezes na frase')
print(f'A primeira letra A apareceu na posiçao {nome.find("a") + 1}')
print(f'A ultima letra A apareceu na posição {nome.rfind("a") + 1}')
