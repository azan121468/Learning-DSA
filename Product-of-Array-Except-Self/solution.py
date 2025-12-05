
def productExceptSelf(nums):
    n = len(nums)
    prefix = [1]
    for i in range(0, n-1):
        prefix.append(prefix[-1] * nums[i])
    
    
    suffix = [1] * len(nums)

    for i in range(n-2, -1, -1):
        suffix[i] = nums[i+1] * suffix[i+1]

    return [p*s for p, s in zip(prefix, suffix)]

a = [1, 2, 3, 4, 5]

ans = productExceptSelf(a)

print(ans)
