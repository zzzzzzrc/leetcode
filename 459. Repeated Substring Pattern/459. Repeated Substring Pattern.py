class Solution:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #初始化重复字符串为s[0]   依次遍历S
        #若s[i]!=s[0] 则重复字符串置为s[0:2](加一位)继续遍历
        #重复上述过程 直到完全遍历S 则返回True  当s[0:j]长度大于s的一半时  返回False
        def repeated(repeat,j):
            i = 0
            while(i+j<=len(s)):
                if s[i:i+j] == repeat:
                    i += j
                else:
                    j+=1
                    return(s[0:j]),j
                    break
            if i==len(s):
                return True,True
            else:
                return False,False
        if len(s)<=1:
            return False
        elif len(s) == 2:
            return s[0]==s[1]
        else:
            j = 1
            repeat = s[0]
            while(j<=len(s)-1):
                repeat,j = repeated(repeat,j)
                if repeat==True and j ==True:
                    return True
                    break
                elif repeat == False and j ==False:
                    return False
                    break
