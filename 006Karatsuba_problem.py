def count_digits(a):
    count = 0
    while a != 0:
        count += 1
        a //= 10
    return count

def power(a,b):
    return pow(a,b)

def karatsubaMul(a, b):
    dig_a = count_digits(a)
    dig_b = count_digits(b)
    dig = max(dig_a,dig_b)
    ref = dig//2
    if dig <= 1:
        return a*b
    else:
        p = (a//power(10,ref))
        q = (b//power(10,ref))
        r = a - (p*power(10,ref))
        s = b - (q*power(10,ref))
        prod1 = karatsubaMul((p+r),(q+s))
        prod2 = karatsubaMul(p,q)
        prod3 = karatsubaMul(r,s)
        
        return prod2*power(10,2*ref) + (prod1-prod2-prod3)*power(10,ref) + prod3

l , m = map(int,input().split())
print(karatsubaMul(l,m))
    
    
