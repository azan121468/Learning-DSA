def longestConsecutive(nums):
    nset = set(nums)
    max_consec = 0

    for num in nset:
        # 1. Validate start of sequence
        if num - 1 in nset: continue
        # 2. Keep counting while increasing value of current number to get longest count
        count = 0
        x = num
        while x in nset:
            count += 1
            x += 1
        # 3. Update maximum count if current count is greater than max_consec count so far
        max_consec = max(max_consec, count)
    
    return max_consec

nums = [1,0,1,2]
ans = longestConsecutive(nums)
print(ans)