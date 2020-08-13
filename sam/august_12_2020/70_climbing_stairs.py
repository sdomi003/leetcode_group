'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45

'''





class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        We could have gotten to step i by either:
            1. climbing 1 step to it from step i-1
            2. climbing 2 steps to it from step i-2, skipping step i-1
        Thus, the number of ways to reach step i depends on the number of ways to reach i-1 and i-2. 
        For every way of reaching step i-1, there is a way to reach step i (by doing a single step).
        Similarly, for every way of reaching step i-2, there is a way to reach step i (by doing a double step).
        
        So, num_ways[i] = num_ways[i-1] + num_ways[i-2]
        
        '''
        
        if (n == 1):
            return 1
        elif (n == 2):
            return 2
        
        
        num_ways = [0 for i in range(n + 1)]
        
        num_ways[0] = None # dummy variable
        num_ways[1] = 1 # there is only one way to reach 1 step, which is to do a single step
        num_ways[2] = 2 # there are 2 ways to reach two steps. Either 2 single steps, or one double step
        
        for i in range(3, n+1):
            num_ways[i] = num_ways[i-1] + num_ways[i-2]
        return num_ways[len(num_ways) - 1]
