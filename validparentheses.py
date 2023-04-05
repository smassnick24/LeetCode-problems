class Solution:
    def __init__(self):
        self.test1 = "()[]{}"
        self.test2 = "(}[)"
        self.test3 = "{}[)()"
        self.test4 = "([{}])"
        self.test5 = "()[{}]"
        
        
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {")": "(", "]": "[", "}": "{"}
        
        for p in s:
            if p in hashmap.values():
                stack.append(p)
            elif stack and hashmap[p] == stack[-1]:
                stack.pop()
            else:
                return False
        return stack == []
        
    

if __name__ == "__main__":
    s = Solution()
    print(s.isValid(s.test1))
    print(s.isValid(s.test2))
    print(s.isValid(s.test3))
    print(s.isValid(s.test4))
    print(s.isValid(s.test5))