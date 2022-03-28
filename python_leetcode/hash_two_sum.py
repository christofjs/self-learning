class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashtable = {}
        for i in range(len(nums)):
            hashtable[nums[i]] = i
        for i in range(len(nums)):
            second = target - nums[i]
            if second in hashtable and hashtable[second] != i:
                return [i, hashtable[second]]
