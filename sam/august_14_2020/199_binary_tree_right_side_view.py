'''
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # Keep track of the level we're on by creating a new queue for each level
    def process_level(self, queue, answer):
        next_level = []
        for i in range(len(queue)):
            if (queue[i].left):
                next_level.append(queue[i].left)
            if(queue[i].right):
                next_level.append(queue[i].right)
        # process last item in list
        answer.append(queue[len(queue) - 1].val)
        return next_level
        
    def rightSideView(self, root: TreeNode) -> List[int]:
        if (not root):
            return []
        # at every level, what is the right-most node? Simple BFS and take the last element
        queue = []
        curr = root
        queue.append(root)
        answer = []
        while (queue):
            queue = self.process_level(queue, answer)
        return answer
