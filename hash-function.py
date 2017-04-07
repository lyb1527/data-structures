'''
Hash functions are used to convert a string or any other type into an integer smaller
than hash size and bigger or equal to zero.

A good hash function can avoid collisions as few as possible. A widely used hash function algorithm
is using a magic number 33.


Hashcode('abcd') = ascii(a)*33^3 + ascii(b)*33^2 + ascii(c)*33 + ascii(d)  % HASH size

Given a string as a key and size of the table, return the hash value of this key, f


For key="abcd" and size=100, return 78
'''

class Solution:
    def hashFunction(self, value, hashSize):
        answer = 0
        for x in value:
            answer = (answer * 33 + ord(x)) % hashSize
            print(answer)
        return answer


s = Solution()
s.hashFunction("abcd", 1000)
