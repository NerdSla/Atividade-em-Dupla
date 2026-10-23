import os
os.system('cls')
par = 0
impar = 0
soma = 0

for i in range (5):
    num = int(input(f'Digite o {i+1}º número inteiro: '))
    soma += num
    if num % 2 == 0:
        par = par + 1
    else:
        impar = impar + 1

os.system('cls')
print(f'Quantidade de Pares: {par}')
print(f'Quantidade de Impares: {impar}')
print(f'Soma: {soma}')