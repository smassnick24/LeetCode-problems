class Solution():
    def removeDuplicates(self, arr: list):
        if not arr:
            return 0
        count = 1    
        for i in range(1, len(arr)):
            if arr[i] != arr[i-1]:
                arr[count] = arr[i]
                count += 1
        
        return count
                
numbers = [1, 2, 2, 2, 3, 3]

Solution().removeDuplicates(numbers)

print(numbers)