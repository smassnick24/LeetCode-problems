class Solution:
    def twoSum(self, nums, target):
        """
        Sam
        nums: list of int
        target: int
        return: list of int
        """
        nums.sort()
        print(nums)
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[right] == target:
                return [left, right]
            elif nums[left] + nums[right] < target:
                left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
        return -1
    
    def twoSumHash(self, nums, target):
        """
        Leetcode Solution
        """
        hashmap = {}
        for i, j in enumerate(nums):
            hashmap[j] = i
        for i, j in enumerate(nums):
            complement = target - j
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]
    
            
            
            
if __name__ == "__main__":
    s = Solution()
    print(s.twoSumHash([3, 4, 7, 10, 11, 3, 18], 10))
    print(s.twoSum2([3, 4, 7, 10, 11, 3, 18], 10))