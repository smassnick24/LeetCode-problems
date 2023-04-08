class Solution:
    def reverse(self, x: int) -> int:
        new = ""
        list1 = []
        parity = True if x >= 0 else False
        x = str(x).replace("-", "")
        for i in range(len(x)):
            list1.append(str(x)[i])
        while list1:
            new += list1.pop()
        if parity:
            if int(new) >= (2 ** 31) - 1:
                return 0
            else:
                return int(new)
        else:
            if int(new) * -1 <= (-2 ** 31):
                return 0
            else:
                return int(new) * -1


if __name__ == '__main__':
    # print(Solution().reverse(123))
    print(-8463847412 < -2**31)
