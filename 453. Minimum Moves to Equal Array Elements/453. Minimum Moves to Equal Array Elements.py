class Solution:
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #暴力解法  根据题意迭代  TLE
        # length  = len(nums)
        # def add(nums):
        #     for i in range(length-1):
        #         nums[i] += 1            #n-1位+1
        #     nums = sorted(nums)
        #     return nums,sum(nums),nums[-1]*length   #当所有元素都相等时  sum(nums)== nums[-1]*length
        # a = sum(nums)
        # b = nums[-1]*length
        # count = 0
        # nums = sorted(nums)
        # while(a!=b):
        #     nums,a,b = add(nums)
        #     count+=1
        # print(nums,count)
        # return count

        #做减法  每次将数组从小到大排序 末尾元素-1直到==min(nums)  TLE
        # min_num = min(nums)
        # nums = sorted(nums)
        # count = 0
        # while(nums[-1]!=min_num):
        #     nums[-1] -= 1
        #     nums = sorted(nums)
        #     count += 1
        # return count

        #求各个元素与最小元素的差值
        min_num = min(nums)
        count = 0
        for item in nums:
            count += item-min_num
        return count
