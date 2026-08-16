class Solution(object):
    def romanToInt(self, s):
        lista = []
        listaauxiliar = []
        inteiro = 0

        for i in s:
            if i == 'I':
                lista.append(1)
            elif i == 'V':
                lista.append(5)
            elif i == 'X':
                lista.append(10)
            elif i == 'L':
                lista.append(50)
            elif i == 'C':
                lista.append(100)
            elif i == 'D':
                lista.append(500)
            elif i == 'M':
                lista.append(1000)

        i = 0

        while i < len(lista):
            if i < len(lista) - 1 and lista[i] < lista[i + 1]:
                listaauxiliar.append(lista[i + 1] - lista[i])
                i += 2
            else:
                listaauxiliar.append(lista[i])
                i += 1

        for i in range(len(listaauxiliar)):
            inteiro += listaauxiliar[i]

        return inteiro