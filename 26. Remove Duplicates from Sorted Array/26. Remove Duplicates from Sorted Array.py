class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #当第一个数与第二个数相等时 pop第一个数
        #不相等时 判断后一位的数
        i=0
        while(i<len(nums)-1):
            if nums[i+1] == nums[i]:
                nums.pop(i)
            else:
                i += 1
        return len(nums)