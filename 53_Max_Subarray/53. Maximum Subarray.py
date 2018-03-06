class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curmax = nums[0]    #当前最大值
        cursum = nums[0]    #当前子数组的和
        for i in range(1,len(nums)):
            cursum += nums[i]
            if nums[i]>=cursum: #如果当前数大于当前子数组的和 则从当前数开始计算
                cursum = nums[i]
            if cursum>curmax:   #储存最大值
                curmax = cursum
        return curmax