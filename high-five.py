'''
There are two properties in the node student id and scores, to ensure that each student will have at least 5 points, find the average of 5 highest scores for each person.


Given results = [[1,91],[1,92],[2,93],[2,99],[2,98],[2,97],[1,60],[1,58],[2,100],[1,61]]

Return
'''

#Definition for a Record
class Record:
    def __init__(self, id, score):
        self.id = id
        self.score = scor
class Solution:

    # <key, value> (student_id, average_score)
    def highFive(self, results):
        # Write your code here
        hash = dict()
        for r in results:
            if r.id not in hash:
                hash[r.id] = []

            hash[r.id].append(r.score)
            if len(hash[r.id]) > 5:
                index = 0
                for i in xrange(1, 6):
                    if hash[r.id][i] < hash[r.id][index]:
                        index = i

                hash[r.id].pop(index)

        answer = dict()
        for id, scores in hash.items():
            answer[id] = sum(scores) / 5.0

        return answer
