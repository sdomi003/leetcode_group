'''
In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

 

Example 1:

Input: N = 2, trust = [[1,2]]
Output: 2
Example 2:

Input: N = 3, trust = [[1,3],[2,3]]
Output: 3
Example 3:

Input: N = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
Example 4:

Input: N = 3, trust = [[1,2],[2,3]]
Output: -1
Example 5:

Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output: 3
 

Constraints:

1 <= N <= 1000
0 <= trust.length <= 10^4
trust[i].length == 2
trust[i] are all different
trust[i][0] != trust[i][1]
1 <= trust[i][0], trust[i][1] <= N

'''


class Solution:
    # O(N) space and time, but not as good as GraphSolution
    def HashMapSolution(self, N: int, trust: List[List[int]]) -> int:
        # if list is empty, just return -1
        if (len(trust) < 1 and N == 1):
            return 1
        elif (len(trust) < 1):
            return -1
        
        seen_trusting = set() # a set of all people who have trusted someone before
        number_trusted = {} # maps {ID -> number of people that trust this ID}
        
        for i in range(len(trust)):
            ID = trust[i][0]
            trusted = trust[i][1]
            
            # add the trusting person to the list of people who have trusted at least 1 person
            if (ID not in seen_trusting):
                seen_trusting.add(ID)
                
            # increase the count of the number of times a person has been trusted
            if (trusted in number_trusted):
                number_trusted[trusted] += 1
            else:
                number_trusted[trusted] = 1
                
        # now, for each ID, check to see if it has never trusted anyone AND if everyone trusted him
        for ID in number_trusted:
            if (ID not in seen_trusting and number_trusted[ID] == N-1):
                return ID
        
        # we weren't able to find someone who never trusts but is trusted by all
        return -1
        
        
    # also O(N) space and time, but does take up less space
    def GraphSolution(self, N: int, trust: List[List[int]]) -> int:
        '''
        The idea is that for each ID, the person with that ID trusts no one. 
        But at the same time, everyone trusts this ID.
        This must meen that we can simply create a list of size N to keep track of how many people trust each ID.
        So every time you see someone trust an ID, go to the list and increase its count at that index.
        But also, every time you see an ID trust someone else, go to the list and decrease to count.
        What you're left with is one spot in the list who's value is equal to N - 1.
        OR if you can't find such an ID, return -1
        '''
        
        scores = [0] * (N)
        print(scores)
        
        for t in trust:
            scores[t[0]-1] -= 1
            scores[t[1]-1] += 1
        for i in range(len(scores)):
            if (scores[i] == N-1):
                return i + 1
        return -1
        
        
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        '''
        TJ = town judge
        TJ CAN'T show up in trust[i][0]
        TJ MUST show up in trust[i][1] exactly N-1 times in order for everyone to trust him
        ''' 
        return self.GraphSolution(N, trust)
        
            
            
    
