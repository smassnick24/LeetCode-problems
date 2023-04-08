# find the longest substring without repeating characters
# given a string s, find the longest substring without repeating characters

class Solution:
    @staticmethod
    def lengthOfLongestubstring(string):
        """Works in most cases, not all"""
        longest = ""
        substring = ""
        sub_list = []
        for i in range(len(string)):
            if string[i] in substring:
                sub_list.append(substring)
                substring = "" + string[i]
            else:
                substring += string[i]
        for i in range(len(sub_list)):
            if len(sub_list[i]) > len(longest):
                longest = sub_list[i]
        return len(longest)


if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("aabcderfffghe"))
