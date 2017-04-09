'''
ugly number is a number that only has factors of 2, 3, and 5

design an algo to find the nth ugly number. The first 10 ugly numbers are
1, 2, 3, 4, 5, 6, 8, 9, 10, 12...

If n=9, return 10

'''
import heapq

class Solution:
    #@return {int} the nth prime number as description.
    def nthUglyNumber(self, n):
        if n <= 1:
            return n

        n -= 1
        key = [2, 3, 5]
        h = []
        for i in range(3):
            heapq.heappush(h, (key[i], i))

        value = key[0]
        while n > 0:
            value, level = heapq.heappop(h)
            while level < 3:
                new_value = key[level] * value
                heapq.heappush(h, (new_value, level))
                level += 1
            n -= 1
        return value
