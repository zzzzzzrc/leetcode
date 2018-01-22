class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs==[]:
            return ""
        else:
            strs = sorted(strs) #按字母表排序
            i = 1
            try:
                if strs[0][0]!=strs[-1][0]:     #第一位不相同则无相同前缀
                    return ""
                else:
                    while(i<=len(strs[0])):     #逐位判断是否相等
                        if strs[0][i] == strs[-1][i]:
                            i+=1
                        else:                   #当不相等时返回前i-1位
                            return strs[0][0:i]
            except:
                return strs[0][0:i]


