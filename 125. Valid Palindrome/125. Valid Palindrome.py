class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s =="":
            return True
        else:
            dic = {}
            dic2 = {}
            abc = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
            num = "0123456789"
            i = 0
            for item in abc:
                dic[item] = dic.get(item,0)+i
                i += 1
            j = 0
            for item in num:
                dic2[item] = dic.get(item,0)+j
                j += 1
            head = 0
            end = len(s)-1
            while(head<end):
                if s[head] not in dic and s[head] not in dic2:      #s[head] is not a alphanmumeric
                    head += 1
                elif s[end] not in dic and s[end] not in dic2:       #s[end] is not aalphanumeric
                    end -= 1
                elif head<end:        #除去所有非字母数字项 head和end不相等
                    if s[head] in dic and s[end] in dic:
                        if dic[s[head]] == dic[s[end]] or dic[s[head]] == dic[s[end]]+26 or dic[s[head]] == dic[s[end]]-26:
                            head += 1
                            end -= 1
                        else:
                            return False
                    elif s[head] in dic2 and s[end] in dic2:
                        if dic2[s[head]] == dic2[s[end]]:
                            head += 1
                            end -= 1
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            return True
