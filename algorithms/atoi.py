class Solution:
    """ Almost working solution"""
    def myAtoi(self, s: str) -> int:
        digits = {"0": 0, "1": 1, "2": 2, "3": 3,
                  "4": 4, "5": 5, "6": 6, "7": 7,
                  "8": 8, "9": 9}
        parity = False if "-" in s else True
        if "+" in s and "-" in s:
            return 0

        s = s.replace("+", "")
        s = s.replace("-", "")
        s = s.replace(" ", "")

        new_num = ""

        for i in range(len(s)):
            if s[i] in digits.keys():
                new_num += s[i]
            else:
                break
        if parity:
            x = int(new_num) if len(new_num) > 0 else 0
            return x if x < (2 ** 31) - 1 else (2 ** 31) - 1
        else:
            x = int(new_num) * -1 if len(new_num) > 0 else 0
            return x if x > (-2 ** 31) else (-2 ** 31)


if __name__ == "__main__":
    print(Solution().myAtoi("   42"))
    print(Solution().myAtoi("  -232-absc"))
    print(Solution().myAtoi("abc432"))
