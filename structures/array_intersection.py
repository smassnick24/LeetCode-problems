class Solution:
    def intersect(self, nums1: list, nums2: list) -> list:
        nums1.sort()
        nums2.sort
        i = j = 0
        ans = []
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += i
            else:
                ans.append(nums1[i])
                i += 1
                j += 1
        return ans
            
            
    
if __name__ == "__main__":
    pass
    
    
        