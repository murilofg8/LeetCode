class Solution(object):
    def lengthOfLastWord(self, s):
        i=len(s)-1
        while i>=0 and s[i]==" ":
            i-=1
        fim=i
        while i>=0 and s[i]!=" ":
            i-=1
        tamanho=len(s[i+1:fim+1])
        return tamanho
        