# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        # 暴力解法 直接遍历两个linked-list求解
        def link(node, num):
            if node:
                num += node.val * tens[0]  # tens为10的倍数
                tens[0] = tens[0] * 10
                return link(node.next, num)
            else:
                tens[0] = 1
                return num

        tens = [1]
        num1 = 0
        num2 = 0
        num1 = link(l1, num1)  # l1表示的数
        num2 = link(l2, num2)  # l2表示的数
        summary = num1 + num2  # 两数的和
        str_sum = str(summary)[::-1]  # 反转
        length = len(str_sum)
        i = 1
        # 构造新链表
        head = ListNode(int(str_sum[0]))
        dummy = head
        while (i < length):
            head.next = ListNode(int(str_sum[i]))
            head = head.next
            i += 1
        return dummy

