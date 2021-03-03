nome = str(input('Digite seu nome completo: '))
print(f'Seu nome completo em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print(f'Seu nome tem {len(nome.strip())} caractéres')
n = nome.split()
print(f'Seu primeiro nome é {n[0].capitalize()} e tem {len(n[0])}')


