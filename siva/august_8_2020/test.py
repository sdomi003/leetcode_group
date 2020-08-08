################################################################################################
# 1342	Number of Steps to Reduce a Number to Zero
################################################################################################
class Solution:
    def numberOfSteps (self, num: int) -> int:
        result = 0
        # while num != 0:
        #     if num % 2 == 0:
        #         num //= 2
        #     else:
        #         num -= 1
        #     result += 1
        # return result
        
        # Using bit wise
        while num != 0:
            if num & 1:
                num = ((num << 1) + (~num))
            else:
                num >>= 1
            result += 1
        return result
################################################################################################
# 1486	XOR Operation in an Array
################################################################################################
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        # nums = [None] * n
        # for i in range(n):
        #     nums[i] = start + 2 * i
        # result = nums[0]
        # for i in range(1, n):
        #     result ^= nums[i]
        # return result
        
        result = start
        for i in range(1, n):
            result ^= (start + (2 * i))
        return result
################################################################################################
# 1086	High Five		sorting
################################################################################################
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
#         d = collections.defaultdict(list)

#         for id, score in items:
#             d[id].append(score)

#         for id in d:
#             d[id] = sorted(d[id])[-5:]

#         return [[i, (sum(d[i]) // 5)] for i in d]

        d = collections.defaultdict(list)
        
        for id, score in items:
            heapq.heappush(d[id], score)
            
        for id in d:
            d[id] = sum(heapq.nlargest(5, d[id])) // 5
            
        return [[idx, val] for idx, val in d.items()]
################################################################################################
# 112	Path Sum
################################################################################################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        # Iterative
        
        if root is None:
            return False
        
        stack = [(root, sum - root.val)]
        while stack:
            curr_root, curr_sum = stack.pop()
            if curr_sum == 0 and not curr_root.left and not curr_root.right:
                return True
            if curr_root.left:
                stack.append((curr_root.left, curr_sum - curr_root.left.val))
            if curr_root.right:
                stack.append((curr_root.right, curr_sum - curr_root.right.val))
        return False

        # Recursive
        if root is None:
            return False
        if sum - root.val == 0 and not root.left and not root.right:
            return True
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
################################################################################################
# 997	Find the Town Judge
################################################################################################
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:            
        indegree = {i: 0 for i in range(1, N+1)}
        outdegree = {i: 0 for i in range(1, N+1)}
        
        for k, l in trust:
            outdegree[k] += 1
            indegree[l] += 1
            
        for i in range(1, N + 1):
            if indegree[i] == N - 1 and outdegree[i] == 0:
                return i
        return -1
################################################################################################
# 392	Is Subsequence
################################################################################################
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_len, t_len = len(s), len(t)
        i = j = 0
        
        while i < s_len and j < t_len:
            if s[i] == t[j]:
                i += 1
            j += 1
        
        return i == s_len
################################################################################################
# 303	Range Sum Query - Immutable
################################################################################################
class NumArray:

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
