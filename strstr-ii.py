'''
Implement strStr function in O(n + m) time.

strStr return the first index of the target string in a source string.
The length of the target string is m and the length of the source string is n.
If target does not exist in source, just return -1.

Given source = abcdef, target = bcd, return 1.
'''

class Solution:
    # @param {string} source a source string
    # @param {string} target a target string
    # @return {int} an integer as index
    def strStr2(self, source, target):
        # Write your code here
        m = len(target)
        n = len(source)

        if m == 0:
            return 0

        import random
        mod = random.randint(1000000, 2000000)
        hash_target = 0
        m26 = 1

        for i in xrange(m):
            hash_target = (hash_target * 26 + ord(target[i]) - ord('a')) % mod
            if hash_target < 0:
                hash_target += mod

        for i in xrange(m - 1):
            m26 = m26 * 26 % mod

        value = 0
        for i in xrange(n):
            if i >= m:
                value = (value - m26 * (ord(source[i - m]) - ord('a'))) % mod

            value = (value * 26 + ord(source[i]) - ord('a')) % mod
            if value < 0:
                value += mod

            if i >= m - 1 and value == hash_target:
                return i - m + 1

        return -1
