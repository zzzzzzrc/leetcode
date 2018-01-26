class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        # i = 0
        # while(i<len(letters)):
        #     if letters[i]<=target:
        #         i += 1
        #     else:
        #         return letters[i]
        # return letters[0]
        if letters[-1]<=target:
            return letters[0]
        else:
            l =0
            r = len(letters) -1
            while(l<r):
                mid = l + (r-l)//2
                if letters[mid]<=target:
                    l =mid+1
                else:
                    r = mid-1
                if l == r and letters[l]<=target:
                    return letters[l+1]
            return letters[l]

