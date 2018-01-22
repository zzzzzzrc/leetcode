class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        # 迭代  暴力解法
        def countandsay(strs,n):
            stack = []
            output = ""
            for item in strs:
                if stack == []:             #当栈为空时 元素进栈
                    stack.append(item)
                elif item in stack:         #当前元素与栈内元素相同时，元素进栈
                    stack.append(item)
                else:                       #当前元素与栈内元素不同时，返回栈内元素（say）以及栈的长度（count），栈清空，新元素进栈
                    output+=(str(len(stack))+stack[0])
                    stack = []
                    stack.append(item)
            output += (str(len(stack))+stack[0])    #遍历结束后栈内元素及栈的长度
            n += 1
            return output,n
        i=1
        strs = "1"
        while(i<n):
            strs,i = countandsay(strs,i)
        return strs
