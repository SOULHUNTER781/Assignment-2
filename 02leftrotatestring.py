def reverse(A,low,high):
    n = high - low
    n //= 2
    for i in range(n):
        A[i+low] , A[high-1-i] = A[high-1-i] , A[i+low]

def rotate(A,d,n):
    reverse(A,0,d)
    reverse(A,d,n)
    reverse(A,0,n)

l = list((input()))
d = int(input())
d %= len(l)
rotate(l,d,len(l))
for x in l:
    print(x, end = "")
print()

