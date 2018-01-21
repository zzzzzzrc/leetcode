class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        # if s=="":
            # return s
        if s == ['']:
            return ''
        else:
            abc = "aeiouAEIOU"
            dic = {}
            for item in abc:
                dic[item] = dic.get(item,0)+1
            head = 0
            end = len(s)-1
            while(head<end):
                if s[head] not in dic:
                    head += 1
                elif s[end] not in dic:
                    end -= 1
                elif head<end:
                    # end_temp = s[end]
                    # head_temp = s[head]
                    # s = s[:head]+end_temp+s[head+1:end]+head_temp+s[end+1:]
                    s[head],s[end] = s[end],s[head]
                    head += 1
                    end -= 1
                else:
                    # return s
                    return ''.join(s)
            # return s
            return ''.join(s)
