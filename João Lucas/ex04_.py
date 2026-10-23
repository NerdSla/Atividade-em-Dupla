import os
os.system('cls')

prod = input('O produto: ')
preco = float(input('Digite o preço: R$ '))

while True:
    pag = int(input('Digite a forma de pagamento [a Vista(1) ou a Prazo(2)]: '))
    if pag < 1 or pag > 2:
        print('Forma de pagamento inválido;\nTente novamente apertando em qualquer tecla...')
        os.system('cls')
    else:
        os.system('cls')
        match pag:
            case 1:
                desc = preco - (preco * 0.1)
                print(f'Produto: {prod}')
                print(f'Valor: {preco}')
                print(f'Forma de pagamento: a Vista')
                print(f'Desconto: 10%')
                print(f'Total a pagar: {desc}')
                break
            case 2:
                while True:
                    quant = int(input('Digite a quantidade de parcelas até no máximo 6 (caso não queira parcelar, digite "1"): '))
                    if quant < 1 or quant > 6:
                        input('Quantidade de parcelas inválidas;\nTente novamente apertando em qualquer tecla...')
                        os.system('cls')
                    else:
                        parc = preco / quant
                        print(f'Produto: {prod}')
                        print(f'Forma de pagamento: a Prazo')
                        if quant > 1:
                            print(f'Quantidade de Parcelas: {quant}')
                            print(f'Valor da parcela: {parc}')
                            print(f'Total a pagar: {preco}')
                            break
                        else:
                            print(f'Total a pagar: {preco}')
                            break
    break