class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        maxprofit = 0
        if len(prices)>0:
            minprice = prices[0]
            for i in range(1,len(prices)):
                if prices[i]<minprice:
                    minprice = prices[i]

                else:
                    if prices[i] - minprice > maxprofit:
                        maxprofit = prices[i] - minprice

        return maxprofit
