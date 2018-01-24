class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # count A >1  return F   连续的三个L return F
        if "LLL" in s:
            return False
        else:
            s = list(s)
            #超过1个'A' return F
            if 'A' in s:
                s.remove('A')
            if 'A' in s:
                return False
            else:
                return True
