class Solution(object):
    def odds(self, low, high):
        # return the number of odd numbers between values, inclusive
        # floor divides, then adds one if either value is odd
        odds = (high-low)//2
        if high % 2 == 0 and low % 2 == 0:
            return odds
        else:
            return odds + 1
        
if 0:
    print(Solution().odds(3,7))
    print(Solution().odds(2,7))
    print(Solution().odds(8,10))