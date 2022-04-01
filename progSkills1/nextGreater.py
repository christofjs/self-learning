class Solution:
    def nextGreaterElement(self, nums1, nums2):
        # find elements in subarray nums1 in array nums2
        # return next element in nums2 larger than that element, -1 otherwise
        ngeArray = []
        for val in nums1:
            for i in range(len(nums2)):
                if i == len(nums2) - 1:
                    ngeArray.append(-1)
                    break
                elif nums2[i] == val:
                    for j in range(i+1, len(nums2)):
                        if nums2[j] > val:
                            ngeArray.append(nums2[j])
                            break
                        elif j == len(nums2) - 1:
                            ngeArray.append(-1)
                            break
                    break
        return ngeArray

    def nextGreaterElement2(self, nums1, nums2):
        # 1/10 runtime, about the same memory
        # dictionary implementation prevents repeat analysis of num2 values
        nextGreatestMap = {}
        toMapStack = []
        result = []

        toMapStack.append(nums2[0])
        for i in range(1, len(nums2)):
            while toMapStack and nums2[i] > toMapStack[-1]:
                nextGreatestMap[toMapStack.pop()] = nums2[i]
            toMapStack.append(nums2[i])
        
        for unmappedValue in toMapStack:
            nextGreatestMap[unmappedValue] = -1
        
        for val in nums1:
            result.append(nextGreatestMap[val])

        return result

if 0:
    print(Solution().nextGreaterElement2([4,1,2],[1,3,4,2]))
