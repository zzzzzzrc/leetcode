class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        #Newton iteration  #精度问题
        #n[i+1] = 1/2*(n[i]+num/n[i])
        #abs(n[i+1]-n[i])<threshold break
        a = num         # n
        delta = num     # 差值
        threshold = 0.01      # 计算精度
        while(delta>threshold):
            b = 1/2*(a+num/a)
            delta = abs(b-a)
            a = b
        integer = int(a)    #平方根取整
        if integer**2==num:      # 验证是否为num的平方根
            return True
        else:
            return False
