class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i=0
        length = len(nums)
        while(i<length):
            if nums[i] == target:
                index = i
                break
            elif nums[i] > target:
                index = i
                break
            else:
                i += 1
        if i == length:
            index = length
        return index
sol = Solution()
a = sol.searchInsert([1,2,3,4,5,7,9],10)
print(a)
