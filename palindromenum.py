"""First try, good job sam
   Now let's find a better solution"""

class Solution:
    def isPalindrome(self, x) -> bool:
        """ Solution with O(n) runtime"""
        num = str(x)
        left = 0
        right = len(num) - 1
        while left <= right:
            if num[left] != num[right]:
                return False
            left += 1
            right -= 1
        return True
    
    
