#3Sum
#1. Sort the array
#2. For all negative values, find sum which is equal to positive of current value using two pointers technique.
#3. Check if 
#      sum is 0, you found triplet
#      sum is -ve, shrink from left to increase sum
#      sum is +ve, shrink form right to decrease sum
#4. While doing all this, take care of bound and duplicates of left, right and current element by moving pointers until previous one is not equal to current one.
def threeSum(nums: list) -> list:
    nums = sorted(nums)  #we lost original nums. To keep it simple, i don't create new list. you can
    n = len(nums)
    res = []

    i = 0
    while i < n - 2 and nums[i] <= 0:  #subtract 2 as we have to have at least two element next to current element to form a triplet.
        l, r = i + 1, n - 1   #search space of remaining array after i-th element
        while l < r:    #two pointers search between l and r.
            cur_sum = nums[i] + nums[l] + nums[r]
            if cur_sum > 0:
                r -= 1
            elif cur_sum < 0:
                l += 1
            else:
                res.append([nums[i], nums[l], nums[r]])
                l += 1
                #since, we want to avoid duplicate, we will move l until either l cross bound or is equal to previous l.
                #also, we can move any of pointer we, want. l is easy to check bound for as it go toward n, so i choose l.
                #issue, with r is that in addition to taking care of bound, we also have to take care if we enter -ve, so i use left.
                while l < r and nums[l-1] == nums[l]:
                    l += 1
                r -= 1
        
        i += 1
        while i < n and nums[i - 1] == nums[i]:  #we will move i until i is either out of bound or is equal to previous i.
            i += 1

    print(res)
    return res


# input = [-4, 4, 3, 1, 5]
# input = [0,0,0]
input = [-1, -1, 0, 1, 1]
threeSum(input)