class Solution:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        #遍历一遍 遇到空格 count+=1
        if s=="":
            return 0
        else:
            length = len(s)
            count = 0
            for i in range(length-1):
                if (s[i] != ' ' and s[i+1] == ' '):      #当前不为空格 下一位为空格
                    count += 1
            if s[-1] != ' ':
                count += 1
            return count
