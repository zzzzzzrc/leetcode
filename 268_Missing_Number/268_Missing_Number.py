class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numbers = len(nums)
        target = (numbers*(numbers+1))//2
        return target-sum(nums)
