#Escreva um programa que leia a idade de 20 pessoas e exiba a soma das idades.
contador = 0
soma = 0
#Processamento
while contador < 20:
    numero = int(input("Digite uma idade: "))
    soma = soma + numero
    contador = contador + 1
print("A soma de todas as idades é igual a " , soma)