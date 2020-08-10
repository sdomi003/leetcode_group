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
    # Recursive Solution, TLE
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         n = len(cost)
        
#         def recursive(cost, i):
#             if i in [0, 1]:
#                 return cost[i]
#             return cost[i] + min(recursive(cost, i-1), recursive(cost, i-2))
        
#         return min(recursive(cost, n-1), recursive(cost, n-2))
    
    # Top Down DP
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         n = len(cost)
#         dp = [None] * n
        
#         def recursive(cost, i):
#             if i in [0, 1]:
#                 return cost[i]
#             if dp[i]:
#                 return dp[i]
#             dp[i] = cost[i] + min(recursive(cost, i-1), recursive(cost, i-2))
#             return dp[i]
        
#         return min(recursive(cost, n-1), recursive(cost, n-2))
    
#     # Bottom Up DP
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [None] * n
        
        for i in range(n):
            if i < 2:
                dp[i] = cost[i]
            else:
                dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        return min(dp[-1], dp[-2])
