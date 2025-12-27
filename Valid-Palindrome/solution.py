def isPalindrome(s: str) -> bool:
    sb = str(s).lower()
    n = len(sb)

    l, r = 0, n-1

    while l <= r:
        while l < r and not sb[l].isalnum():
            l += 1
        while r > l and not sb[r].isalnum():
            r -= 1
        
        if sb[r] != sb[l]: return False
        
        l += 1
        r -= 1
    
    return True

print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))
print(isPalindrome(" "))