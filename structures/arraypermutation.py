class Solution:
    def buildArray(self, nums: list) -> list:
        built = [0]*len(nums)
        for i in range(len(nums)):
            built[i] = nums[i]
        for j in range(len(nums)):
            built[j] = nums[built[j]]
    

arr = [5, 2, 0, 3, 1]
Solution().buildArray(arr)