class Solution(object):
    def searchInsert(self, nums, target):
        esquerda = 0
        direita = len(nums) - 1

        while esquerda <= direita:
            meio = (esquerda + direita) // 2

            if nums[meio] == target:
                return meio  # Encontrou o valor!
            elif nums[meio] < target:
                esquerda = meio + 1  # O target está na metade direita
            else:
                direita = meio - 1   # O target está na metade esquerda

        # Se o loop terminar sem encontrar, 'esquerda' é exatamente
        # o índice onde o elemento deve ser inserido.
        return esquerda