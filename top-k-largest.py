'''
Given an integer array, find the top k largest numbers in it


Given [3,10,1000,-99,4,100] and k = 3.
Return [1000, 100, 10].
'''


import heapq

class Solution:

    # return : the top k largest numbers in array

    def topK(self, nums, k):
        heapq.heapify(nums)
        topk = heapq.nlargest(k, nums)
        topk.sort()
        topk.reverse()
        return topk


a = [3,10,1000,-99,4,100]
s = Solution()
print(s.topK(a, 3))
