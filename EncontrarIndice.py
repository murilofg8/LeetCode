class Solution(object):
    def strStr(self, haystack, needle):
        len_h = len(haystack)
        len_n = len(needle)

        # Se a palavra buscada for maior que o texto, é impossível encontrar
        if len_n > len_h:
            return -1

        # Percorre apenas até onde a needle ainda cabe
        for i in range(len_h - len_n + 1):
            if haystack[i : i + len_n] == needle:
                return i  # Retorna imediatamente a posição assim que achar

        return -1  # Se percorreu tudo e não achou