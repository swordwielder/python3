class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==0:
            return 0
        a=prices[0]
        b=0
        for i in prices:
            if i<a:
                a=i
            elif i-a>b:
                b=i-a
        return b
