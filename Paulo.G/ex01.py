import os
os.system("cls")

primero_numero = int(input("\nDigite seu primeiro número: "))

#\n

segundo_numero = int(input("\nDigite seu segundo número: "))

#\n

operador = str(input("\nDigite o operador matemático escolhido: "))

match operador:
    case "+":
        soma = primero_numero + segundo_numero
        print(f"Operador e numero escolhido: {operador}, {primero_numero} + {segundo_numero}")
        print (f"Resultado: {soma}")
    case "-":
        subtracao = primero_numero - segundo_numero
        print(f"Operador e numero escolhido: {operador}, {primero_numero} - {segundo_numero}")
        print (f"Resultado: {subtracao}")
    case "*":
        multiplicacao = primero_numero * segundo_numero
        print(f"Operador e numero escolhido: {operador}, {primero_numero} * {segundo_numero}")
        print (f"Resultado: {multiplicacao}")
    case "/":
        while True:
            if primero_numero == 0 or segundo_numero == 0:
                primero_numero = int(input("Digite seu primeiro número: "))
                segundo_numero = int(input("Digite seu segundo número: "))
            else:
                print("")
                break
        divisao = primero_numero / segundo_numero
        print(f"Operador e numero escolhido: {operador}, {primero_numero} / {segundo_numero}")
        print (f"Resultado: {divisao}")
    case _:
        print ("Operador invalido")