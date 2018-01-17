class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        dic = {}
        digit = "0123456789"
        for i in range(len(digit)):
            dic[digit[i]]= i
        def str2int(num):
            tens = 1        #每一位所乘的数量级  个位-->1 十位-->10
            i = len(num)-1  #从最右端（个位）开始
            integer = 0
            while(i>=0):
                integer += dic[num[i]]*tens
                tens=tens*10
                i-=1
            return integer
        int1 = str2int(num1)
        int2 = str2int(num2)
        return str(int1+int2)
