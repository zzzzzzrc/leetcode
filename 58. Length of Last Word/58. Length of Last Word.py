class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        #指针从尾部向头部遍历 当遇到空格时 停止遍历 返回长度
        if s=="":
            return 0
        else:
            length = len(s)
            index = length-1
            #末尾由空格
            while(index>=0):
                if s[index] == ' ':
                    index -= 1
                else:
                    string = s[0:index+1]
                    break
            if index == -1:
                return 0
            else:
                string_len = len(string)
                string_index = string_len-1
                while(string_index>=0):
                    if string[string_index] != ' ':
                        string_index -= 1
                    else:
                        return string_len - 1 -string_index
                return string_len
