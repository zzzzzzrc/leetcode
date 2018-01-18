class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        if c==0:
            return True
        else:
            for i in range(int(c**0.5)+1):
                b_2 = c-i**2
                b = b_2**0.5
                if b%1==0:
                    return True
            return False
