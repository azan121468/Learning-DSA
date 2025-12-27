def longestPalindrome(s):
    n = len(s)
    if n == 1: return s

    longest_len = 0
    longest_palin = ""

    # Expand from single character
    for x in range(n):
        l, r = x, x
        
        while l >= 0 and r < n and s[l] == s[r]:
            cur_len = r - l + 1
            if cur_len > longest_len:
                longest_len = cur_len
                longest_palin = s[l:r+1]
            l -= 1
            r += 1
    
    # Expand from two neighbors
    for x in range(n - 1):
        l, r = x, x+1

        while l >= 0 and r < n and s[l] == s[r]:
            cur_len = r - l + 1
            if cur_len > longest_len:
                longest_len = cur_len
                longest_palin = s[l:r+1]
            l -= 1
            r += 1
            

    return longest_palin

a = longestPalindrome('abcddcba')
print(a)