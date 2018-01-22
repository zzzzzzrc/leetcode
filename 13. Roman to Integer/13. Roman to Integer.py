class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        total = 0
        prestr = 0
        i = len(s)-1
        while(i>=0):
            curstr = dic[s[i]]
            if curstr < prestr:
                total -= curstr
            else:
                total += curstr
            prestr = curstr
            i-=1
        return total
