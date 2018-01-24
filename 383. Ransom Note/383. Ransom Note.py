class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        #构建两个dic
        dic1 = {}
        dic2 = {}
        for item in ransomNote:
            dic1[item] = dic1.get(item,0)+1
        for item in magazine:
            dic2[item] = dic2.get(item,0)+1
        for key in dic1.keys():
            if key not in dic2:
                return False
            elif dic1[key]>dic2[key]:
                return False
        return True
