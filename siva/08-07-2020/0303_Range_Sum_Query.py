'''
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:

Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
 

Constraints:

You may assume that the array does not change.
There are many calls to sumRange function.
0 <= nums.length <= 10^4
-10^5 <= nums[i] <= 10^5
0 <= i <= j < nums.length
'''

class NumArray:

    '''
    [-2, 0, 3, -5, 2, -1]
      0. 1. 2.  3. 4.  5.
      
    total_sum = -3
    
    sum from the left to curr
    sum_from_left = [-2, -2, 1, -4, -2, -3]
    
    sum from the right to curr
    sum_from_right = [-3,-1,-1,-4,1,-1]
    
    sum of range i->j is simply
    total_sum - (sum_from_left[i-1] + sum_from_right[j+1])       
    '''
    
    
    def __init__(self, nums: List[int]):
        if not nums:
            return
        self.nums = nums
        self.n = len(self.nums)
        self.dp = [None] * self.n
        self.dp[0] = nums[0]
        for i in range(1, self.n):
            self.dp[i] = self.nums[i] + self.dp[i - 1]

    def sumRange(self, i: int, j: int) -> int:
        if i == 0:
            return self.dp[j]
        return self.dp[j] - self.dp[i-1]


class NumArray:

    def __init__(self, nums: List[int]):
        if not nums:
            return
        self.nums = nums
        for i in range(1, len(self.nums)):
            self.nums[i] = self.nums[i] + self.nums[i - 1]

    def sumRange(self, i: int, j: int) -> int:
        if i == 0:
            return self.nums[j]
        return self.nums[j] - self.nums[i-1]

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
