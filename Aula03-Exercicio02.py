#Faça um programa que leia 3 numeros e diga qual é o maior deles.
n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
n3 = int(input("Digite o terceiro valor: "))
#Verifica se n1 é maior que n2 ou vice-versa
if (n1 > n2 and n1 > n3):
    maior = n1
    print("O maior numero é: ", maior)
if (n2 > n1 and n2 > n3):
    maior = n2
    print("O maior numero é: ", maior)
if (n3 > n1 and n3 > n1):
    maior = n3
    print("O maior numero é: ", maior)
