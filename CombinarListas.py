# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        lista=[]
        i=0
        j=0
        while i<len(list1) and j<len(list2):
            if list1[i]<=list2[j]:
                lista.append(list1[i])
                i+=1
            elif list1[i]>list2[j]:
                lista.append(list2[j])
                j+=1
        
        while i<len(list1):
            lista.append(list1[i])
            i+=1

        while j<len(list2):
            lista.append(list2[j])
            j+=1

        return lista