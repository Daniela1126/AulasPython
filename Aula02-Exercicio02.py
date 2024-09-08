#Faça um programa em Python que receba a altura e o peso de uma pessoa e mostre qual o valor do IMC
altura = float(input("Qual a sua altura? "))
peso = float(input("Qual o seu peso? "))
#Encontre o IMC
imc = (peso / (altura * altura) )
print("O IMC é igual a ", imc)