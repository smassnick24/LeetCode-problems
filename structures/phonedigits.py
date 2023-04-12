"""
Given a string containing digits from 2-9 inclusive,
return all possible letter combinations that the number could represent.
Return the answer in any order.
"""

class Solution():
    """Not Completed"""
    def letterCombinations(self, digits: str) -> list:
        letters = {"1": "", "2": "abc", "3": "def", "4": "ghi",
                   "5": "jkl", "6": "mno", "7": "pqrs", 
                   "8": "tuv", "9": "wxyz"}
        combos = []
        storage = ""
        
        if len(digits) > 4:
            digits = digits[0:4]
            
        for digit in digits:
            if digit not in letters:
                raise ValueError("Expected digits in range 2-9")
            
        
        