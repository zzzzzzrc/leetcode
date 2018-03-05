# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a = dummy = ListNode(0) #a用来指向dummy dummy用来改变
        while(l1 and l2):       #当l1 和 l2都不为none时  dummy总指向小的数
            if l1.val<=l2.val:
                dummy.next = l1
                dummy = dummy.next
                l1 = l1.next
            else:
                dummy.next = l2
                dummy = dummy.next
                l2 = l2.next
            # dummy = dummy.next
        # 当某个链表遍历完后
        if l1:
            dummy.next = l1
        else:
            dummy.next = l2
        return a.next