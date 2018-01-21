class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dic={}
        count = 0
        i = 0
        length = len(nums)
        if k < 0:
            return 0
        elif k == 0:
            while(i<length):
                if nums[i] not in dic:
                    dic[nums[i]] = 0
                    i += 1
                else:
                    dic[nums[i]] = 1
                    i += 1
            return (sum(dic.values()))
        else:
            while(i<length):
                if nums[i] not in dic:
                    dic[nums[i]] = 1
                    if (nums[i]+k) in dic and (nums[i]-k) in dic:
                        count += 2
                        i += 1
                    elif (nums[i]+k) in dic or (nums[i]-k) in dic:
                        count += 1
                        i += 1
                    else:
                        i += 1
                else:
                    i += 1
            return count
