'''
From any string, we can form a subsequence of that string by deleting some number of characters (possibly no deletions).

Given two strings source and target, return the minimum number of subsequences of source such that their concatenation equals target. If the task is impossible, return -1.

 

Example 1:

Input: source = "abc", target = "abcbc"
Output: 2
Explanation: The target "abcbc" can be formed by "abc" and "bc", which are subsequences of source "abc".
Example 2:

Input: source = "abc", target = "acdbc"
Output: -1
Explanation: The target string cannot be constructed from the subsequences of source string due to the character "d" in target string.
Example 3:

Input: source = "xyz", target = "xzyxz"
Output: 3
Explanation: The target string can be constructed as follows "xz" + "y" + "xz".
 

Constraints:

Both the source and target strings consist of only lowercase English letters from "a"-"z".
The lengths of source and target string are between 1 and 1000.
'''
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        '''
        imagine target is 1 letter, can I make source == target with some subtractions?
        imagine target is 2 letters, can I make source == target with some sub?
            can I do it with the remaining letters of source from the 1 letter sub problem?
            if yes, do it
            if no, add 1 to the counter and imagine I am starting out with a new source
        '''
        
        p_source = float('inf') # source pointer, holds curr index
        p_target = 0 # target pointer, holds curr index
        
        # hash map for letters in source {letter -> [indices this letter appears at]}
        source_pos = {}
        for i in range(len(source)):
            if (source[i] in source_pos):
                source_pos[source[i]].append(i)
            else:
                source_pos[source[i]] = [i]
                
        # iterate through target and update p_source & sub_needed accordingly
        sub_needed = 0
        for letter in target:
            target_letter_found = False
            # handle case where it's impossible to match
            if (letter not in source_pos):
                return -1
            # iterate through positions
            for pos in source_pos[letter]:
                if (p_source < pos):
                    p_source = pos
                    target_letter_found = True
                    break
            if (not target_letter_found):
                # set p_source to first occurence of target letter
                # increase sub_needed
                p_source = source_pos[letter][0]
                sub_needed += 1
        return sub_needed
