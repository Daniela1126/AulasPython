#Recebe as quatro notas do aluno
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))
#Calcula a média
media = (n1+n2+n3+n4)/4
#estrutura de decisão para verificar se o aluno foi aprovado ou não
if (media >= 7): 
    print("Aprovado")
else:
    print("Reprovado")