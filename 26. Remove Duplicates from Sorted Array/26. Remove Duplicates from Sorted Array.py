class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i = 0
        a = len(nums)
        while(i<a-1):
            if nums[i] == nums[i+1]:
                del nums[i]
                a = len(nums)
            else:
                i+=1
        output = len(nums)
        return output
