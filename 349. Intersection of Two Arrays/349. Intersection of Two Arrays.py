class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        intersection = []
        dic1 = {}
        dic2 = {}
        for item in nums1:
            dic1[item] = dic1.get(item,0)+1
        for item in nums2:
            if item in dic1:
                if item not in dic2:
                    dic2[item] = dic2.get(item,0)+1
                    intersection.append(item)
        return intersection
