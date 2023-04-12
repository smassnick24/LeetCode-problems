class Solution:

    def containsDuplicates(self, nums: list) -> bool:
        """
        Returns true if the array contains duplicates
        Returns false if the array does not contain duplicates
        """
        hashmap = {}
        for i, j in enumerate(nums):
            if j in hashmap:
                return True
            else:
                hashmap[j] = 1
        return False


if __name__ == '__main__':
    test_case1 = [1, 2, 2, 3]
    test_case2 = [1, 2, 3, 4]

    s = Solution()
    print(s.containsDuplicates(test_case1))
    print(s.containsDuplicates(test_case2))
