'''nums = [1,2,1,3,4,1,1,8,1,10,1]
dic = {}
for i in range(len(nums)):
    if nums[i] not in dic:
        dic[nums[i]] = 1
    else:
        dic[nums[i]] += 1
        #if dic[nums[i]] > len(nums)/2:
            #output = nums[i]

print(max(dic,key=dic.get))'''
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        if len(nums) == 1:
            return nums[0]
        else:
            for i in range(len(nums)):
                if nums[i] not in dic:
                    dic[nums[i]] = 1
                else:
                    dic[nums[i]] += 1
        return max(dic,key=dic.get)

