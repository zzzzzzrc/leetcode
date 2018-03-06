class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # if s == "":
        #     return 0
        # else:
        split = s.split(' ')    #以空格分割
        rev = split[::-1]       #反转 以解决末尾空格的问题
        for item in rev:
            if item !='':
                return len(item)    #遇到第一个不为空格的字符  返回长度
        return 0                #若都为空格 返回0