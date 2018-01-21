class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s =="":
            return s
        else:
            s = list(s)
            head = 0
            end = len(s)-1
            while(head<end):
                s[head],s[end] = s[end],s[head]
                head += 1
                end -= 1
            return ''.join(s)
