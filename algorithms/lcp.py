# Longest common prefix

# plan
# look at each word simultaneously
# check the nth letter. if all the same, append the letter to prefix
# if the letter is not the same, return prefix

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = ""
        for index, c in enumerate(strs[0]):
            if all(s[index] == c for s in strs):
                prefix += c
            else:
                return prefix
        return prefix

if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonPrefix([""]))