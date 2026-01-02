#greedy approach
#we set target to index of last element.
#then we move jumping index towarding left while checking if value at that index can
#jump to target index. if it can, we update target idx to jumping idex
#we move jmp_idx past till -1, as when -1 is reached
#if num was reachable, it means we are past list and target can be our starting point
#as it follow alongs with us till start of the list.

def canJump(nums: list) -> bool:
    n = len(nums)

    if n == 1: return True

    tgt_idx = n - 1
    jmp_idx = n - 2

    while jmp_idx >= 0:
        jmp_len = tgt_idx - jmp_idx
        if nums[jmp_idx] >= jmp_len:
            tgt_idx = jmp_idx
        jmp_idx -= 1

    #by the time jmp_idx reach -1, tgt_idx should be 0 otherwise we can't jump to last value
    return tgt_idx == 0

nums = [1, 2, 3, 4]
ans = canJump(nums)
print(ans)

