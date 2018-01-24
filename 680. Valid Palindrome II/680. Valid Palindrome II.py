class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #两个指针 head end 当存在不相同的字符时 判断
        #出现不同时 判断中间的字符串是否是回文 (删除第一个或最后一个)
        head = 0
        end =len(s)-1
        while(head<=end):
            if s[head] != s[end]:
                s_uncommon = s[head:end+1]
                break
            else:
                head += 1
                end -= 1
        if head >end:
            return True
        else:
            s_list = list(s_uncommon)
            if s_list[1:] == s_list[1:][::-1] or s_list[:-1] == s_list[:-1][::-1]:
                return True
            else:
                return False
