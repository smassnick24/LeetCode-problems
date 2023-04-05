class Solution:
    def romanToInt(self, s: str) -> int:
        """ Sam's Hashmap for the win"""
        tot = 0
        hashmap = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        for i in range(len(s)):
            if i + 1 < len(s) and hashmap[s[i]] < hashmap[s[i+1]]:
                tot -= hashmap[s[i]]
            else:
                tot += hashmap[s[i]]  
        return tot

if __name__ == "__main__":
    test = "MCMXCIV"
    s = Solution()
    print(s.romanToInt(test))