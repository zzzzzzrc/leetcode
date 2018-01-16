class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # 得到数量级
        def get_tens(num):
            a = num
            n = 1
            while(a>=10):
                n = n*10
                a = num//n
            return n
        # 负数不可能为回文
        if x<0:
            return False
        # 个位数必为回文
        elif x<10:
            return True
        else:
            head = get_tens(x)
            end  = 1
            a = x
            b = x
            while(end<=head):           #循环的条件前后指针相遇 或者end指针超过head  12321 123321
                dig_head = a//head      # 得到第一个数
                dig_end  = b%10         # 得到末尾的数
                if dig_head == dig_end: # 如果相等则继续  head向右 end向左
                    a = a%head          # a去掉第一个数
                    head = head//10     # 数量级-1
                    b = b//10           # b去掉最后一个数
                else:
                    return False
            return True

