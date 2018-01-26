class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        else:
            def Newton(num):
                curnum = 0.5*(num+x/num)
                delta = abs(num-curnum)
                return curnum,delta
            delta = 1
            num = x
            while(delta>0.01):
                num,delta=Newton(num)
            return int(num)
