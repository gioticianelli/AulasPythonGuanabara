# Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

# Verificando o menor
menor = n1
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

# Verificando o maior
maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3

# Saída
print(f"O menor número é {menor}")
print(f"O maior número é {maior}")
