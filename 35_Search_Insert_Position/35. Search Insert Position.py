class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if target <=nums[i]:        #找到插入位置
                return i
            else:
                i+=1
        return len(nums)                #当目标数比nums都大时 插入在最后