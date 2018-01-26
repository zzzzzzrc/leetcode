class Solution:
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        #对于houses中的每一个 寻找最近的heater 并计算距离  求这个最大距离
        # output = 0
        # for i in range(len(houses)):
        #     distance = abs(houses[i]-heaters[0])
        #     for j in range(len(heaters)):
        #         distance = min(distance,abs(houses[i]-heaters[j]))
        #     output = max(distance,output)
        # return output
        ########################TLE####################################
        houses = sorted(houses)
        heaters = sorted(heaters)
        houses_num = len(houses)
        heaters_num = len(heaters)
        output = 0
        distance = 0
        j = 0
        for i in range(houses_num):
            #j = 0                        注意j不用每次重新置0   heat[j] <house[i]< heat[j+1]    必有 house[i+1]>heat[j] 但是heat[j+1]需判断
            if houses[i]<heaters[0]:
                distance = heaters[0]-houses[i]
            else:
                while(j<heaters_num and houses[i]>=heaters[j]):                     #当heat[j] <house[i]< heat[j+1] 时或者 j=heaters_num
                    j+= 1
                if j == heaters_num:
                    distance = houses[i] - heaters[j-1]                             #house一直大于heat
                else:
                    distance = min(houses[i]-heaters[j-1],heaters[j]-houses[i])     #house再两个heat中间
            output = max(output,distance)
        return output
