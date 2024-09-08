#Verificar se o número digitado
#é PAR
n1 = int(input("Digite um número: "))
contador = 0
#Processamento
while contador <= n1:
    if contador % 2 == 0:
        print(contador)
    contador = contador + 1
