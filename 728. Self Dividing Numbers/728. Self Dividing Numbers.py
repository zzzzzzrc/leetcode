class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def isSelfDivide(num):
            strnum = str(num)
            length = len(strnum)
            count = 0
            for item in strnum:
                if item == '0':
                    count += 0
                elif num%int(item)==0:
                    count += 1
                else:
                    count += 0
            if count == length:
                return True
            else:
                return False
        output = []
        for i in range(left,right+1):
            if isSelfDivide(i):
                output.append(i)
        return output


