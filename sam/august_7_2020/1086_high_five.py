'''
Given a list of scores of different students, return the average score of each student's top five scores in the order of each student's id.

Each entry items[i] has items[i][0] the student's id, and items[i][1] the student's score.  The average score is calculated using integer division.

 

Example 1:

Input: [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
Output: [[1,87],[2,88]]
Explanation: 
The average of the student with id = 1 is 87.
The average of the student with id = 2 is 88.6. But with integer division their average converts to 88.
 

Note:

1 <= items.length <= 1000
items[i].length == 2
The IDs of the students is between 1 to 1000
The score of the students is between 1 to 100
For each student, there are at least 5 scores
'''



class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        items.sort(key = lambda x: -1*x[1]) # sort the list based on scores. Disregard IDs for now.
        #print(items)
        IDs = []
        top_5_map = {} # maps ID -> [top 5 scores]
        # now iterate through the list
        for item in items:
            curr_ID = item[0]
            curr_score = item[1]
            if (curr_ID in top_5_map and len(top_5_map[curr_ID]) < 5):
                top_5_map[curr_ID].append(curr_score)
            elif(curr_ID not in top_5_map):
                top_5_map[curr_ID] = [curr_score]
                IDs.append(curr_ID)
        
        # now sort IDs
        IDs.sort()
        
        high_five = []
        # for each ID, add ID to answer with its average
        for ID in IDs:
            high_five.append([ID, sum(top_5_map[ID])//5])
        return high_five
