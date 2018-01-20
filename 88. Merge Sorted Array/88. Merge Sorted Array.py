class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        #从后往前进行融合
        #先比较位于数组末端的数 大的放在nums1的末端 依次遍历
        pnum1 = m-1  #num1数据指针
        pnum2 = n-1     #num2数据指针
        pnew  = m+n-1       #融合数组指针
        while(pnum1>=0 and pnum2>=0):
            if nums1[pnum1] >= nums2[pnum2]:    #num1的数大
                nums1[pnew] = nums1[pnum1]
                pnum1 -= 1                      #num1的数据地址指针-1
                pnew -= 1                       #newarray的地址指针-1
            else:
                nums1[pnew] = nums2[pnum2]
                pnum2 -= 1
                pnew -= 1
        if pnum1<0:  #数组1数据全部遍历
            for p in range(pnum2+1):
                nums1[p] = nums2[p]   #将数组2剩下的元素插入
        if pnum2<0: # 数组2数据全部遍历完
            for p in range(pnum1+1):
                nums1[p] = nums1[p]
