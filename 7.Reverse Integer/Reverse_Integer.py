class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        def get_tens(num):
            n = 1
            a = num
            while(a>=10):
                n = n *10
                a = num//n
            return n
        def get_digit(num):
            "get every bit of x"
            a = num//10 #12345 ——> 1234
            b = num%10  #12345 ——> get 5
            return a,b
        output = 0
        n = get_tens(x)
        if x>= 0:
            while(x!=0):
                x,digit = get_digit(x)
                output += digit*n
                n = n//10
            if output <= 2**31:
                return output
            else:
                return 0
        else:
            m = -1*x
            n = get_tens(m)
            while(m!=0):
                m,digit = get_digit(m)
                output += digit*n
                n = n//10
            output = -1*output
            if output >= -2**31:
                return output
            else:
                return 0


