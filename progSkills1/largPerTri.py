class Solution(object):
    def largestPerimeter(self, nums):
        # given int list nums, return largest perimeter triangle of non-zero area
        nums.sort()
        i = -1
        while nums[i] >= (nums[i-1] + nums[i-2]):
            if -i == len(nums) - 2:
                return 0
            i -= 1
        return nums[i] + nums[i-1] + nums[i-2]

if 0:
    print(Solution().largestPerimeter([2,1,2]))
    print(Solution().largestPerimeter([1,2,1]))
    print(Solution().largestPerimeter([6,1,3,2,5]))