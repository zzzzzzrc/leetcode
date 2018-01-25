class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        k = k%n
        temp = nums[n-k:n]
        i = n-1
        while(i>k-1):
            nums[i] = nums[i-k]
            i -= 1
        while(i<=k-1 and i >=0):
            nums[i] = temp[i]
            i -= 1
