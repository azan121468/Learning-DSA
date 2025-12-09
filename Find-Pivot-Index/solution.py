def pivotIndex(nums):
    n = len(nums)

    #1. Find Perfix Sum for each element in array
    prefixSum = [0] * n

    for i in range(1, n):
        prefixSum[i] = prefixSum[i-1] + nums[i-1]
    
    #2. Find Suffix Sum for each element in array
    suffixSum = [0] * n

    for i in range(n - 2, -1, -1):
        suffixSum[i] = suffixSum[i+1] + nums[i+1]
    
    #3. Find at what index prefix and suffix sum meet
    for i in range(n):
        if prefixSum[i] == suffixSum[i]:
            return i

    return -1

a = [1,7,3,6,5,6]
pI = pivotIndex(a)
print(pI)