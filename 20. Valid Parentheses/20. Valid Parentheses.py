class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #出现右括号 必定在前面有一个左括号出现 否则return False
        stack = []
        dic={')':'(',
             ']':'[',
             '}':'{'}

        for item in s:
            if item in ['(','{','[']:
                stack.append(item)
            elif item in[')','}',']']:
                # a = stack.pop()
                if stack == [] or stack.pop() != dic[item]:
                    return False
            else:
                return False
        if stack == []:
            return True
        else:
            return False
