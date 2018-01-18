class Solution:
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        #(1+i)*i/2=n
        #求解一元二次方程
        #求根公式x=-b/2a +/- (b^2-4ac)^0.5/2a
        return int((-1+(8*n+1)**0.5)/2)

