class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic = {}
        for number in nums:
            dic[number] = dic.get(number,0)+1
            if dic[number] == 2:
                duplicated = number
                break
        length = len(nums)
        sum_total = int((1+length)*length/2)
        return [duplicated,sum_total - (sum(nums)-duplicated)]


