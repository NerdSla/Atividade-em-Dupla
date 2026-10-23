import os
import time
os.system("cls")

numero = int(input("Digite seu número para ser multiplicado: "))

for i in range(1, 11):
    print (f"Multiplicação de {i}: {numero * i}")
    time.sleep(1)