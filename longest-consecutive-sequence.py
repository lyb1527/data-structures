'''
Given an unsorted array of integers, find the length of the longest consecutive
elements sequence

MUST IN O(n) complexity

Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

'''

class Solution:
    # @param nums, a list of integer
    # @return an integer
    def longestConsecutive(self, nums):
        nums.sort()
        left = nums[0]
        answer = 1
        tmp = 1
        for n in nums:
            if(n - left == 0):
                continue;
            elif(n - left == 1):
                tmp += 1
            else:
                if tmp > answer:
                    answer = tmp
                tmp = 1
            l = n
        if tmp > answer:
            answer = tmp
        return answer
