class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        output = []
        for index,str in enumerate(s):
            if str not in dic:
                dic[str] = index
            else:
                dic[str] = -1
        for key,value in dic.items():
            if value>=0:
                output.append(value)
        if len(output) == 0:
            return -1
        else:
            return min(output)
