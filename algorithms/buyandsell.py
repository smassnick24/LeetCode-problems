class Solution:
    def maxProfit(self, prices):
        """kind of works, oversights led to errors"""
        options = []
        for i in range(len(prices)): 
            if (prices[i] > prices[i-1]):
                options.append(prices[i] - prices[i-1])
        return max(options)
        
        
test_case1 = [1, 7, 6, 4, 5, 2] # buy on index 0, sell on index 2, profit = 6
test_case2 = [7, 6, 5, 4, 3] # dont buy
test_case3 = [1, 2, 3, 4, 5, 6] # buy on index 0, sell on index 5, profit = 5


print(Solution().maxProfit(test_case1))
print(Solution().maxProfit(test_case2))
print(Solution().maxProfit(test_case3))