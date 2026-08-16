#Dado um número inteiro x, retorne true se x for um palíndromo, e false de outras formas.
class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False

        lista = list(map(int, str(x)))
        
        for i in range(len(lista)//2):
            if lista[i]!=lista[len(lista)-1-i]:
                return False

        return True