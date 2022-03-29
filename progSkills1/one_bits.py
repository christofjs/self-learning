class Solution(object):
    def hammingWeight(self, n):
        # return the number of one bits in input
        count = 0
        for l in str(bin(n)):
            if l == "1":
                count += 1
        return count

    def hammingWeight2(self,n):
        count = 0
        while n > 0:
            n &= n - 1
            count += 1
        return count

if 0:
    print(Solution().hammingWeight2(0x0000010101000))
    print(Solution().hammingWeight2(0x0010010101001))