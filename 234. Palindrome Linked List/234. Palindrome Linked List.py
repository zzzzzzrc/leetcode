# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        def reverse(head):
            newhead = None
            while(head):
                p = head
                head = head.next
                p.next = newhead
                newhead = p
            return newhead
        if head == None or head.next == None:
            return True
        elif head.next.next==None:
            if head.val == head.next.val:
                return True
            else:
                return False
        else:
            fast = head
            slow = head
            while(fast and fast.next):
                slow = slow.next
                fast = fast.next.next
            node = slow
            newhead = reverse(node)
            while(newhead):
                if head.val != newhead.val:
                    return False
                    break
                head = head.next
                newhead = newhead.next
        return True
