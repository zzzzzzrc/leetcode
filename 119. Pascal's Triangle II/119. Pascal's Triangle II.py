class Solution:
    def getRow(self, rowIndex):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        list = []
        if rowIndex == 0:
            list=[1]
            return [1]
        elif rowIndex == 1:
            list=[[1],[1,1]]
            return [1,1]

        #elif rowIndex == 2:
         #   list=[[1],[1,1]]
        else:
            list.append([1])
            list.append([1,1])
            for i in range(2,rowIndex+1):
                a = []
                a.append(1)
                for j in range(1,i):
                    a.append(list[i-1][j-1]+list[i-1][j])
                a.append(1)
                list.append(a)
                if i == rowIndex:
                    return a
