#entrada de dados
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))
#efetua calculo da média
media = (n1 + n2 + n3)/3
#verifica se o aluno foi aprovado (média >= 7)
#recuperação (média entre 5 e 6)
#reprovado, (média menor que 5)
if (media >= 7):
    print("Você foi aprovado, sua média é ", media)
#else:
#   if(media >=5 and media <= 6):
elif (media >= 5 and media < 7):
    print("Você ficou em recuperação, sua média é ", media)
else:
    print("Você foi reprovado, ficou com média: ", media)
