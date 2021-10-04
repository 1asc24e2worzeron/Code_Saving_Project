class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        for i in range(0, len(prices)-1):
            if prices[i+1] > prices[i]:
                profit += prices[i+1] - prices[i]
                
        return profit
        
    def maxProfitBruteForce(self, prices: List[int]) -> int:
        
        if len(prices) < 2:
            return 0
        
        if len(prices) == 2:
            if prices[1] <= prices[0]:
                return 0
            else:
                return prices[1] - prices[0]
        
        profit = 0
        
        for i in range(0, len(prices)-1):
            
            maxIndex = i
            localProfit = 0
            
            for j in range(i+1, len(prices)):
                if prices[j] > prices[i]:
                    maxIndex = j
            
            if (maxIndex > i):
                localProfit = prices[maxIndex] - prices[i]
                for j in range(i+1, maxIndex+1):
                    currentProfit = self.maxProfit(prices[i:j]) + self.maxProfit(prices[j:maxIndex+1])
                    if currentProfit > localProfit:
                        localProfit = currentProfit
            
            localProfit += self.maxProfit(prices[maxIndex+1:])
            if localProfit > profit:
                profit = localProfit
                
        return profit