class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currentSum = nums[0]
        maxSum = nums[0]
        #动态规划问题   当前最优解
        for i in range(1,len(nums)):
            currentSum = max(nums[i],currentSum+nums[i]) #比较 i 和 （i + i-1）的大小  找到当前最优解
            maxSum     = max(maxSum,currentSum)          #储存全局最优解
        return maxSum
data = [-2,1,-3,4,-1,2,1,-5,4]
sol = Solution()
output = sol.maxSubArray(data)
print(output)
