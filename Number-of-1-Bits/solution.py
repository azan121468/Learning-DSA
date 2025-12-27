def hammingWeight(n: int) -> int:
    bit_count = 0
    ncopy = n #to preserve original value

    while ncopy:
        is_bit_set = ncopy & 1
        bit_count += 1 if is_bit_set else 0
        ncopy = ncopy >> 1
    
    return bit_count

n = 2147483645
ans = hammingWeight(n)
print(ans)