'''
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
Note:
cost will have a length in the range [2, 1000].
Every cost[i] will be an integer in the range [0, 999].
'''
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # simply put, dp[i] = min(cost[i-1], cost[i-2]) + cost[i]
        # so we need to initialize our dp with 2 stair costs hard-coded
        
        if (len(cost) == 0):
            return 0
        elif(len(cost) == 1):
            return cost[0]
        elif(len(cost) == 2):
            return cost[1]
        
        
        dp = [None for i in range(len(cost))]
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        for i in range(2, len(cost)):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
            
        i += 1
        return min(dp[i-1], dp[i-2])
