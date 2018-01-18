class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = sorted(nums)
        a = nums_set[-1]*nums_set[-2]*nums_set[-3]
        b = nums_set[0]*nums_set[1]*nums_set[-1]
        return max(a,b)
