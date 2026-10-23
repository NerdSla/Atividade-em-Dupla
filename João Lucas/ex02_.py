import os
os.system('cls')

prod = input('O produto: ')
quant = int(input('Digite a quantidade: '))
preco = float(input('Digite o preço: R$ '))

if quant <= 5:
    desc = preco - (preco * 0.02)
    print(f'Produto: {prod}')
    print(f'Total: {preco}')
    print(f'Desconto: 2%')
    print(f'Total a pagar: {desc}')
elif quant > 5 and quant <= 10:
    desc = preco - (preco * 0.03)
    print(f'Produto: {prod}')
    print(f'Total: {preco}')
    print(f'Desconto: 3%')
    print(f'Total a pagar: {desc}')
else:
    desc = preco - (preco * 0.05)
    print(f'Produto: {prod}')
    print(f'Total: {preco}')
    print(f'Desconto: 5%')
    print(f'Total a pagar: {desc}')
