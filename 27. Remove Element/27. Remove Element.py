class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        #依次遍历 当前值等于指定值时pop 否则i+=1 遍历完
        i=0
        while(i<len(nums)):
            if nums[i] == val:
                nums.pop(i)
            else:
                i+=1
        return len(nums)