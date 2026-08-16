#Dado um array de inteiros nums e um inteiro target, retorne os índices dos dois números de forma que a soma deles seja igual atarget .
#Você pode assumir que cada entrada terá exatamente uma solução e que não poderá usar o mesmo elemento duas vezes.
#Você pode retornar a resposta em qualquer ordem.

numeros = list(map(int, input("digite os números da lista").split()))
alvo = int(input("digite o alvo:"))
lista = []
for i in range(len(numeros)-1):
    for j in range(i+1,len(numeros)):
        if numeros[i]+numeros[j]==alvo:
            lista.append(i)
            lista.append(j)

print(lista)