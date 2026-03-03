# Move Zeroes
# Idea is as follow.
# 1. Start two pointers i and j at start of the list.
# 2. Now, move j until its either out of bound or has zero.
# 3. Once, loop finish if 
#    i.  j is out of bound, exit the loop
#    ii. otherwise, increment i and j, and let loop continue

def moveZeroes(nums: list[int]) -> None:
    if not nums: return
    
    n = len(nums)
    i, j = 0, 0

    while i < n and j < n:
        while j < n and nums[j] == 0:
            j += 1
        if j == n: break
        
        nums[i], nums[j] = nums[j], nums[i]

        i+=1
        j+=1

nums1 = [0,1,0,3,12]
#output: [0,1,0,3,12]
nums2 = [0]
#output: [0]

moveZeroes(nums1)
moveZeroes(nums2)

print(nums1)
print(nums2)