class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # min_price=prices[0]

        # max_profit=0

        # for price in prices:

        #     min_price=min(price,min_price)

        #     profit=price-min_price

        #     max_profit=max(profit,max_profit)

        # return max_profit

        #or

        i=0
        j=1
        max_price=0
        while j<len(prices):
            s=prices[j]-prices[i]
            if s>max_price:
                max_price=s
            
            if prices[i]> prices[j]:
                i=j
            j+=1
        return max_price

