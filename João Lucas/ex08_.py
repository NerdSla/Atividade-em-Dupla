import os
os.system('cls')

lim_tent = 3
tent = 0

cad_usua = input('Cadastre seu usuário: ')
cad_sen = input('Cadastre sua senha: ')

os.system('cls')
while tent < lim_tent:
    usua = input('Digite seu usuário: ')
    sen = input('Digite sua senha: ')
    if usua == cad_usua and sen == cad_sen:
        print('Seja Bem-Vindo! :3')
        break
    else:
        tent = tent + 1
        if tent == lim_tent:
            print('Limite de Tentativas atingido;\nAcesso Negado.')
            break
        else:
            print(f'Tentativas restantes: {lim_tent - tent}')
            input('Usuário ou senha incorretas;\nTente novamente apertando qualquer botão...')