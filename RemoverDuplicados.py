class Solution(object):
    def deleteDuplicates(self, head):
        atual = head

        while atual and atual.next:
            if atual.val == atual.next.val:
                atual.next = atual.next.next
            else:
                atual = atual.next

        return head