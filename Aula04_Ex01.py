#Faça um programa que receba os seguintes dados de entrda: 

nome = input("Digite seu nome: ")
idade = int(input("Qual é a sua idade? "))
altura = float(input("Qual a sua altura? "))
peso = float(input("Qual o seu peso? "))
#Encontre o IMC
imc = (peso / (altura * altura) )
print("O IMC é igual a ", imc)
if (imc < 17):
    print("Olá ", nome, "seu IMC é igual a", imc, "e você está muito abaixo do peso")
elif (imc >= 17 and imc < 18.5):
    print("Olá ", nome, "seu IMC é igual a", imc,  "você está abaixo do peso.")
elif (imc >= 18.5 and imc <25):
    print("Olá ", nome, "seu IMC é igual a", imc,  "você está com peso normal.")
elif (imc >= 25 and imc <30):
    print("Olá ", nome, "seu IMC é igual a", imc,  "você está acima do peso.")
elif (imc >= 30 and imc <35):
    print("Olá ", nome, "seu IMC é igual a", imc,  "você tem uma Obesidade de Grau I")
elif (imc >= 35 and imc <40):
    print("Olá ", nome, "seu IMC é igual a", imc,  "você tem uma Obesidade de Grau II.")
elif (imc >= 40):
    print("Olá ", nome, "seu IMC é igual a", imc,  "você tem uma Obesidade de Grau III.")


#versão simplificada do professor
nome = input("Digite seu nome: ")
idade = int(input("Qual é a sua idade? "))
altura = float(input("Qual a sua altura? "))
peso = float(input("Qual o seu peso? "))
#Encontre o IMC
imc = (peso / (altura ** 2) )
if imc = 16.9
    classificacao = "Muito abaixo do peso"
elif (17 <= imc and imc <=18.4):
    classificacao = "Abaixo do peso"
elif (18.5 <= imc and imc <= 24.9):
    classificacao = "Peso normal"
elif (25 <= imc and imc <=29.9):
    classificacao = "Acima do Peso"
elif (25 <= imc and imc <= 29.9):
    classificacao = "Obesidade Grau I"
elif (30 <= imc and imc <=34.9):
    classificacao = "Obesidade Grau II"
else:
    classificacao = "Obesidade Grau III"

