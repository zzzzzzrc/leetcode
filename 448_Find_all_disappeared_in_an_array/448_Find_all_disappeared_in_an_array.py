class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        for i in range(length):
            index = abs(nums[i])-1
            nums[index] = -abs(nums[index])
        a = []
        for i in range(length):
            if nums[i] > 0:
                a.append(i+1)
        return a
