class Solution(object):
    def longestCommonPrefix(self, strs):
        lista = []
        prefixocomum = []

        for i in range(len(strs)):
            lista.append(len(strs[i]))

        menorpalavra = min(lista)

        for i in range(menorpalavra):
            for j in range(1, len(strs)):
                if strs[0][i] != strs[j][i]:
                    return "".join(prefixocomum)

            prefixocomum.append(strs[0][i])

        return "".join(prefixocomum)