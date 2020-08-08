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
class Solution:
    
    # technically, this recursive approach is also a DFS solution. Just a recursive DFS.
    def recursive_solution(self, curr, past_sum, target):
        if (not curr):
            return False
        elif (curr.left or curr.right):
            if (self.recursive_solution(curr.left, curr.val + past_sum, target) or self.recursive_solution(curr.right, curr.val + past_sum, target)):
                return True
            else:
                return False
        else:
            return True if curr.val + past_sum == target else False
        
    # DFS iteratively
    # stack contains [[node, curr_sum], [node, curr_sum], [node, curr_sum], etc]
    def iterative_DFS_solution(self, root, target):
        if (not root):
            return None
        stack = []
        stack.append([root, 0])
        while (len(stack) > 0):
            curr = stack.pop()
            curr_node = curr[0]
            if (curr_node.left or curr_node.right):
                if (curr_node.left):
                    stack.append([curr_node.left, curr_node.val + curr[1]])
                if (curr_node.right):
                    stack.append([curr_node.right, curr_node.val + curr[1]])  
            else:
                print (curr_node.val + curr[1])
                # leaf node reached, check if sum is valid
                if (curr_node.val + curr[1] == target):
                    return True
        # if we reach this point, we looked at all paths and never found a valid one
        return False
    
    
    
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        #return self.recursive_solution(root, 0, sum)
        return self.iterative_DFS_solution(root, sum)
