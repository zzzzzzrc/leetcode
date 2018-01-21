class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        output = []
        dic1 = {}
        dic2 = {}
        for number in nums1:
            dic1[number] = dic1.get(number,0)+1
        for number in nums2:
            if number in dic1:
                if dic1[number] > 0:
                    if number in dic1:
                        dic1[number] -= 1
                        output.append(number)
        return output
