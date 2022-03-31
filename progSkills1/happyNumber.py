class Solution:
    def isHappy(self,n):
        # determine if n is happy, return True if so
        # happy:
        #   replace n with sum of squares of digits
        #   repeat until it equals 1 or loops on non-1
        #   if 1, happy
        visited = []
        while n not in visited:
            visited.append(n)
            digits = [int(x) for x in str(n)]
            n = 0
            for i in digits:
                n += i**2
            if n == 1: return True
        return False

    def isHappy2(self,n):
        # Floyd Cycle implementation - slower and more memory consumed
        slow = self.squareDigits(n)
        fast = self.squareDigits(self.squareDigits(n))
        while slow != fast:
            slow = self.squareDigits(slow)
            fast = self.squareDigits(self.squareDigits(fast))
        return fast == 1

    def squareDigits(self,n):
        return sum([int(x)**2 for x in str(n)])

if 0:
    print(Solution().isHappy2(19))
    print(Solution().isHappy2(2))
