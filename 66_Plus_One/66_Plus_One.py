class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits)-1   #末尾index
        while(i>=0):
            if digits[i] + 1 ==10:  # 若相加等于10 需要进位
                digits[i] =0        # 该位置0
                i-=1                # index向前移位 再进行判断
            else:
                digits[i] += 1      #若相加不为10 跳出循环
                break
        if i == -1:                 #若第一位相加等于10  需要向前进位 9999———> 10000
            newdigits=[0]*(len(digits)+1) # 构造新列表
            for j in range(len(digits)+1):
                if j == 0:
                    newdigits[j] = 1
                else:
                    newdigits[j] = 0
        else:
            newdigits = digits
        return newdigits
