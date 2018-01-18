class Solution:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        divisors = []
        if num <= 1:
            return False
        else:
            for i in range(1,int(num**0.5)+1):      #范围为num的平方
                if num%i==0:
                    divisors.append(i)              #找出所有能够整除的数
                    if num//i!=num:
                        divisors.append(num//i)     #num本身除外
            sum_of_divisors=0
            for item in divisors:
                sum_of_divisors += item
            return sum_of_divisors == num
