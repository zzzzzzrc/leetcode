class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        i = 0
        count = 1
        while(i<len(chars)-1):
            if chars[i] == chars[i+1]:
                del(chars[i+1])
                count+=1
            else:
                if count >=2 and count<10:
                    # chars = list(chars[:i+1])+list(str(count))+list(chars[i+1:])
                    chars.insert(i+1,str(count))
                    i += 2
                    count = 1
                elif count>=10 and count<100:
                    # chars = list(chars[:i+1])+list(str(count)[0])+list(str(count)[1])+list(chars[i+1:])
                    chars.insert(i+1,str(count)[0])
                    chars.insert(i+2,str(count)[1])
                    i += 3
                    count = 1
                elif count>=100 and count <1000:
                    # chars = list(chars[:i+1])+list(str(count)[0])+list(str(count)[1])+list(str(count)[2])+list(chars[i+1:])
                    chars.insert(i+1,str(count)[0])
                    chars.insert(i+2,str(count)[1])
                    chars.insert(i+3,str(count)[2])
                    i += 4
                    count = 1
                elif count == 1000:
                    # chars = list(chars[:i+1])+list(str(count)[0])+list(str(count)[1])+list(str(count)[2])+list(str(count)[3])+list(chars[i+1:])
                    chars.insert(i+1,str(count)[0])
                    chars.insert(i+2,str(count)[1])
                    chars.insert(i+3,str(count)[2])
                    chars.insert(i+4,str(count)[3])
                    i += 5
                    count = 1
                else:
                    i+=1
                    count = 1
        if count>1 and count<10:
            chars.insert(len(chars),str(count))
            # chars = chars+list(str(count))
        elif count>=10 and count<100:
            chars.insert(len(chars),str(count)[0])
            chars.insert(len(chars)+1,str(count)[1])
            # chars = chars+list(str(count)[0])+list(str(count)[1])
        elif count>=100 and count<1000:
            chars.insert(len(chars),str(count)[0])
            chars.insert(len(chars)+1,str(count)[1])
            chars.insert(len(chars)+2,str(count)[2])
            # chars = chars+list(str(count)[0])+list(str(count)[1])+list(str(count)[2])
        elif count == 1000:
            chars.insert(len(chars),str(count)[0])
            chars.insert(len(chars)+1,str(count)[1])
            chars.insert(len(chars)+2,str(count)[2])
            chars.insert(len(chars)+3,str(count)[3])
            # chars = chars+list(str(count)[0])+list(str(count)[1])+list(str(count)[2])+list(str(count)[3])
        return len(chars)
