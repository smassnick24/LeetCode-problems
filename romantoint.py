""" Leet code does not take this answer as it says that it doesnt return the expected answer for one test case
    MCMXCIV == 2216. On leetcode, my code yields 1984 or something but when I run it on my compiler, the result is 2216.
    I dont know, man
    """

class Solution:
    def romanToInt(self, s: str) -> int:
        """ Sam's Hashmap for the win"""
        tot = 0
        hashmap = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        for letter in s:
            if letter in hashmap:
                tot += hashmap[letter]
        return tot

if __name__ == "__main__":
    test = "MCMXCIV"
    s = Solution()
    print(s.romanToInt(test))