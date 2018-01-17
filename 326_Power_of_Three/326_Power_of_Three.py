class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #暴力解法 循环除以3
        if n == 1 or n == 3:
            return True
        elif n==2 or n<=0:
            return False
        else:
            while(n>3):
                if n%3==0:
                    n=n//3
                else:
                    return False
            if n==3:
                return True
            else:
                return False
