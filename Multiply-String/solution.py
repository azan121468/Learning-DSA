def multiply_by_single_digit(a, b):
    assert len(b) == 1, "Second digit must be single"
    n1 = list(a)
    n2 = list(b)
    out = ""

    carry = 0
    d2 = int(n2[-1])
    while n1:
        d1 = int(n1.pop())
        ans = d1 * d2 + carry
        out += str(ans % 10)
        carry = ans // 10
    
    if carry:
        out += str(carry)
    
    out = out[::-1]
    return int(out)

def multiply(num1: str, num2: str) -> str:
    numm2 = list(num2) #numm2 instead of num2 to retain original variable with value

    ans = 0
    i = 0
    
    while numm2:
        d2 = numm2.pop()
        
        prod = multiply_by_single_digit(num1, d2)
        prod *= 10 ** i
        
        ans += prod

        i += 1

    return ans 

a = "9337"
b = "93"

ans = multiply(a, b)
print(f"{a} * {b} = {ans}")

# assert int(a) * int(b) == ans