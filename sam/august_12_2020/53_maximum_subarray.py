'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        Keep track of the largest seen.
        At each i, we have 3 possible situations
            1. adding this number would make the value negative, so drop the continous subarray and start fresh with the next index
            2. adding this number would make the value higher/lower but still positive, in which case keep the subarray
            3. this number alone is bigger than any sum we've seen before
        '''
        if (len(nums) < 1):
            return 0
        elif (len(nums) < 2):
            return nums[0]
        
        
        largest_seen = nums[0]
        curr_sum = nums[0] if nums[0] > 0 else 0
        for i in range(1, len(nums)):
            curr_sum += nums[i]
            if (curr_sum < nums[i]):
                curr_sum = nums[i]
            if (curr_sum > largest_seen):
                largest_seen = curr_sum
        return largest_seen
