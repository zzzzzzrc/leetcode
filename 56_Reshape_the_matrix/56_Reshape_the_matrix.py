class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """

        r_old = len(nums)
        c_old = len(nums[0])
        data_c = []
        temp = []
        output = []
        if r*c != r_old*c_old:
            return nums
        else:
            for i in range(r_old):
                for j in range(c_old):
                    temp.append(nums[i][j])
            for row in range(r):
                data_c= temp[row*c:(row+1)*c]
                output.append(data_c)
        return output
