class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        def reverse(s):
            return s[::-1]
        s = s.split(' ')
        output = ""
        for item in s:
            output += ' '
            output += reverse(item)
        return output[1:]
