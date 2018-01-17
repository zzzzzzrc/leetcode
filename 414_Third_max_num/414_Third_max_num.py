class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        a = set(nums)
        b = sorted(a)
        length = len(b)
        if length == 0:
            return []
        elif length == 1:
            return b[0]
        elif length == 2:
            return b[1]
        else:
            return b[-3]
