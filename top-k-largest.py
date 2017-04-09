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



###JAVA implementation
class Solution {

     public int[] topk(int[] nums, int k) {
         PriorityQueue<Integer> minheap = new PriorityQueue<Integer>(k, new Comparator<Integer>() {
             public int compare(Integer o1, Integer o2) {
                 if(o1 < o2) {
                     return 1;
                 } else if(o1 > o2) {
                     return -1;
                 } else {
                     return 0;
                 }
             }
         });

         for (int i : nums) {
             minheap.add(i);
         }

         int[] result = new int[k];
         for (int i = 0; i < result.length; i++) {
             result[i] = minheap.poll();
         }
         return result;
    }
};
