class Solution:
    def countOdds(self, low: int, high: int) -> int:
        """Takes a range of low and high and returns
           the number of odd numbers in the range
           Low is included, high is included"""
        range_list = list(range(low, high + 1))
        oddCount = len([odd for odd in range_list if odd % 2 != 0])
        return oddCount

    def countOddsExp(self, low: int, high: int) -> int:
        """Takes a range of low and high and returns
            the number of odd numbers in the range
            Low is included, high is included"""
        if low % 2 == 1 or high % 2 == 1:
            return (high - low) // 2 + 1
        else:
            return (high - low) // 2


if __name__ == '__main__':
    print(Solution().countOdds(800445804, 979430543))
