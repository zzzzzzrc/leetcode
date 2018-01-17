class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        def ugly(num):
            if num%2==0:
                return num//2       #能被2整除 继续循环
            elif num%3==0:
                return num//3       #能被3整除
            elif num%5==0:
                return num//5       #能被5整除
            else:
                return -1
        if num==1:
            return True
        elif num<1:
            return False
        else:
            while(num>1):           #循环直到num=1   6//2=3-->3//3=1
                num=ugly(num)
            if num==1:
                return True
            else:
                return False
