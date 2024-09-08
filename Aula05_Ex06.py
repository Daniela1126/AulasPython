#Escreva um programa que leia 20 numeros do usuário e exiba quantos números são maiores que 8.
contador = 0
resultado = 0
#Processamento
while contador < 5:
    numero = float(input("Digite um numero: "))
    if numero > 8:
        resultado = resultado + 1
    contador = contador + 1
print(resultado)