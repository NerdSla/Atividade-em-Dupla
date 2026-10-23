import os
os.system("cls")

# Coleta de dados
renda_mensal = float(input("Digite sua renda mensal: "))
valor_emprestimo = int(input("Digite o valor do empréstimo: "))
desejo_prestacoes = int(input("Digite em quantas prestações deseja pagar: "))

prestacao = valor_emprestimo / desejo_prestacoes

# O emprestimo deve ser de no maximo 10x a renda mensal
limite_emprestimo = valor_emprestimo * 10

print("")

# Cada prestação deve ser no maximo 30% da renda mensal
limite_percentual_rendamensal = renda_mensal * 0.30

if valor_emprestimo < limite_emprestimo and prestacao < limite_percentual_rendamensal:
    print("Aprovado")
else:
    print("Negado")

print(f"renda mensal: {renda_mensal}")
print(f"valor do emprestimo: {valor_emprestimo}")
print(f"prestações desejadas: {desejo_prestacoes}")
print(f"Limite do emprestimo: {limite_emprestimo}")
print(f"Cada prestação: {prestacao}")
print(f"30% da renda mensal: {limite_percentual_rendamensal}")

