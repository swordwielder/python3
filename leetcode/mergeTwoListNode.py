# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        list1 = list(l1)
        list2 = list(l2)        
        a = []
        l1i=0
        l2i=0
        
        for i in range(len(list1)+len(list2)):
            if list1[l1i]<=list2[l2i]:
                a.append(list1[l1i])
                l1i+=1
            else:
                a.append(list2[l2i])
                l2i+=1
        
        return a
        
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
