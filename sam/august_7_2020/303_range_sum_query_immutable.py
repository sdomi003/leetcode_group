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
        self.nums = nums
        self.sum_from_left = []
        self.sum_from_right = [None for i in range(len(nums))]
        self.total_sum = sum(nums)
        
        self.return_0 = False
        
        if (len(nums) < 1):
            self.return_0 = True
            return
        
        self.sum_from_left.append(nums[0])
        self.sum_from_right[len(nums) - 1] = (nums[len(nums) - 1])
        
        for i in range(1, len(nums)):
            self.sum_from_left.append(self.sum_from_left[i-1] + nums[i])
        
        for i in range(len(nums) - 2, -1, -1):
            self.sum_from_right[i] = (self.sum_from_right[i+1] + nums[i])    

    def sumRange(self, i: int, j: int) -> int:
        
        if (self.return_0):
            return 0
        
        left_sum = None
        right_sum = None
        if (i == 0):
            left_sum = 0
        else:
            left_sum = self.sum_from_left[i-1]
        if (j == len(self.nums) - 1):
            right_sum = 0
        else:
            right_sum = self.sum_from_right[j+1]

        return self.total_sum - (left_sum + right_sum)

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
