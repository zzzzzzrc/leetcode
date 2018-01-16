class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # 10%9=1
        # 11%9=2
        # 100%9=1
        # 102%9=3
        if num == 0:
            return 0
        else:
            output = num%9
            if output == 0:
                return 9
            else:
                return output
# class Solution:
#     def addDigits(self, num):
#         """
#         :type num: int
#         :rtype: int
#         """
#         def add(num):
#             sum_num = 0
#             while(num>0):
#                 a = num%10
#                 sum_num += a
#                 num = num//10
#             return sum_num
#         if num<10:
#             return num
#         else:
#             while(num>=10):
#                 num = add(num)
#             return num
