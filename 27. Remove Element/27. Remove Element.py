class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = len(nums)
        i = 0
        while(i < length):
            if nums[i] == val:
                del nums[i]
                length = len(nums)
            else:
                i+=1
        return length
