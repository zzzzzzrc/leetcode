class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        output = False
        i = 0
        dic = {}
        while(i<len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = i
                i += 1
            else:
                output = True
                break
        return output
