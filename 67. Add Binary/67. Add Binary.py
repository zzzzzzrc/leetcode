class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        length_a = len(a)
        length_b = len(b)
        i = length_a - 1
        j = length_b - 1
        c_flag = 0
        output = ""
        while(i>=0 and j>=0):
            if int(a[i])+int(b[j])+c_flag == 3:
                c_flag = 1
                output = "1" + output
                i -= 1
                j -= 1


            elif int(a[i])+int(b[j])+c_flag == 2:
                c_flag = 1
                output = "0" + output
                i -= 1
                j -= 1
            elif int(a[i])+int(b[j])+c_flag == 1:
                c_flag = 0
                output = "1" + output
                i -= 1
                j -= 1
            else:
                c_flag = 0
                output = "0" + output
                i -= 1
                j -= 1
        if i <0 and j >= 0:
            while(j>=0):
                if int(b[j])+c_flag == 2:
                    c_flag = 1
                    output = "0" + output
                    j -= 1
                elif int(b[j])+c_flag == 1:
                    c_flag = 0
                    output = "1" + output
                    j -= 1
                else:
                    c_flag = 0
                    output = "0" + output
                    j -= 1
        elif i>=0 and j < 0:
            while(i>=0):
                if int(a[i])+c_flag == 2:
                    c_flag = 1
                    output = "0" + output
                    i -= 1
                elif int(a[i])+c_flag == 1:
                    c_flag = 0
                    output = "1" + output
                    i -= 1
                else:
                    c_flag = 0
                    output = "0" + output
                    i -= 1

        if c_flag == 1:
            output = "1" + output


        return output

