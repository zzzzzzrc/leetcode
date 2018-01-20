class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        elif haystack == "":
            return -1
        else:
            length = len(haystack)
            length_needle = len(needle)
            i = 0
            while(i<=length-length_needle):
                if haystack[i] == needle[0]:
                    if haystack[i:i+length_needle] == needle:
                        return i
                    else:
                        i += 1
                else:
                    i += 1
            return -1
