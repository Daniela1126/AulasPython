#Escreva um programa que leia 10 numeros do usuário e calcule a soma entre desses numeros.
contador = 0
soma = 0
#Processamento
while contador < 10:
    numero = float(input("Digite um numero: "))
    soma = soma + numero
    contador = contador + 1
print(soma)
    