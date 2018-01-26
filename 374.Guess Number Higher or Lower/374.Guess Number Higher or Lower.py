# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n
        while (l<=r):
            mid = l+(r-l)//2
            a = guess(mid)
            if a == -1:
                r = mid -1
            elif a == 1:
                l = mid + 1
            else:
                return mid
