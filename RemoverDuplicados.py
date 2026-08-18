# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        for i in range(len(head)-1):
            for j in range(i+1,len(head)):
                if head[i]==head[j]:
                    head.pop(j)

        return head