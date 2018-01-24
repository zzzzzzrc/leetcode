class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        #当k=1时 不做反转
        if k<=1:
            return s
        else:
            def reverse(s):
                # head = 0
                # end = len(s)-1
                # while(head<=end):
                #     s[head],s[end] = s[end],s[head]
                #     head += 1
                #     end -= 1
                return s[::-1]
            i = 0
            length = len(s)
            #每2K中的前K个做反转
            while(i<length-2*k):
                s = s[:i]+reverse(s[i:i+k]) + s[i+k:]
                i += 2*k
            #末尾依照题目规则进行处理
            if length - i<k:
                s = s[:i]+reverse(s[i:])
            else:
                s = s[:i]+reverse(s[i:i+k])+s[i+k:]
            return s
