'''
In a deck of cards, each card has an integer written on it.

Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:

Each group has exactly X cards.
All the cards in each group have the same integer.
 

Example 1:

Input: deck = [1,2,3,4,4,3,2,1]
Output: true
Explanation: Possible partition [1,1],[2,2],[3,3],[4,4].
Example 2:

Input: deck = [1,1,1,2,2,2,3,3]
Output: false´
Explanation: No possible partition.
Example 3:

Input: deck = [1]
Output: false
Explanation: No possible partition.
Example 4:

Input: deck = [1,1]
Output: true
Explanation: Possible partition [1,1].
Example 5:

Input: deck = [1,1,2,2,2,2]
Output: true
Explanation: Possible partition [1,1],[2,2],[2,2].
 

Constraints:

1 <= deck.length <= 10^4
0 <= deck[i] < 10^4
'''
class Solution:
    def common_divisor_solution(self, deck):
        # count occurences
        # find a common divisor in the counts
        counts = {} # maps number -> number of times seen
        largest_count = 0
        for num in deck:
            if (num in counts):
                counts[num] += 1
                if (counts[num] > largest_count):
                    largest_count = counts[num]
            else:
                counts[num] = 1
                if (counts[num] > largest_count):
                    largest_count = counts[num]
                    
        if (largest_count < 2):
            return False
        
        # at this point, I have the counts. Find common divisor
        for count in counts:
            print(count, counts[count])
            
        print(largest_count)
        for i in range(2, largest_count+1):
            div_by_all = True
            for count in counts:
                if (counts[count] % i != 0):
                    div_by_all = False
                    break
            if (div_by_all):
                return True
        return False
    
    
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        return self.common_divisor_solution(deck)
