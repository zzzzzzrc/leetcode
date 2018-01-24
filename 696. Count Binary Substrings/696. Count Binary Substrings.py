class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # #solution1
        # #00110011
        # #当字符发生变化时
        # #00/110011  计算00符合要求的   pre = 0 cur(00) = 2         0->1
        # #/0011/0011 计算0011符合要求的 pre(00) = 2 cur(11) = 2     1->0
        # #00/1100/11 计算1100符合要求的 pre(11) = 2 cur(00) = 2     0->1
        # #0011/0011/ 计算0011符合要求的 pre(00) = 2 cur(11) = 2     无变化  需要在循环外进行处理
        # preCount = 0
        # curCount = 1
        # count = 0
        # i = 0
        # while(i<len(s)-1):
        #     if s[i] == s[i+1]:
        #         curCount += 1
        #         i += 1
        #     else:
        #         count += min(preCount,curCount)
        #         preCount = curCount
        #         curCount = 1
        #         i += 1
        # count += min(preCount,curCount)
        # return count

        #########################################################
        #solution2
        # 做映射 00111011--->2312
        # 00111011---> 00 111 0 11--->2312
        #zip()  以短的为准 zip([2,3,1,2],[3,1,1]) ---> (2,3)(3,1)(1,2)
        s = list(map(len, s.replace('01', '0 1').replace('10', '1 0').split()))
        return sum(min(a, b) for a, b in zip(s, s[1:]))

