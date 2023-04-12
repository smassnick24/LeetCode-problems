class Solution:
    def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
        """list1 has length m+n where m = len(list1) and n = len(list2)
           the length of n in list one is trailing zeros
           merge in-place"""
        for i in range(len(nums2)):
            nums1[i+m] = nums2[i]
        nums1.sort()
            
            
if __name__ == "__main__":
    Solution().merge([1, 3, 7, 0, 0, 0], 3, [5,5,5], 3)
            