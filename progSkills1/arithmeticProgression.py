class Solution:
    def canMakeArithmeticProgression(self, arr):
        # True/False: array holds arithmetic progression
        arr.sort()
        step = arr[0] - arr[1]
        for i in range(1, len(arr) - 1):
            if arr[i] - arr[i + 1] != step:
                return False
        return True

if 0:
    print(Solution().canMakeArithmeticProgression([3,5,1]))
    print(Solution().canMakeArithmeticProgression([1,2,4]))