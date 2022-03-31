from functools import reduce
class Solution(object):
    def arraySign(self, nums):
        # return 0 if product 0, 1 if product positive, -1 if product negative
        numsProd = 1
        for i in nums:
            numsProd *= i
        if numsProd > 0:
            return 1
        elif numsProd < 0:
            return -1
        else:
            return 0
    
    def arraySign2(self, nums):
        # return 0 if product 0, 1 if product positive, -1 if product negative
        # if don't need product
        sign = 1
        for i in nums:
            if i == 0: return 0
            if i < 0: sign *= -1
        return sign

    def arraySign3(self, nums):
        # return 0 if product 0, 1 if product positive, -1 if product negative
        # 2/3 runtime, a bit more memory
        try:
            if len(nums) == 1:
                return nums[0]/abs(nums[0])
            return reduce(lambda x, y: (x/abs(x))*(y/abs(y)), nums)
        except ZeroDivisionError:
            return 0

if 0:
    print(Solution().arraySign3([-1,-2,-3,-4,3,2,1]))
    print(Solution().arraySign3([1,5,0,2,-3]))
    print(Solution().arraySign3([9,72,34,29,-49,-22,-77,-17,-66,-75,-44,-30,-24]))