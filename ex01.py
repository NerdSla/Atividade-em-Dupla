import os
os.system("cls")

primero_numero = int(input("Digite seu primeiro número: "))

print("")

segundo_numero = int(input("Digite seu segundo número: "))

print("")

escolha_operador = str(input("Digite o operador matemático escolhido: "))

match escolha_operador:
    case "+":
        soma = primero_numero + segundo_numero
        print (f"soma: {soma}")
    case "-":
        subtracao = primero_numero - segundo_numero
        print (f"subtracao: {subtracao}")
    case "*":
        multiplicacao = primero_numero * segundo_numero
        print (f"multiplicacao: {multiplicacao}")
    case "/":
        divisao = primero_numero / segundo_numero
        print (f"divisao: {divisao}")