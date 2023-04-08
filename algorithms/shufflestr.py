class Solution:
    def restoreString(self, s: str, indices: list) -> str:
        hashmap = {}
        restored_intermediate = [0 for n in range(len(s))]
        for i in range(len(s)):
            hashmap[indices[i]] = s[i]
        for j in range(len(hashmap.keys())):
            restored_intermediate[j] = hashmap[j]
        return "".join(restored_intermediate)



if __name__ == '__main__':
    print(Solution().restoreString("codeleet", [4, 5, 6, 7, 0, 2, 1, 3]))

