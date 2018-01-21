class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        j = 0
        for i in range(length):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
        for p in range(j,length):
            nums[p] = 0
