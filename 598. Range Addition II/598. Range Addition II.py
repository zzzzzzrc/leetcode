class Solution:
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if ops == []:
            return m*n
        else:
            row = []
            col = []
            for item in ops:
                if item[0]>m:
                    item[0]=m
                row.append(item[0])
                if item[1]>n:
                    item[1]=n
                col.append(item[1])
            min_row = min(row)
            min_col = min(col)
            return min_row*min_col

