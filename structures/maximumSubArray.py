def maxSubArray(arr: list) -> int:
    answer = float("-inf")
    maximum = 0
    
    for num in arr:
        maximum += num
        answer = max(answer, maximum)
        maximum = max(maximum, 0)
    return answer