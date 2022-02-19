# Crie um algoritimo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
print('# Exemplo 01')
n = int(input('Digite um número: '))
dobro = n * 2
tripo = n * 3
raiz = n ** (1/2)
print('''Analizando o numero digitado, '
o dobro será {}.
o triplo será {}.
a raiz quadrada sera {}.'''.format(dobro, tripo, raiz))

print('# Exemplo 02')
n = int(input('Digite um número: '))
print('''Analizadno o número digitado,
o dobro será {}.
o tripo será {}. 
ea raiz quadrada será {}.'''.format(n * 2, n * 3, (n**(1/2))))

print('# Exemplo 03')
n = int(input('Digite um número: '))
print('''Analizadno o número digitado,
o dobro será {}.
o tripo será {}. 
ea raiz quadrada será {}.'''.format(n * 2, n * 3, pow(n, (1/2))))