'''
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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
