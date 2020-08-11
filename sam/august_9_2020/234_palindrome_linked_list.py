'''
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
NOTE FROM SAM: O(n) solution involves modifying the input.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        N = 0
        curr = head
        while (curr):
            curr = curr.next
            N += 1
        
        # if even, compare :N//2 - 1 and N//2:
        # if odd, compare :N//2 - 1 and N//2 + 1
        
        stack = []
        curr = head
        for i in range(N//2):
            stack.append(curr.val)
            curr = curr.next
        # if odd, skip the middle element
        if (not N % 2 == 0):
            curr = curr.next
        # compare the values to the stack top
        while (curr and len(stack) > 0):
            left = stack.pop()
            if (curr.val != left):
                print("flag1")
                return False
            curr = curr.next
        if (not curr and len(stack) == 0):
            return True
        else:
            return False
            
            
