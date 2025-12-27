def reverseBits(n):
    out = 0

    for _ in range(32): #since we are given 32 bit signed integer
        bit = n & 1
        # out = out << 1
        # out |= bit
        out = (out << 1) | bit
        n = n >> 1
    
    return out

n = 43261596
ans = reverseBits(n)
print(ans)