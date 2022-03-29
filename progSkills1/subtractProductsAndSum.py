from functools import reduce
class Solution(object):
    def subtractProductAndSum(self, n):
        # return the difference between the product of digits and sum of digits
        prod_digs = 1
        sum_digs = 0
        while n > 0:
            dig = n % 10
            sum_digs += dig
            prod_digs *= dig
            n //= 10
        return prod_digs - sum_digs
    
    def subtractProductAndSum2(self, n):
        # 3/4 runtime, about the same memory
        a = [int(x) for x in str(n)]
        return reduce(lambda x, y: x * y, a) - sum(a)

if 1:
    print(Solution().subtractProductAndSum2(234))
    print(Solution().subtractProductAndSum2(4421))
        