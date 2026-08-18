class Solution(object):
    def isValid(self, s):
        pilha = []

        for caractere in s:

            if caractere == '(' or caractere == '[' or caractere == '{':
                pilha.append(caractere)

            else:
                if len(pilha) == 0:
                    return False

                topo = pilha.pop()

                if caractere == ')' and topo != '(':
                    return False

                if caractere == ']' and topo != '[':
                    return False

                if caractere == '}' and topo != '{':
                    return False

        if len(pilha) == 0:
            return True

        return False


        