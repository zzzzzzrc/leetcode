class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        len_A = len(A)
        len_B = len(B)
        repeatedA = A + A
        # #A包含B
        # if B in A:                                  # A:abcd    B:cd
        #     return 1
        # elif B in repeatedA:                        # B不在A内  A也不在B内  但是符合A:abcd    B:da
        #     return 2
        # #B不包含A  则必定不符合??
        # elif A not in B:
        #     return -1
        # else:
        #     B_split = B.split(A)
        #     #若除去两端  还存在不为A的序列  不符合
        #     if len(B_split)-B_split.count('') > 2:
        #         return -1
        #     else:
        #         if B[0:len_A] not in repeatedA or B[len_B-len_A:len_B] not in repeatedA:
        #             return -1
        #         else:
        #             return B.count(A)+(B_split[0] != '')+( B_split[-1]!='')

        if len_A >= len_B:
            if B in A:
                return 1
            elif B in repeatedA:
                return 2
            else:
                return -1
        else:
            B_split = B.split(A)    # 将B按A分割  bcdabcdabcdab ----> bcd '' '' ab   bcdabcddabcdab ---> bcd '' d '' ab
            #若除去两端  还存在不为A的序列  不符合
            if len(B_split)-B_split.count('') > 2:
                return -1
            else:
                #B开始以及最后的len_A个字符串可以构成A
                if B[0:len_A] not in repeatedA or B[len_B-len_A:len_B] not in repeatedA:
                    return -1
                else:
                    #统计A的次数
                    return B.count(A)+(B_split[0] != '')+( B_split[-1]!='')


