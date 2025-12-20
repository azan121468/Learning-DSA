def topKFrequent(nums: list, k: int) -> list:
    n = len(nums)
    freq = {}

    # get frequency of each number in hashset
    for num in nums:
        freq[num] = 1 + freq.get(num, 0)
    
    #now we will put each element at index of its count. len is bound to n as this is max size of list
    bucket = [[] for _ in range(n+1)]
    for num, count in freq.items():
        bucket[count].append(num)

    ans = []
    
    for i in range(len(bucket) - 1, 0, -1):
        for val in bucket[i]:
            ans.append(val)
            if len(ans) == k:
                return ans

    return ans

# a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6]
# a = [1]
a = [1,2,1,2,1,2,3,1,3,2]
f = topKFrequent(a, 2)
print(f)