class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dictionary = {}
        for i in range(len(numbers)):
            if target - numbers[i] not in dictionary:
                dictionary[numbers[i]] = i

            else:
                return [dictionary[target-numbers[i]]+1,i+1]
