class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        bits = 1    #每个数有几位digit   1-->9 初始化为1
        count = 9   #共有多少个这样的数  1-->9共有9个
        total = 9   #一共的bits数
        cur_total = 0
        if n<=9:
            return n
        else:
            while(n>total):
                cur_total += bits*count
                bits += 1   # 1bit --> 2bits --> 3bits...
                count = count*10    # 9个(1-9) --> 90个(10-99) -->900个(100-999)...
                total += bits*count #一共的bits数
            n_in_curbits = n - cur_total  #在bits位区间内有多少个digit
            print(n_in_curbits)
            index_bit = n_in_curbits % bits #第index_n个bits位数的第index_bit位
            print(index_bit)
            if index_bit == 0:
                index_bit = bits    #当整除时 处在最后一位
                index_n = n_in_curbits // bits  #第index_n个bits位数
            else:
                index_n = n_in_curbits // bits + 1 #第index_n个bits位数
            print(index_n)
            value = 10**(bits-1) + (index_n-1)   #第n个digit所在的数的数值
            print(value)
            strvalue = str(value)
            return int(strvalue[index_bit-1])

