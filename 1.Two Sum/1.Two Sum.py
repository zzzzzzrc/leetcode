class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}                          #python字典具有hashmap的性质
        for i,number in enumerate(nums):   #dict={key1:value1,key2:value2,key3:value3}
            if number not in dict:          #nums不在字典中 将该nums与target的差值存入字典中
                dict[target-number] = i     #dict={target-nums:i}   i为地址
            else:
                output = (dict[number],i)   # 此时的i为当前num的index  dict[number] 为另一个数的index
                return output
a = Solution()
b = a.twoSum((3,3,4,5),9)
print(b)
