class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        #两个dic  大写 小写
        abc = "abcdefghijklmnopqrstuvwxyz"
        ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        dic1 = {}
        dic2 = {}
        for item in abc:
            dic1[item] = dic1.get(item,0)+1
        for item in ABC:
            dic2[item] = dic2.get(item,0)+1
        if word=="":
            return False
        elif len(word) == 1:
            return True
        else:
            if word[0] in dic1:
                for item in word:
                    if item in dic2:
                        return False
                return True
            else:
                count = 0
                for item in word:
                    if item in dic1:
                        count += 1
                if count == len(word)-1 or count == 0:
                    return True
                else:
                    return False
