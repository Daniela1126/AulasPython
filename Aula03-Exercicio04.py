# Fazer um programa que verifique se a pessoa pode dirigir e para isso ela precise ter cnh
#Recebe a idade e a informação de que a pessoa tem ou não cnhl
idade = int(input("Digite sua idade: "))
cnh = input("Possui CNH: ")
#verifica se a pessoa pode dirigir
if (idade >=18 and cnh == "sim"):
    print("Pode dirigir")
else:
    print("Não pode dirigir")

