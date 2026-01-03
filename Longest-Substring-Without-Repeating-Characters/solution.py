# Sliding window to find longest substring without repeating characters
# Idea is as follow
#1. Initialize l and r both to 0
#2. move r forward while adding s[r] to seen.
#3. if s[r] is seen, we have to keep removing s[l] and move l forward until s[r] is not in seen.
#   we don't need bound check for l as l should always stop before r.
#   this is due to fact that we don't add current s[r] so it has already occured before.
#   we only have to move l until that occurence is removed. Even in worst case l will only travel until r - 1(inclusive) at max.
#4. Find length of this windows and compare with max. if greater than max, update max
#5. move r forward and continue the loop until r reaches end of string

def lengthOfLongestSubstring(s: str) -> int:
    n = len(s)
    
    l, r = 0, 0
    seen = set()
    longest_len = 0

    while r < n:
        while s[r] in seen:
            seen.remove(s[l])
            l += 1
        
        seen.add(s[r])
        longest_len = max(longest_len, r - l + 1)

        r += 1
    
    return longest_len

        





a = 'abdedfkljm'
ans = lengthOfLongestSubstring(a)
print(ans)