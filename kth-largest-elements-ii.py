'''
Find K-th largest element in an array. and N is much larger than k.

n array [9,3,2,4,8], the 3rd largest element is 4.

In array [1,2,3,4,5], the 1st largest element is 5, 2nd largest element is 4, 3rd largest element is 3 and etc.

'''
import heapq

class Solution:
    # @return {int} the kth largest element
    def kthLargestElement2(self, nums, k):
        # Write your code here
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)

        return heapq.heappop(heap)
